# VC Knowledge Skills Collection

A curated collection of **pure knowledge/methodology skills** for venture capital work. These skills contain frameworks, mental models, and structured approaches that work without any external API integrations -- just expert thinking you can feed to an AI agent.

| | |
|---|---|
| **Downloaded Skills** | 107 |
| **Stub Files** | 11 (Anthropic FS waitlist) |
| **Total Knowledge Skills** | 147 (in database) |
| **Categories** | 10 |
| **Last Download** | February 2026 |

---

## What Are Knowledge Skills?

Unlike MCP servers or connectors that require API keys and external services, knowledge skills are **self-contained methodology files**. They teach Claude how to apply specific frameworks:

- **Investment analysis** frameworks (Munger's Lattice, CEO evaluation, scenario analysis, startup analyst)
- **Financial modeling** approaches (3-statement models, DCF, comps, startup modeling, variance analysis)
- **Due diligence** processes (DD memos, legal risk assessment, contract review, NDA triage, compliance)
- **Market research** methodologies (TAM/SAM/SOM, competitive intelligence, sector analysis, battlecards)
- **Portfolio operations** playbooks (metrics tracking, hiring, roadmap management, CEO advisory)
- **GTM & sales** frameworks (playbooks, pipeline review, call prep, launch strategy)

---

## Browse by Workflow

Skills are organized into 10 workflow folders:

| Category | Skills | Description |
|----------|--------|-------------|
| [founder_toolkit/](founder_toolkit/) | 17 | Fundraising, GTM strategy, pricing, growth, startup validation |
| [portfolio_operations/](portfolio_operations/) | 14 | Supporting portfolio companies, CEO advisory, KPI dashboards |
| [financial_modeling/](financial_modeling/) | 13 | Valuation, forecasting, variance analysis, startup modeling |
| [market_research/](market_research/) | 13 | Market sizing, competitive landscapes, sector analysis |
| [investor_relations/](investor_relations/) | 13 | Board prep, pitch decks, investor updates |
| [due_diligence/](due_diligence/) | 11 | DD processes, legal risk, contract review, NDA triage |
| [gtm_sales/](gtm_sales/) | 11 | Go-to-market, sales playbooks, pipeline, launch strategy |
| [investment_analysis/](investment_analysis/) | 9 | Thesis development, scenario analysis, startup evaluation |
| [communications/](communications/) | 6 | Internal comms, content, data storytelling, meeting briefing |
| [sentiment_signals/](sentiment_signals/) | 0 | Market sentiment, signal tracking (database-only) |

Each skill lives in its own subfolder: `{category}/{skill_id}/SKILL.md`

### Feed to an AI Agent

Copy any SKILL.md into your Claude Code skills directory:

```bash
cp knowledge_skills/due_diligence/cybos-ddmemo/SKILL.md ~/.claude/skills/dd-memo/SKILL.md
```

---

## Source Tracking

All credit for the skills belongs to their original authors and maintainers. This project downloads and redistributes them for discoverability -- see each repo's license below.

Provenance for every downloaded file is tracked in `manifest.json` (repo, path, SHA256 hash, timestamp).

| Source Repo | License | Skills | Notes |
|-------------|---------|--------|-------|
| anthropics/skills | MIT | 1 | Internal comms + 4 example templates |
| anthropics/knowledge-work-plugins | Apache-2.0 | 17 | Finance(6), legal(6), sales(2), PM(2), marketing(1) |
| anthropics/claude-cookbooks | MIT | 1 | Creating Financial Models |
| sickn33/antigravity-awesome-skills | MIT | 14 | Copywriting, pricing, quant, startup modeling, etc. |
| openclaw/skills | MIT | 1 | Market environment analysis |
| rkiding/awesome-finance-skills | No license | 2 | AlphaEar sentiment + signal tracker |
| propane-ai/kits | Apache-2.0 | 35 | Founder(13), GTM(10), CX(4), Product(5), Marketing(2) |
| gerstep/cybos | No license | 5 | Research (w/ shared resources), DD Memo, GTD, Content, Summarize |
| tradermonty/claude-trading-skills | No license | 2 | Scenario analyzer, bubble detector |
| alirezarezvani/claude-skills | MIT | 2 | CEO Advisor, Financial Analyst toolkit |
| sundial-org/awesome-openclaw-skills | No license | 2 | Pre-mortem analyst, 88KB competitive intelligence playbook |
| evolsb/claude-legal-skill | MIT | 1 | CUAD-grounded contract review (41 risk categories) |
| luisschmitzheadline/VC-Skills.md | MIT | 1 | Bottom-up market sizing (TAM/SAM/SOM) with ARPC decomposition |

---

## Unavailable Skills

11 skills from **Anthropic's Claude for Financial Services** program are behind a waitlist. Stub files with descriptions are in [`unavailable/`](unavailable/):

| Skill | Category |
|-------|----------|
| 3-Statement Financial Modeling | Financial Modeling |
| Comps Analysis | Financial Modeling |
| Competitive Landscape Analysis | Market Research |
| DCF Modeling | Financial Modeling |
| Due Diligence Data Pack | Due Diligence |
| Earnings Analysis | Investment Analysis |
| Initiating Coverage Research | Investment Analysis |
| Investment Banking Pitch Deck | Investor Relations |
| Presentation Quality Checker | Communications |
| Company Profile/Strip Creator | Investment Analysis |
| Creating Financial Models | Financial Modeling |

---

## Refreshing Downloads

To check for updates or re-download all skills:

```bash
# Show what would be downloaded
python3 download_skills.py --dry-run

# Download all (uses cache, skips existing)
python3 download_skills.py

# Force re-download everything
python3 download_skills.py --force

# Download a single skill
python3 download_skills.py --skill cybos-research --verbose
```

Set `GITHUB_TOKEN` env var for higher API rate limits (5000 vs 60 requests/hour).

The download script generates `manifest.json` with SHA256 hashes, timestamps, and download status for every file.

---

## License

These files are downloaded from open-source repositories with their own licenses. Check source repositories before redistribution.
