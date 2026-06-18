<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="شعار oh-my-gh-writing" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Scenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · العربية · <a href="README.fr.md">Français</a> · <a href="README.pt.md">Português</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

**oh-my-gh-writing** حزمة مهارة كتابة لـ GitHub موجهة إلى AI Agents. تقوم بتوجيه مهام مثل Issues وPRs وReviews وCommits وREADME وCHANGELOG وRelease Notes وMigration Guides وRFCs وIssue Forms وPR Templates إلى معايير خاصة بكل سيناريو، لتساعد الوكيل على إنتاج مسودات Markdown أو YAML واضحة ومحددة بحدود أدلة صريحة.

ليست هذه الأداة مولد README ولا خدمة تكامل مع GitHub. إنها قاعدة قواعد Markdown قابلة للنقل: الأدوات التي تدعم Agent Skills يمكنها تحميلها مباشرة، والأدوات الأخرى يمكنها تحويل `SKILL.md` وملفات `reference/*.md` المناسبة إلى قواعد أو تعليمات أو قاعدة معرفة.

## لماذا oh-my-gh-writing؟

الكتابة الجيدة في GitHub لا تعني ملء Markdown فقط. الأصعب هو معرفة السيناريو الصحيح، والحقائق التي يجب التحقق منها، وما لا يجوز اختلاقه، وهل يمكن لصق الناتج في Issue أو PR أو Review أو README بدون تنظيف إضافي.

- **18 سيناريو كتابة لـ GitHub**: Issues وPRs وCode Review وCommit وREADME وCHANGELOG وRelease Notes وMigration Guide وRFC وIssue Form وPR Template وغيرها.
- **التوجيه قبل الكتابة**: يفرق بين Feature Request وEnhancement وDiscussion وFeature PR وBug Fix PR وRefactor PR.
- **تحميل تدريجي للمراجع**: يبقى `SKILL.md` خفيفا، وتقرأ المعايير التفصيلية عند الحاجة فقط.
- **حدود الأدلة**: لا يتم تخمين الإصدارات أو الأوامر أو CI أو التوافق أو releases أو أرقام issues/PRs.
- **مخرجات أنظف**: يتجنب المقدمات الحوارية، وكتل Markdown الخارجية، وعناوين الاختبار، وبقايا النسخ.
- **مراجع مفتوحة المصدر حقيقية**: يستند إلى GitHub Docs وConventional Commits وKeep a Changelog ومشاريع مثل React وKubernetes وTypeScript وNode.js وTailwind CSS.

## طرق الاستخدام

**كـ skill**: ضع هذا المستودع في مكان يستطيع الوكيل فيه تحميل مجلد يحتوي `SKILL.md` وقراءة `reference/` عند الحاجة.

**كقواعد**: إذا لم تكن أداتك تدعم هذا الشكل مباشرة، فحوّل جدول التوجيه في `SKILL.md` وملفات `reference/*.md` المناسبة إلى قواعد مشروع أو تعليمات مخصصة أو قاعدة معرفة.

