# Badge Catalog

Load this file only when the user asks for detailed badge design, exact shields.io URL patterns, or multi-ecosystem README badges. Basic badge rules live in `weapons.md`.

Shields.io base URL: `https://img.shields.io/`

## Static Badge Formula

```text
https://img.shields.io/badge/<label>-<message>-<color>
```

Use it inside Markdown image syntax:

```markdown
![Status](https://img.shields.io/badge/Status-Active-green)
```

- `label` is the left-side text; `message` is the right-side text; `color` is a named color or hex value without `#`.
- Encode spaces as `_` or `%20`; escape literal `-` as `--` and literal `_` as `__`.
- Add `?style=flat-square&logo=python&logoColor=white` only when the style or logo helps readers identify a real technology or status.

Use copy-paste examples as patterns only. Replace every placeholder with real repository, package, workflow, service, or account evidence. Do not keep example package names such as `react` or `django` unless the target project actually is that package.

## Common Copy-Paste Badge Recipes

Use these when the target project has the matching evidence.

| Intent | Markdown pattern | Evidence required |
|--------|------------------|-------------------|
| License | `[![License](https://img.shields.io/github/license/<user>/<repo>)](LICENSE)` | Public license file or GitHub license detection |
| Build status | `[![Build Status](https://img.shields.io/github/actions/workflow/status/<user>/<repo>/<workflow-name>.yml?branch=main)](https://github.com/<user>/<repo>/actions/workflows/<workflow-name>.yml)` | Existing GitHub Actions workflow file |
| npm version | `[![npm](https://img.shields.io/npm/v/<package>)](https://www.npmjs.com/package/<package>)` | Published npm package |
| npm monthly downloads | `[![npm downloads](https://img.shields.io/npm/dm/<package>)](https://www.npmjs.com/package/<package>)` | Published npm package |
| PyPI version | `[![PyPI](https://img.shields.io/pypi/v/<package>)](https://pypi.org/project/<package>/)` | Published PyPI package |
| Python versions | `[![Python versions](https://img.shields.io/pypi/pyversions/<package>)](https://pypi.org/project/<package>/)` | Published PyPI package metadata |
| GitHub stars | `[![GitHub stars](https://img.shields.io/github/stars/<user>/<repo>?style=social)](https://github.com/<user>/<repo>/stargazers)` | Public GitHub repository |
| GitHub forks | `[![GitHub forks](https://img.shields.io/github/forks/<user>/<repo>?style=social)](https://github.com/<user>/<repo>/forks)` | Public GitHub repository |
| Last commit | `[![Last commit](https://img.shields.io/github/last-commit/<user>/<repo>)](https://github.com/<user>/<repo>/commits)` | Public GitHub repository |
| Codecov | `[![Codecov](https://img.shields.io/codecov/c/github/<user>/<repo>)](https://codecov.io/gh/<user>/<repo>)` | Codecov project exists |
| PRs welcome | `[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)` | Project actually accepts outside PRs or has contribution guidance |

Rules:

- Prefer repository-aware endpoints such as `/github/license/user/repo` over hard-coded static values when possible.
- Link each badge to a useful destination: workflow, registry package, license, stargazers, coverage report, or contributing guide.
- Omit package/download/coverage badges when the package or service does not exist yet.
- Do not show both a registry license badge and a GitHub license badge unless they communicate different useful facts.

## Optional / Special Badge Recipes

Use these sparingly. They are useful for community, style, funding, or dynamic data, but should not be default README clutter.

