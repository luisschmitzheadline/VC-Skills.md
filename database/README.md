# VC Skills Database

A comprehensive database of **346 VC-relevant skills**, MCP servers, and connectors for venture capital workflows.

| | |
|---|---|
| **Skills** | 346 |
| **Version** | 1.5.0 |
| **Updated** | February 2026 |

---

## Interactive Dashboard

**[Open the Dashboard](index.html)** - Browse and filter all 346 skills with:
- Full-text search across names, descriptions, and tags
- Filter by workflow (Deal Sourcing, Due Diligence, Portfolio Support, etc.)
- Filter by type (MCP Server, Skill, Connector)
- Filter by Knowledge Only (pure methodology skills, no integrations needed)
- Click cards to expand details
- Direct links to source repositories

The dashboard is a self-contained HTML file that works offline - share it directly or host anywhere.

---

## Repository Structure

```
database/
├── index.html                    # Interactive dashboard (browse & filter)
├── sources.html                  # Sources & attribution page
├── vc_skills_database.json       # Source data (346 skills, structured)
├── vc_skills_database.csv        # Spreadsheet export (Excel/Google Sheets)
├── build.py                      # Build script (regenerates all exports)
├── README.md                     # This documentation
├── SOURCES.md                    # Data sources & crawl history
├── ../LICENSE                    # MIT License (repo root)
├── by_workflow/                  # Skills organized by VC workflow
│   ├── deal_sourcing.md
│   ├── due_diligence.md
│   ├── portfolio_support.md
│   ├── fund_operations.md
│   ├── data_infrastructure.md
│   └── automation.md
└── ../knowledge_skills/          # Downloaded knowledge skill content
    ├── download_skills.py        # Download script
    ├── manifest.json             # Download manifest with hashes
    ├── investment_analysis/      # 4 skills
    ├── financial_modeling/       # 14 skills
    ├── market_research/          # 12 skills
    ├── due_diligence/            # 10 skills
    ├── portfolio_operations/     # 15 skills
    ├── investor_relations/       # 6 skills
    ├── gtm_sales/                # 12 skills
    ├── communications/           # 8 skills
    ├── sentiment_signals/        # 2 skills
    └── unavailable/              # Stubs for Anthropic FS skills
```

---

## Quick Start

### Option 1: Interactive Dashboard (Recommended)
Open `index.html` in any browser to search and filter skills interactively.

### Option 2: Spreadsheet
Open `vc_skills_database.csv` in Excel or Google Sheets for sorting and filtering.

### Option 3: Programmatic Access
```python
import json
with open('vc_skills_database.json') as f:
    data = json.load(f)
    skills = data['skills']

# Filter by workflow
deal_sourcing = [s for s in skills if 'deal_sourcing' in s['vc_workflows']]
```

---

## Skills Overview

### By Type

| Type | Count | Description |
|------|-------|-------------|
| MCP Server | 187 | Model Context Protocol servers for Claude |
| Skill | 147 | Claude Code skills (install to ~/.claude/skills/) |
| Connector | 11 | Official Anthropic connectors |

### By VC Relevance Score

Each skill has a 1-5 VC relevance score based on how useful it is for venture capital work:

| Score | Label | Criteria | Count |
|-------|-------|----------|-------|
| ★★★★★ | Essential VC Tool | Built specifically for VC/PE workflows | 34 |
| ★★★★ | Highly Relevant | Extremely useful for VC work | 55 |
| ★★★ | Moderately Relevant | Applicable to VC workflows | 90 |
| ★★ | Somewhat Relevant | Useful in specific cases | 95 |
| ★ | Low Relevance | General tool | 71 |

**Scoring factors:**
- VC-specific keywords (pitchbook, crunchbase, due diligence, etc.)
- Core VC workflows (deal sourcing, due diligence)
- Core VC tasks (financial analysis, company identification, etc.)
- Official Anthropic connectors
- Verified/official status
- Source quality (financial data providers, etc.)

### Knowledge Skills

117 skills are **pure knowledge/methodology skills** that work without any external APIs or integrations. These contain frameworks, mental models, and structured approaches:

| Category | Skills | Examples |
|----------|--------|----------|
| Financial Modeling | 22 | 3-statement models, DCF, comps, variance analysis, startup modeling |
| Market Research | 20 | Competitive intelligence, sector analysis, TAM/SAM/SOM, battlecards |
| Portfolio Operations | 16 | Metrics tracking, churn prediction, roadmap management, CEO advisory |
| Due Diligence | 13 | DD memos, legal risk assessment, contract review, NDA triage, compliance |
| Investment Analysis | 13 | Earnings analysis, startup analyst, scenario analysis, bubble detection |
| GTM & Sales | 13 | Sales playbooks, pipeline review, call prep, launch strategy |
| Communications | 9 | Internal comms, copywriting, data storytelling, meeting briefing |
| Investor Relations | 7 | Board prep, pitch decks, investor updates |
| Sentiment & Signals | 4 | Market sentiment, signal tracking |