| الأيقونة | Agent / Tool | الإعداد الموصى به | ملاحظات / وثائق |
|---------|--------------|-------------------|-----------------|
| <a href="https://developers.openai.com/codex/skills"><img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="24" height="24" alt="OpenAI"></a> | [Codex](https://developers.openai.com/codex/skills) | استنساخ إلى `$HOME/.agents/skills/oh-my-gh-writing` أو `.agents/skills/oh-my-gh-writing` | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <a href="https://code.claude.com/docs/en/skills"><img src="https://www.google.com/s2/favicons?domain=claude.ai&sz=64" width="24" height="24" alt="Claude"></a> | [Claude Code](https://code.claude.com/docs/en/skills) | استنساخ أو symlink إلى `~/.claude/skills/oh-my-gh-writing` أو `.claude/skills/oh-my-gh-writing` | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <a href="https://geminicli.com/docs/cli/skills/"><img src="https://www.google.com/s2/favicons?domain=geminicli.com&sz=64" width="24" height="24" alt="Gemini CLI"></a> | [Gemini CLI](https://geminicli.com/docs/cli/skills/) | الوثائق تذكر `~/.gemini/skills/` و`~/.agents/skills/` و`gemini skills install` | تحقق من [الوثائق الرسمية](https://geminicli.com/docs/cli/skills/) الحالية |
| <a href="https://antigravity.google/"><img src="https://www.google.com/s2/favicons?domain=antigravity.google&sz=64" width="24" height="24" alt="Antigravity"></a> | [Antigravity CLI](https://antigravity.google/) | تحقق من مسار دمج skills / rules في الوثائق الحالية | [Google Antigravity](https://antigravity.google/) |
| <a href="https://hermes-agent.nousresearch.com/docs/guides/work-with-skills"><img src="https://www.google.com/s2/favicons?domain=hermes-agent.nousresearch.com&sz=64" width="24" height="24" alt="Hermes"></a> | [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | ضعه في `~/.hermes/skills/<category>/oh-my-gh-writing` | تثبيت HTTP لملف واحد مناسب فقط لـ `SKILL.md`؛ احتفظ بـ `reference/`. راجع [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <a href="https://cursor.com/docs"><img src="https://www.google.com/s2/favicons?domain=cursor.com&sz=64" width="24" height="24" alt="Cursor"></a> | [Cursor](https://cursor.com/docs) | حوّل الموجه والقواعد المطلوبة إلى project rules أو knowledge base | راجع [Cursor Docs](https://cursor.com/docs) |
| <a href="https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions"><img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="24" height="24" alt="GitHub"></a> | [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | حوّلها إلى `.github/copilot-instructions.md` أو `.github/instructions/*.instructions.md` أو بنية skill | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <a href="https://docs.continue.dev/customize/rules"><img src="https://www.google.com/s2/favicons?domain=continue.dev&sz=64" width="24" height="24" alt="Continue"></a> | [Continue](https://docs.continue.dev/customize/rules) | حوّلها إلى `.continue/rules/*.md`؛ الفصل حسب السيناريو أكثر ثباتا | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <a href="https://docs.windsurf.com"><img src="https://www.google.com/s2/favicons?domain=windsurf.com&sz=64" width="24" height="24" alt="Windsurf"></a> | [Windsurf / Devin Desktop](https://docs.windsurf.com) | الوثائق الحالية تذكر memories وrules للتخصيص | تحقق من الطريقة الحالية في [Windsurf / Devin Docs](https://docs.windsurf.com) |

## البدء السريع

```bash
# Codex
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

روابط محلية للتطوير:

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

أمثلة:

```text
اكتب README لهذا المستودع.
حوّل هذا bug report إلى GitHub Issue.
اكتب وصف PR من diff الحالي.
راجع هذا PR وصنف الملاحظات إلى blocking / major / minor / nit.
```

## السيناريوهات

| # | الفئة | السيناريو | وقت الاستخدام |
|---|------|-----------|---------------|
| 1 | Issue | Bug Report | الإبلاغ عن عيب قابل لإعادة الإنتاج |
| 2 | Issue | Feature Request | اقتراح ميزة أو API جديد |
| 3 | Issue | Enhancement | تحسين سلوك موجود |
| 4 | Issue | Discussion | فتح نقاش مجتمعي |
| 5 | PR | Feature PR | وصف PR لميزة جديدة |
| 6 | PR | Bug Fix PR | وصف PR لإصلاح bug |
| 7 | PR | Refactor PR | وصف refactor بدون تغيير سلوكي |
| 8 | PR | Documentation PR | وصف تغييرات توثيق فقط |
| 9 | Review | Code Review | مراجعة تغييرات الكود |
| 10 | Commit | Standard Commit | كتابة رسائل commit |
| 11 | Docs | README | إنشاء أو تعديل صفحة المشروع |
| 12 | Docs | CONTRIBUTING | إنشاء إرشادات المساهمة |
| 13 | Docs | CHANGELOG | كتابة تاريخ الإصدارات |
| 14 | Release | Release Notes | كتابة إعلان إصدار |
| 15 | Release | Migration Guide | شرح خطوات الترقية |
| 16 | Design | RFC | اقتراح تصميم |
| 17 | Templates | Issue Form YAML | إنشاء GitHub Issue Forms |
| 18 | Templates | PR Template | إنشاء Pull Request templates |

لكل سيناريو ملف قياسي في `reference/`. الفهرس الكامل في [`INDEX.md`](INDEX.md).

## بنية المستودع

```text
oh-my-gh-writing/
├── README.md
├── README.*.md
├── README_Example.md
├── SKILL.md
├── INDEX.md
├── CONTRIBUTING.md
├── LICENSE
├── assets/
│   └── oh-my-gh-writing-logo.png
└── reference/
    ├── *.md
    ├── readme.md
    ├── shared-principles.md
    ├── output-validation.md
    ├── source-catalog.md
    ├── weapons.md
    ├── emoji-guide.md
    └── badge-catalog.md
```

## المساهمة

نرحب بالمساهمات في قواعد السيناريوهات، ومصادر المراجع، وقواعد التحقق من المخرجات، وأدوات Markdown الصغيرة. بالنسبة للأمثلة أو حالات الاختبار، يرجى أولا وصف المصدر والسيناريو وهدف الاختبار وحدود الترخيص أو الخصوصية في Issue أو Discussion.

أبق `SKILL.md` خفيفا وضع التفاصيل في ملف `reference/*.md` المناسب. راجع [`CONTRIBUTING.md`](CONTRIBUTING.md).

## المصادر

تستند القواعد إلى [GitHub Docs](https://docs.github.com/en)، و[Conventional Commits](https://www.conventionalcommits.org/)، و[Keep a Changelog](https://keepachangelog.com/)، و[Google Engineering Practices](https://google.github.io/eng-practices/review/) ومشاريع ناضجة مثل Angular وKubernetes وReact وTypeScript وVS Code وNode.js وTailwind CSS. راجع [`reference/source-catalog.md`](reference/source-catalog.md).

## الترخيص

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