| Intent | Markdown pattern | Evidence required |
|--------|------------------|-------------------|
| Visitor count | `[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F<user>%2F<repo>&count_bg=%2379C83D&title_bg=%23555555&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)` | User explicitly wants third-party visitor tracking |
| Discord | `[![Discord](https://img.shields.io/discord/<server-id>?color=7289da&label=Discord&logo=discord&logoColor=ffffff)](<discord-invite-or-community-url>)` | Real Discord server id and public invite/community link |
| Code style: Black | `[![Code style: black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)` | Project uses Black |
| Code style: Prettier | `[![Code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4)](https://prettier.io/)` | Project uses Prettier |
| WakaTime | `[![WakaTime](https://wakatime.com/badge/user/<user-uuid>/project/<project-id>.svg)](https://wakatime.com/badge/user/<user-uuid>/project/<project-id>)` | Public WakaTime badge ids provided |
| GitHub Sponsors | `[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/<user>)` | GitHub Sponsors profile exists |
| Ko-fi | `[![Ko-fi](https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=ko-fi&logoColor=black)](https://ko-fi.com/<user>)` | Ko-fi profile exists |
| Netlify deploy status | `[![Netlify Status](https://api.netlify.com/api/v1/badges/<site-id>/deploy-status)](https://app.netlify.com/sites/<site-name>/deploys)` | Netlify site id and deploy page |
| Vercel deploy status | `[![Vercel](https://therealsujitk-vercel-badge.vercel.app/?app=<vercel-app-name>)](https://vercel.com/<team-or-user>/<vercel-app-name>)` | Vercel project exists; third-party badge renders |
| Dynamic JSON | `[![Dynamic JSON](https://img.shields.io/badge/dynamic/json?url=<encoded-api-url>&query=%24.status&label=System%20Status&color=blue)](<status-page-or-api-doc>)` | Public JSON endpoint and verified JSONPath query |
| Made with Python | `[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f?logo=python&logoColor=white)](https://www.python.org/)` | Python is a primary project language/runtime |
| Made with love | `[![Made with love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red)](#)` | User explicitly wants a decorative badge |
| X/Twitter follow | `[![X Follow](https://img.shields.io/twitter/follow/<handle>?style=social)](https://x.com/<handle>)` | Real public account handle |
| Custom static style | `[![Architecture](https://img.shields.io/badge/Architecture-<message>-000000?style=for-the-badge&logo=markdown)](<docs-or-architecture-link>)` | Real project concept and useful destination |

Special badge rules:

- Visitor counters and social/funding badges are opt-in because they add tracking, promotion, or personal-account assumptions.
- Third-party deployment badges must render on GitHub. If a Vercel or visitor-count image fails, omit it or use a normal link.
- `Dynamic JSON` badges require a stable public API, URL-encoded endpoint, and verified query. Do not expose private tokens or internal URLs.
- Decorative badges such as `Made with love` should not displace status, version, license, install, or docs badges.

## Shields.io Styling Notes

Useful query parameters:

| Option | Example |
|--------|---------|
| Style | `?style=flat`, `?style=flat-square`, `?style=for-the-badge`, `?style=social` |
| Logo | `&logo=python&logoColor=white` |
| Label override | `?label=CI` or `&label=System%20Status` |
| Color | `?color=blue` or `&color=0f766e` |
| Label color | `&labelColor=111827` |

Encoding reminders:

- Spaces become `%20` or `_` in the static badge path.
- Literal underscores become `__` in the static badge path.
- Literal dashes become `--` in the static badge path.
- Use simple-icons slugs for `logo=` when available.

## GitHub

Prefix: `/github/`

