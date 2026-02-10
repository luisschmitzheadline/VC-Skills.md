# VC Skills

Claude Code can be extended with skills, MCP servers, and connectors -- but they're scattered across dozens of GitHub repos, marketplaces, and registries. This repo does two things:

1. **Indexes 346 VC-relevant skills** in a searchable [dashboard](https://luisschmitzheadline.github.io/VC-Skills.md/dashboard/) -- so you can discover what's out there
2. **Ships 84 ready-to-use methodology skills** -- frameworks for financial modeling, due diligence, market research, and more that work without any API keys or setup

## Quick Start

**[Browse the Dashboard](https://luisschmitzheadline.github.io/VC-Skills.md/dashboard/)** -- search, filter, and explore all 346 skills. Use the "Knowledge Only" toggle to see the 117 that need no integrations.

**Use a skill** -- copy any downloaded skill into your Claude Code skills directory:

```bash
cp knowledge_skills/due_diligence/cybos-ddmemo/SKILL.md ~/.claude/skills/dd-memo/SKILL.md
```

## Ready-to-Use Skills

The [`knowledge_skills/`](knowledge_skills/) directory contains 84 downloaded methodology skills -- pure frameworks and mental models, no API keys needed. Browse by workflow:

| Workflow | Skills |
|----------|--------|
| [Financial Modeling](knowledge_skills/financial_modeling/) | 14 |
| [Portfolio Operations](knowledge_skills/portfolio_operations/) | 15 |
| [Market Research](knowledge_skills/market_research/) | 13 |
| [GTM & Sales](knowledge_skills/gtm_sales/) | 12 |
| [Due Diligence](knowledge_skills/due_diligence/) | 10 |
| [Communications](knowledge_skills/communications/) | 8 |
| [Investor Relations](knowledge_skills/investor_relations/) | 6 |
| [Investment Analysis](knowledge_skills/investment_analysis/) | 4 |
| [Sentiment & Signals](knowledge_skills/sentiment_signals/) | 2 |

See the full [`knowledge_skills/` README](knowledge_skills/) for source tracking, download scripts, and the 11 Anthropic Financial Services stubs behind a waitlist.

## Repository Structure

```
database/                    # Skills database + dashboard
  vc_skills_database.json    #   Source of truth (346 skills)
  index.html                 #   Interactive dashboard
  sources.html               #   Sources & attribution page
  build.py                   #   Regenerates CSV, dashboard, workflow docs
knowledge_skills/            # Downloaded skill content (84 skills)
  {category}/{skill_id}/     #   SKILL.md + supporting files
  unavailable/               #   11 Anthropic FS stubs (waitlist)
  download_skills.py         #   Download/refresh script
  manifest.json              #   Provenance tracking (repo, hash, timestamp)
```
