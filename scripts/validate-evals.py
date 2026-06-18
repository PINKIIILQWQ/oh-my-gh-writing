#!/usr/bin/env python3
"""Validate lightweight eval fixtures without external dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"

OUTPUT_TYPES = {
    "markdown-artifact",
    "yaml-artifact",
    "multi-file-package",
    "routing-only",
}
RISK_CATEGORIES = {
    "routing",
    "format",
    "evidence",
    "cleanliness",
    "workflow",
    "language",
}
REQUIRED_FIELDS = {
    "id",
    "prompt",
    "expected_route",
    "output_type",
    "risk_category",
    "expected_output",
    "assertions",
}
OPTIONAL_FIELDS = {"expected_file", "must_contain", "must_not_contain"}
ALLOWED_EVAL_FIELDS = REQUIRED_FIELDS | OPTIONAL_FIELDS


def load_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except Exception as exc:  # noqa: BLE001 - report parse path clearly
        raise ValueError(f"{path.relative_to(ROOT)} is not valid JSON: {exc}") from exc


def require_list(value: object, field: str, eval_id: str) -> list[object]:
    if not isinstance(value, list):
        raise ValueError(f"{eval_id}: `{field}` must be an array")
    return value


def require_non_empty_string(value: object, field: str, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context}: `{field}` must be a non-empty string")
    return value


def require_string_list(value: object, field: str, context: str, *, non_empty: bool) -> list[str]:
    items = require_list(value, field, context)
    if non_empty and not items:
        raise ValueError(f"{context}: `{field}` must not be empty")
    for index, item in enumerate(items, start=1):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(
                f"{context}: `{field}` item #{index} must be a non-empty string"
            )
    return items


def validate_trigger_queries() -> None:
    data = load_json(EVALS / "trigger-queries.json")
    if not isinstance(data, dict):
        raise ValueError("evals/trigger-queries.json must be a JSON object")
    if data.get("skill_name") != "oh-my-gh-writing":
        raise ValueError(
            "evals/trigger-queries.json: `skill_name` must be `oh-my-gh-writing`"
        )

    queries = data.get("queries")
    if not isinstance(queries, list) or not queries:
        raise ValueError("evals/trigger-queries.json: `queries` must be a non-empty array")

    seen_queries: set[str] = set()
    positives = 0
    negatives = 0
    for index, item in enumerate(queries, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"trigger query #{index}: item must be an object")
        if set(item) != {"query", "should_trigger"}:
            raise ValueError(
                f"trigger query #{index}: fields must be exactly `query` and `should_trigger`"
            )

        query = require_non_empty_string(item["query"], "query", f"trigger query #{index}")
        normalized_query = " ".join(query.split()).casefold()
        if normalized_query in seen_queries:
            raise ValueError(f"trigger query #{index}: duplicate query")
        seen_queries.add(normalized_query)

        should_trigger = item["should_trigger"]
        if not isinstance(should_trigger, bool):
            raise ValueError(f"trigger query #{index}: `should_trigger` must be boolean")
        if should_trigger:
            positives += 1
        else:
            negatives += 1

    if positives == 0 or negatives == 0:
        raise ValueError("trigger queries must include both positive and negative examples")


def validate_evals() -> None:
    load_json(EVALS / "schema.json")
    validate_trigger_queries()
    data = load_json(EVALS / "evals.json")

    if not isinstance(data, dict):
        raise ValueError("evals/evals.json must be a JSON object")
    if data.get("skill_name") != "oh-my-gh-writing":
        raise ValueError("evals/evals.json: `skill_name` must be `oh-my-gh-writing`")

    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        raise ValueError("evals/evals.json: `evals` must be a non-empty array")

    seen_ids: set[str] = set()
    for index, item in enumerate(evals, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"eval #{index}: item must be an object")

        extra_fields = sorted(set(item) - ALLOWED_EVAL_FIELDS)
        if extra_fields:
            raise ValueError(
                f"eval #{index}: unsupported fields: {', '.join(extra_fields)}"
            )

        raw_eval_id = item.get("id", f"#{index}")
        eval_id = raw_eval_id if isinstance(raw_eval_id, str) else f"#{index}"
        missing = sorted(REQUIRED_FIELDS - item.keys())
        if missing:
            raise ValueError(f"{eval_id}: missing required fields: {', '.join(missing)}")
        eval_id = require_non_empty_string(item["id"], "id", eval_id)
        if eval_id in seen_ids:
            raise ValueError(f"{eval_id}: duplicate id")
        seen_ids.add(eval_id)

        require_non_empty_string(item["prompt"], "prompt", eval_id)
        require_non_empty_string(item["expected_output"], "expected_output", eval_id)

        output_type = require_non_empty_string(item["output_type"], "output_type", eval_id)
        if output_type not in OUTPUT_TYPES:
            raise ValueError(f"{eval_id}: unsupported output_type `{item['output_type']}`")

        expected_route = require_non_empty_string(
            item["expected_route"], "expected_route", eval_id
        )
        if expected_route.startswith("references/") and not (ROOT / expected_route).is_file():
            raise ValueError(f"{eval_id}: expected route not found: {expected_route}")

        risk_category = require_string_list(
            item["risk_category"], "risk_category", eval_id, non_empty=True
        )
        if len(set(risk_category)) != len(risk_category):
            raise ValueError(f"{eval_id}: `risk_category` must not contain duplicates")
        for category in risk_category:
            if category not in RISK_CATEGORIES:
                raise ValueError(f"{eval_id}: unsupported risk category `{category}`")

        require_string_list(item["assertions"], "assertions", eval_id, non_empty=True)
        for optional in ("must_contain", "must_not_contain"):
            if optional in item:
                require_string_list(item[optional], optional, eval_id, non_empty=False)

        expected_file = item.get("expected_file")
        if expected_file is None and (
            item.get("must_contain") or item.get("must_not_contain")
        ):
            raise ValueError(
                f"{eval_id}: containment checks require an `expected_file` fixture"
            )
        if expected_file is not None:
            expected_file = require_non_empty_string(expected_file, "expected_file", eval_id)
            expected_path = EVALS / expected_file
            if not expected_path.is_file():
                raise ValueError(f"{eval_id}: expected file not found: evals/{expected_file}")
            expected_text = expected_path.read_text(encoding="utf-8")
            for needle in item.get("must_contain", []):
                if needle not in expected_text:
                    raise ValueError(
                        f"{eval_id}: expected file missing required text: {needle!r}"
                    )
            for needle in item.get("must_not_contain", []):
                if needle in expected_text:
                    raise ValueError(
                        f"{eval_id}: expected file contains forbidden text: {needle!r}"
                    )


def main() -> int:
    try:
        validate_evals()
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("eval fixtures are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