| Badge | URL pattern |
|-------|----------|
| License | `/github/license/user/repo` |
| Stars | `/github/stars/user/repo` |
| Forks | `/github/forks/user/repo` |
| Watchers | `/github/watchers/user/repo` |
| Issues total | `/github/issues/user/repo` |
| Open Issues raw | `/github/issues-raw/user/repo` |
| Closed Issues | `/github/closed-issues/user/repo` |
| PRs total | `/github/issues-pr/user/repo` |
| Open PRs raw | `/github/issues-pr-raw/user/repo` |
| Merged PRs | `/github/merged-prs/user/repo` |
| Closed PRs | `/github/closed-prs/user/repo` |
| Discussions | `/github/discussions/user/repo` |
| Last Commit | `/github/last-commit/user/repo` |
| Commit Activity monthly | `/github/commit-activity/m/user/repo` |
| Commit Activity yearly | `/github/commit-activity/y/user/repo` |
| Latest Release | `/github/release/user/repo` |
| Release Version | `/github/v/release/user/repo` |
| Release Date | `/github/release-date/user/repo` |
| Latest Tag | `/github/v/tag/user/repo` |
| Tag | `/github/tag/user/repo` |
| Contributors | `/github/contributors/user/repo` |
| Downloads total | `/github/downloads/user/repo/total` |
| Downloads release | `/github/downloads/user/repo/tag` |
| Workflow Status | `/github/actions/workflow/status/user/repo/workflow.yml` |
| Checks Status | `/github/checks-status/user/repo/commit-sha` |
| Repo Size | `/github/repo-size/user/repo` |
| Code Size | `/github/languages/code-size/user/repo` |
| Top Language | `/github/languages/top/user/repo` |
| Language Count | `/github/languages/count/user/repo` |
| Directory File Count | `/github/directory-file-count/user/repo` |
| Deployments | `/github/deployments/user/repo/env` |
| Milestones | `/github/milestones/user/repo` |
| Hacktoberfest | `/github/hacktoberfest/year/user/repo` |
| GitHub Sponsors | `/github/sponsors/user` |
| Followers user | `/github/followers/user` |

## Package Registry

| Ecosystem | Badge | URL pattern |
|-----------|-------|----------|
| npm | Version | `/npm/v/package` |
| npm | License | `/npm/l/package` |
| npm | Type Definitions | `/npm/types/package` |
| npm | Unpacked Size | `/npm/unpacked-size/package` |
| npm | Monthly Downloads | `/npm/dm/package` |
| npm | Weekly Downloads | `/npm/dw/package` |
| npm | Daily Downloads | `/npm/dd/package` |
| npm | Yearly Downloads | `/npm/dy/package` |
| npm | Total Downloads | `/npm/dt/package` |
| PyPI | Version | `/pypi/v/package` |
| PyPI | License | `/pypi/l/package` |
| PyPI | Python Versions | `/pypi/pyversions/package` |
| PyPI | Wheel | `/pypi/wheel/package` |
| PyPI | Implementation | `/pypi/implementation/package` |
| PyPI | Format | `/pypi/format/package` |
| PyPI | Status | `/pypi/status/package` |
| PyPI | Monthly Downloads | `/pypi/dm/package` |
| PyPI | Weekly Downloads | `/pypi/dw/package` |
| PyPI | Daily Downloads | `/pypi/dd/package` |
| Docker | Version | `/docker/v/user/repo` |
| Docker | Image Size | `/docker/size/user/repo` |
| Docker | Pulls | `/docker/pulls/user/repo` |
| Docker | Stars | `/docker/stars/user/repo` |
| Docker | Automated Build | `/docker/automated/user/repo` |
| Crates.io | Version | `/crates/v/crate` |
| Crates.io | License | `/crates/l/crate` |
| Crates.io | Downloads | `/crates/d/crate` |
| Crates.io | Downloads version | `/crates/dv/crate` |
| Crates.io | Crate Size | `/crates/size/crate` |
| RubyGems | Version | `/gem/v/gem` |
| RubyGems | Total Downloads | `/gem/dt/gem` |
| RubyGems | Runtime Dependencies | `/gem/rd/gem` |
| NuGet | Version | `/nuget/v/package` |
| NuGet | Total Downloads | `/nuget/dt/package` |
| NuGet | Weekly Downloads | `/nuget/dw/package` |
| Packagist | Version | `/packagist/v/user/package` |
| Packagist | License | `/packagist/l/user/package` |
| Packagist | PHP Version | `/packagist/php-version/user/package` |
| Packagist | Monthly Downloads | `/packagist/dm/user/package` |
| Packagist | Daily Downloads | `/packagist/dd/user/package` |
| Packagist | Total Downloads | `/packagist/dt/user/package` |
| Hex.pm | Version | `/hexpm/v/package` |
| Hex.pm | License | `/hexpm/l/package` |
| Hex.pm | Total Downloads | `/hexpm/dt/package` |
| Maven Central | Version | `/maven-central/v/group/artifact` |
| Maven Central | Version with label | `/maven-central/v/group/artifact?label=Maven` |