Use the **Knowledge Only** filter in the dashboard to browse just these skills. See [`knowledge_skills/README.md`](../knowledge_skills/README.md) for the full downloaded catalog.

### By Workflow

| Workflow | Count | Description |
|----------|-------|-------------|
| Due Diligence | 175 | Financial analysis, technical DD, market sizing, legal review |
| Portfolio Support | 147 | KPI tracking, board materials, competitor monitoring |
| Deal Sourcing | 95 | Thematic research, company identification, lead gen |
| Fund Operations | 54 | LP reporting, document generation, CRM |
| Data Infrastructure | 52 | Databases, scraping, enrichment, signals |
| Automation | 20 | Workflow orchestration, email, scheduling |

---

## VC Workflow Categories

### 1. Deal Sourcing & Flow
Finding and evaluating new investment opportunities.

**Key Tasks:** thematic_research, market_mapping, company_identification, lead_generation, competitive_landscape, trend_analysis

**Top Skills:**
- **Deep Research Skill** - Multi-source research with verification
- **PitchBook Connector** - 8.5M+ private companies
- **Octagon AI MCP** - 3M+ private companies, 500K+ funding deals (FREE)
- **Crunchbase Scraper (Apify)** - Free alternative to Crunchbase

### 2. Due Diligence
Evaluating investment opportunities.

**Key Tasks:** financial_analysis, market_sizing, technical_dd, management_research, legal_research, document_review

**Top Skills:**
- **Octagon AI MCP** - SEC filings, transcripts, financials (FREE)
- **Due Diligence Data Pack Skill** - Data room document processing
- **3-Statement Financial Modeling Skill** - Integrated financial models
- **Trail of Bits Skills** - Security code review

### 3. Portfolio Support
Supporting existing portfolio companies.

**Key Tasks:** kpi_tracking, fundraising_support, strategic_research, competitor_monitoring, board_materials

**Top Skills:**
- **Dashboard Creator Skill** - KPI dashboards with charts
- **Amplitude/Mixpanel MCP** - Product analytics
- **Chargebee MCP** - Subscription metrics
- **Timeline Creator Skill** - Roadmaps and Gantt charts

### 4. Fund Operations
Managing the fund itself.

**Key Tasks:** lp_reporting, lp_prospecting, lp_communication, document_generation, board_materials

**Top Skills:**
- **XLSX Skill** - Excel/financial modeling
- **IB Pitch Deck Skill** - Template-based presentations
- **Company Profile Creator Skill** - 1-2 page summaries
- **HubSpot MCP** - CRM management

### 5. Data Infrastructure
Building systems to support workflows.

**Key Tasks:** database_queries, company_data_enrichment, signal_generation, web_scraping

**Top Skills:**
- **PostgreSQL MCP** - Database queries
- **Apify MCP** - Web scraping (6000+ tools)
- **Firecrawl MCP** - Structured data extraction
- **Neo4j MCP** - Graph relationships

### 6. Automation & Productivity
Automating repetitive tasks.

**Key Tasks:** research_automation, document_generation, email_management, workflow_orchestration

**Top Skills:**
- **Zapier MCP** - 8000+ app integrations
- **Make MCP** - Workflow automation
- **Composio MCP** - Multi-tool integration

---

## Featured Collections

### Octagon AI Suite (FREE - Highly Recommended)

A comprehensive suite of specialized MCP servers for VC work:

| Server | Data Coverage | Primary Use |
|--------|--------------|-------------|
| Octagon AI MCP | 8000+ public, 3M+ private | SEC filings, earnings, financials |
| Octagon VC Agents | AI personas | Pitch feedback, DD simulations |
| Octagon Funding Data | 500K+ deals | Funding rounds, investor activity |
| Octagon Investors | Investor profiles | Portfolio analysis, co-investor research |
| Octagon 13F Holdings | Institutional filings | Hedge fund positions |
| Octagon Private Companies | 3M+ private | Private market research |
| Octagon Deep Research | Multi-source | Comprehensive research |

**Installation:** `npx octagon-mcp` (free API key from octagonai.co)

### Official Anthropic Connectors (Premium)

| Connector | Provider | Primary Use |
|-----------|----------|-------------|
| PitchBook | PitchBook | Private market data |
| S&P Capital IQ | S&P Global | Financial data |
| Daloopa | Daloopa | Financial extraction |
| Morningstar | Morningstar | Investment research |
| Aiera | Aiera | Earnings transcripts |
| Third Bridge | Third Bridge | Expert interviews |
| Chronograph | Chronograph | Portfolio monitoring |
| LSEG | Refinitiv | Market data |
| Moody's | Moody's | Credit analysis |