## Distribution / Marketplace

| Ecosystem | Badge | URL pattern |
|-----------|-------|----------|
| Visual Studio Marketplace | Version | `/visual-studio-marketplace/v/extension` |
| Visual Studio Marketplace | Installs | `/visual-studio-marketplace/i/extension` |
| Visual Studio Marketplace | Downloads | `/visual-studio-marketplace/d/extension` |
| Visual Studio Marketplace | Rating | `/visual-studio-marketplace/stars/extension` |
| Visual Studio Marketplace | Reviews | `/visual-studio-marketplace/r/extension` |
| JetBrains Plugin | Version | `/jetbrains/plugin/v/pluginId` |
| JetBrains Plugin | Downloads | `/jetbrains/plugin/d/pluginId` |
| JetBrains Plugin | Rating | `/jetbrains/plugin/rating/pluginId` |
| JetBrains Plugin | Reviews | `/jetbrains/plugin/reviews/pluginId` |
| Homebrew | Version | `/homebrew/v/formula` |
| Homebrew | Cask Version | `/homebrew/cask/v/cask` |
| Homebrew | Downloads | `/homebrew/d/formula` |
| Chocolatey | Version | `/chocolatey/v/package` |
| Chocolatey | Downloads | `/chocolatey/d/package` |
| Scoop | Version | `/scoop/v/package` |
| Snapcraft | Version | `/snap/v/package` |
| Snapcraft | Downloads | `/snap/d/package` |
| AUR | Version | `/aur/version/package` |
| AUR | License | `/aur/license/package` |
| AUR | Maintainer | `/aur/maintainer/package` |
| AUR | Votes | `/aur/votes/package` |
| AUR | Popularity | `/aur/popularity/package` |
| AUR | Last Modified | `/aur/last-modified/package` |
| winget | Version | `/winget/v/package` |
| winget | Status | `/winget/s/package` |

## CI / Coverage / Quality

| Badge | URL pattern |
|-------|----------|
| GitLab Pipeline Status | `/gitlab/pipeline/user/repo` |
| GitLab Coverage | `/gitlab/coverage/user/repo` |
| GitLab Latest Release | `/gitlab/v/release/user/repo` |
| GitLab Last Commit | `/gitlab/last-commit/user/repo` |
| GitLab License | `/gitlab/license/user/repo` |
| GitLab Contributors | `/gitlab/contributors/user/repo` |
| GitLab Top Language | `/gitlab/languages/top/user/repo` |
| GitLab Stars | `/gitlab/stars/user/repo` |
| GitLab Forks | `/gitlab/forks/user/repo` |
| CircleCI | `/circleci/build/user/repo/branch` |
| Travis CI .com | `/travis/.com/user/repo` |
| Travis CI branch | `/travis/.com/user/repo/branch` |
| Jenkins Build | `/jenkins/s/https/jenkins.example.com/job/job` |
| Jenkins Tests | `/jenkins/tests/https/jenkins.example.com/job/job` |
| Jenkins Coverage | `/jenkins/coverage/https/jenkins.example.com/job/job` |
| AppVeyor Build | `/appveyor/build/user/repo` |
| AppVeyor Tests | `/appveyor/tests/user/repo` |
| Codecov | `/codecov/c/user/repo` |
| Codecov branch | `/codecov/c/user/repo/branch` |
| Coveralls | `/coveralls/user/repo` |
| Sonar Quality Gate | `/sonar/quality_gate/project` |
| Sonar Coverage | `/sonar/coverage/project` |
| Sonar Violations | `/sonar/violations/project` |
| Sonar Tech Debt | `/sonar/tech_debt/project` |
| Sonar Rating | `/sonar/rating/project` |
| Sonar Alert Status | `/sonar/alert_status/project` |
| Codacy Grade | `/codacy/grade/projectId` |
| Codacy Coverage | `/codacy/coverage/projectId` |
| Code Climate Maintainability | `/codeclimate/maintainability/user/repo` |
| Code Climate Coverage | `/codeclimate/coverage/user/repo` |
| Snyk Vulnerabilities | `/snyk/vulnerabilities/github/user/repo` |
| Dependabot | `/dependabot/user/repo` |
| LGTM Alerts | `/lgtm/alerts/g/user/repo` |
| LGTM Grade | `/lgtm/grade/python/g/user/repo` |