### Crypto/Web3 Investments
- **Web3 MCP (Strangelove)** - Multi-chain: Solana, ETH, Cardano, BTC
- **DexPaprika MCP** - 5M+ tokens across 20+ blockchains
- **Whale Tracker MCP** - Large holder movements
- **Heurist Mesh Agent** - Smart contract auditing

### Healthcare/Biotech
- **ClinicalTrials.gov MCP** - Search 400K+ clinical trials
- **BioMCP** - PubMed, ClinicalTrials.gov, MyVariant.info

### Real Estate/PropTech
- **Zillow MCP Server** - Property search, Zestimates, market trends
- **Real Estate Investment MCP** - ZHVI, rent indexes, forecasts

---

## Data Schema

Each skill entry contains:

```json
{
  "id": "skill-001",
  "name": "Skill Name",
  "source": "github.com/org/repo",
  "source_type": "github|anthropic_connector|mcp_registry|glama|pulsemcp|apify",
  "description": "What the skill does",
  "vc_workflows": ["deal_sourcing", "due_diligence"],
  "vc_tasks": ["thematic_research", "financial_analysis"],
  "skill_type": "skill|mcp_server|connector",
  "installation": "How to install",
  "official": true,
  "verified": true,
  "tags": ["tag1", "tag2"],
  "notes": "Additional context",
  "vc_relevance": 4,
  "requires_integration": false,
  "knowledge_category": "financial_modeling",
  "download_status": "downloaded"
}
```

---

## Installation Guide

### MCP Servers

**Via NPM:**
```bash
npm install @package/mcp-server
```

**Via GitHub:**
```bash
git clone https://github.com/org/mcp-server
cd mcp-server && npm install
```

**Configure in Claude Code** (`~/.claude/settings.json`):
```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["path/to/server/index.js"],
      "env": { "API_KEY": "your-key" }
    }
  }
}
```

### Claude Code Skills

```bash
cd ~/.claude/skills
git clone https://github.com/org/skill-name
# Restart Claude Code
```

### Anthropic Connectors

1. Go to Claude settings → "Connectors"
2. Enable desired connectors
3. Authenticate with service credentials

---

## Sources

This database was compiled from:

**MCP Registries:**
- PulseMCP, Glama, mcpservers.org
- registry.modelcontextprotocol.io, mcp-awesome.com

**GitHub Collections:**
- VoltAgent/awesome-agent-skills
- punkpeye/awesome-mcp-servers
- wong2/awesome-mcp-servers
- travisvn/awesome-claude-skills
- mhattingpete/claude-skills-marketplace

**Official Sources:**
- Anthropic connectors
- modelcontextprotocol/servers
- Claude Financial Services Skills

**Specialized:**
- Octagon AI suite (7 MCPs)
- Apify marketplace (Crunchbase, LinkedIn, SEC scrapers)
- Strangelove Web3 MCP, DexPaprika
- ClinicalTrials.gov MCP, BioMCP

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.5.0 | 2026-02-09 | Added 45 skills from 7 new repos: Anthropic KWP (17), sickn33 (10), tradermonty (2), alirezarezvani (2), cookbooks (1), sundial (2), evolsb (1), NicholasSpisak (10). 84 downloaded SKILL.md files. |
| 1.4.0 | 2026-02-08 | Added 35 knowledge skills from propane-ai/kits, gerstep/cybos. Knowledge category fields. Download catalog with 48 SKILL.md files. |
| 1.3.1 | 2026-02-04 | Removed 4 duplicates, added interactive dashboard, source tracking |
| 1.3.0 | 2026-02-03 | Added 58 skills: Octagon AI suite, Crypto/Web3, Real Estate, Healthcare/Biotech |
| 1.2.0 | 2026-02-03 | Added 30 skills from SkillsMP: CRM integrations, VC research skills |
| 1.1.0 | 2026-02-03 | Added 31 skills: Claude Financial Services Skills, Apify scrapers |
| 1.0.0 | 2026-02-03 | Initial release with 156 skills |

See [SOURCES.md](SOURCES.md) for detailed crawl history and data provenance, or browse the [Sources & Attribution page](sources.html).

---

## Updating the Database

**Source of truth:** `vc_skills_database.json`

After editing the JSON, run the build script to regenerate all exports:

```bash
python3 build.py
```

This will:
1. Validate data (check for duplicates, missing fields)
2. Regenerate `vc_skills_database.csv`
3. Rebuild `index.html` with embedded data
4. Update all `by_workflow/*.md` files

```
vc_skills_database.json  ←── Edit this
         │
         │  python3 build.py
         ▼
         ├──→ index.html (dashboard)
         ├──→ vc_skills_database.csv
         └──→ by_workflow/*.md
```

---

## Contributing

To add a skill:
1. Fork this repository
2. Add entry to `vc_skills_database.json`
3. Run `python3 build.py`
4. Submit pull request

---

## License

This database is provided for informational purposes. Individual skills have their own licenses - check source repositories before use.