## Community / Website / Other

| Badge | URL pattern |
|-------|----------|
| Discord | `/discord/serverId` |
| Matrix | `/matrix/room` |
| Slack | `/slack/team/serverId` |
| Gitter | `/gitter/room/user/repo` |
| Zulip | `/zulip/topics/stream` |
| Bluesky Followers | `/bluesky/followers/user` |
| Reddit Subscribers | `/reddit/subscribers/subreddit` |
| Twitch Status | `/twitch/status/user` |
| Twitch Views | `/twitch/views/user` |
| Twitch Followers | `/twitch/followers/user` |
| YouTube Channel Views | `/youtube/channel/views/channelId` |
| YouTube Subscribers | `/youtube/channel/subscribers/channelId` |
| YouTube Video Views | `/youtube/v/videoId` |
| YouTube Likes | `/youtube/likes/videoId` |
| YouTube Comments | `/youtube/comments/videoId` |
| Twitter/X Followers | `/twitter/followers/user` |
| GitHub Sponsors | `/github/sponsors/user` |
| Open Collective Backers | `/opencollective/backers/collective` |
| Open Collective Sponsors | `/opencollective/sponsors/collective` |
| Liberapay Receives | `/liberapay/receives/username` |
| Liberapay Patrons | `/liberapay/patrons/username` |
| Liberapay Goal | `/liberapay/goal/username` |
| Website Status | `/website?url=https://example.com` |
| Website Up/Down | `/website-up-down/https/example.com?label=Website` |
| Maintenance | `/maintenance/yes/year` |
| Chromium HSTS Preload | `/hsts/preload/domain` |
| Go Module | `/go/mod/module` |
| Keybase PGP | `/keybase/pgp/username` |
| Keybase BTC | `/keybase/btc/username` |
| Eclipse Marketplace Version | `/eclipse-marketplace/v/package` |
| Eclipse Marketplace Downloads | `/eclipse-marketplace/d/package` |
| Eclipse Marketplace Rating | `/eclipse-marketplace/rating/package` |
| F-Droid | `/f-droid/v/package` |
| CTAN Version | `/ctan/v/package` |
| CTAN License | `/ctan/l/package` |
| W3C Validation | `/w3c-validation/default` |
| Libraries.io | `/librariesio/release/npm/package` |
| Sourcegraph | `/sourcegraph/rr/user/repo` |

## Special GitHub Trend / Growth Visuals

These are not normal shields.io GitHub endpoints. Use them only when the source exists and the URL is verified.

| Service | Use | Markdown pattern | Evidence required |
|---------|-----|------------------|-------------------|
| Trendshift | GitHub trending history / repo engagement badge | `[![Trendshift](https://trendshift.io/api/badge/repositories/<trendshift-repo-id>)](https://trendshift.io/repositories/<trendshift-repo-id>)` | A real Trendshift repository page or user-provided Trendshift repo id |
| Star History | Star growth chart | `[![Star History Chart](https://api.star-history.com/svg?repos=user/repo&type=Date)](https://www.star-history.com/#user/repo&Date)` | Real public GitHub `user/repo` |

Rules:

- Do not invent a Trendshift repository id from `owner/repo`; open or search Trendshift first, or ask the user for the id.
- Do not call a repository "Trending" unless a Trendshift page, GitHub Trending page, user input, or another verifiable source supports it.
- Prefer standard GitHub stars/forks/release badges when no trend source is verified.
- If the external image fails, returns HTML, or does not render on GitHub, omit the badge and link the source page instead.

## External Source

[pudding0503/github-badge-collection](https://github.com/pudding0503/github-badge-collection) is a useful supporting catalog for GitHub visual assets and badge ideas. Treat it as inspiration and verify each concrete badge or asset before use.
