#!/usr/bin/env python3
"""
Download and catalog VC knowledge skills from GitHub repositories.

Downloads SKILL.md files and associated reference content for pure
knowledge/methodology skills that don't require external integrations.

Usage:
    python3 download_skills.py              # Download all skills
    python3 download_skills.py --dry-run    # Show what would be downloaded
    python3 download_skills.py --force      # Re-download even if cached
    python3 download_skills.py --skill id   # Download a single skill
    python3 download_skills.py --verbose    # Show detailed progress

Set GITHUB_TOKEN env var for higher API rate limits (5000 vs 60 req/hr).
"""

import argparse
import base64
import hashlib
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
UNAVAILABLE_DIR = SCRIPT_DIR / "unavailable"
MANIFEST_PATH = SCRIPT_DIR / "manifest.json"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
API_BASE = "https://api.github.com"
RAW_BASE = "https://raw.githubusercontent.com"

# Rate limit tracking
_api_calls = 0
_api_remaining = None


# =============================================================================
# REGISTRY: Every knowledge skill with its exact GitHub location
# =============================================================================

REGISTRY = {
    # --- anthropics/skills ---
    "anthropics-internal-comms": {
        "repo": "anthropics/skills",
        "path": "skills/internal-comms",
        "files": ["SKILL.md"],
        "dirs": ["examples"],
        "category": "communications",
        "source_label": "anthropics/skills",
    },

    # --- sickn33/antigravity-awesome-skills ---
    "antigravity-copywriting": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/copywriting",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "communications",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-pricing-strategy": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/pricing-strategy",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-quant-analyst": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/quant-analyst",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-business-analyst": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/business-analyst",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investment_analysis",
        "source_label": "sickn33/antigravity-awesome-skills",
    },

    # --- openclaw/skills ---
    "openclaw-market-environment-analysis": {
        "repo": "openclaw/skills",
        "path": "skills/veeramanikandanr48/market-environment-analysis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "openclaw/skills",
    },
    # --- rkiding/awesome-finance-skills ---
    "rkiding-alphaear-sentiment": {
        "repo": "rkiding/awesome-finance-skills",
        "path": "skills/alphaear-sentiment",
        "files": ["SKILL.md"],
        "dirs": ["references"],
        "category": "sentiment_signals",
        "source_label": "rkiding/awesome-finance-skills",
    },
    "rkiding-alphaear-signal-tracker": {
        "repo": "rkiding/awesome-finance-skills",
        "path": "skills/alphaear-signal-tracker",
        "files": ["SKILL.md"],
        "dirs": ["references"],
        "category": "sentiment_signals",
        "source_label": "rkiding/awesome-finance-skills",
    },

    # --- propane-ai/kits — Founder persona ---
    "propane-founder-board-prep": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/board-prep",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investor_relations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-company-narrative": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/company-narrative",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "communications",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-finance-and-runway": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/finance-and-runway",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-hiring": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/hiring",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-investor-management": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/investor-management",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investor_relations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-investor-research": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/investor-research",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investor_relations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-investor-updates": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/investor-updates",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investor_relations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-market-research": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/market-research",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-metrics-review": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/metrics-review",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-pitch-deck": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/pitch-deck",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investor_relations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-plan-creation": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/plan-creation",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-sales-investor-emails": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/sales-investor-emails",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investor_relations",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-stakeholder-comms": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/stakeholder-comms",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "communications",
        "source_label": "propane-ai/kits",
    },
    "propane-founder-data-and-metrics": {
        "repo": "propane-ai/kits",
        "path": "plugins/Founder/skills/data-and-metrics",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "propane-ai/kits",
    },

    # --- propane-ai/kits — GTM persona ---
    "propane-gtm-account-research": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/account-research",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-draft-outreach": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/draft-outreach",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-competitive-intelligence": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/competitive-intelligence",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-gtm-strategy": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/gtm-strategy",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-sales-playbook": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/sales-playbook",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-forecast": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/forecast",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-call-prep": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/call-prep",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-demo-script": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/demo-script",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-review-pipeline": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/review-pipeline",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-gtm-roi-calculator": {
        "repo": "propane-ai/kits",
        "path": "plugins/GTM/skills/roi-calculator",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "propane-ai/kits",
    },

    # --- propane-ai/kits — CX persona ---
    "propane-cx-churn-prediction": {
        "repo": "propane-ai/kits",
        "path": "plugins/CX/skills/churn-prediction",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },
    "propane-cx-expansion-playbook": {
        "repo": "propane-ai/kits",
        "path": "plugins/CX/skills/expansion-playbook",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },
    "propane-cx-health-scoring": {
        "repo": "propane-ai/kits",
        "path": "plugins/CX/skills/health-scoring",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },
    "propane-cx-prepare-quarterly-business-review": {
        "repo": "propane-ai/kits",
        "path": "plugins/CX/skills/prepare-quarterly-business-review",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },

    # --- propane-ai/kits — Product persona ---
    "propane-product-competitive-analysis": {
        "repo": "propane-ai/kits",
        "path": "plugins/Product/skills/competitive-analysis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "propane-ai/kits",
    },
    "propane-product-metrics-tracking": {
        "repo": "propane-ai/kits",
        "path": "plugins/Product/skills/metrics-tracking",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },
    "propane-product-progress-reporting": {
        "repo": "propane-ai/kits",
        "path": "plugins/Product/skills/progress-reporting",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },
    "propane-product-roadmap-management": {
        "repo": "propane-ai/kits",
        "path": "plugins/Product/skills/roadmap-management",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "propane-ai/kits",
    },
    "propane-product-user-research-synthesis": {
        "repo": "propane-ai/kits",
        "path": "plugins/Product/skills/user-research-synthesis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "propane-ai/kits",
    },

    # --- propane-ai/kits — Marketing persona ---
    "propane-marketing-competitive-analysis": {
        "repo": "propane-ai/kits",
        "path": "plugins/Marketing/skills/competitive-analysis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "propane-ai/kits",
    },
    "propane-marketing-product-marketing": {
        "repo": "propane-ai/kits",
        "path": "plugins/Marketing/skills/product-marketing",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "propane-ai/kits",
    },

    # --- gerstep/cybos ---
    "cybos-research": {
        "repo": "gerstep/cybos",
        "path": ".claude/skills/Research",
        "files": ["SKILL.md"],
        "dirs": ["shared", "workflows", "evals"],
        "category": "due_diligence",
        "source_label": "gerstep/cybos",
    },
    "cybos-ddmemo": {
        "repo": "gerstep/cybos",
        "path": ".claude/skills/DDMemo",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "gerstep/cybos",
    },
    "cybos-gtd": {
        "repo": "gerstep/cybos",
        "path": ".claude/skills/GTD",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "gerstep/cybos",
    },
    "cybos-content": {
        "repo": "gerstep/cybos",
        "path": ".claude/skills/Content",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "communications",
        "source_label": "gerstep/cybos",
    },
    "cybos-summarize": {
        "repo": "gerstep/cybos",
        "path": ".claude/skills/Summarize",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "gerstep/cybos",
    },

    # --- anthropics/knowledge-work-plugins (finance) ---
    "kwp-variance-analysis": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "finance/skills/variance-analysis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-financial-statements": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "finance/skills/financial-statements",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-audit-support": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "finance/skills/audit-support",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-close-management": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "finance/skills/close-management",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-journal-entry-prep": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "finance/skills/journal-entry-prep",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-reconciliation": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "finance/skills/reconciliation",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "anthropics/knowledge-work-plugins",
    },

    # --- anthropics/knowledge-work-plugins (legal) ---
    "kwp-legal-risk-assessment": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "legal/skills/legal-risk-assessment",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-contract-review": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "legal/skills/contract-review",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-nda-triage": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "legal/skills/nda-triage",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-compliance": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "legal/skills/compliance",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-meeting-briefing": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "legal/skills/meeting-briefing",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "communications",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-canned-responses": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "legal/skills/canned-responses",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "communications",
        "source_label": "anthropics/knowledge-work-plugins",
    },

    # --- anthropics/knowledge-work-plugins (sales) ---
    "kwp-competitive-intelligence-sales": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "sales/skills/competitive-intelligence",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-account-research": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "sales/skills/account-research",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "anthropics/knowledge-work-plugins",
    },

    # --- anthropics/knowledge-work-plugins (product-management) ---
    "kwp-competitive-analysis-pm": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "product-management/skills/competitive-analysis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "anthropics/knowledge-work-plugins",
    },
    "kwp-feature-spec": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "product-management/skills/feature-spec",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "anthropics/knowledge-work-plugins",
    },

    # --- anthropics/knowledge-work-plugins (marketing) ---
    "kwp-competitive-analysis-marketing": {
        "repo": "anthropics/knowledge-work-plugins",
        "path": "marketing/skills/competitive-analysis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "anthropics/knowledge-work-plugins",
    },

    # --- sickn33/antigravity-awesome-skills (new additions) ---
    "antigravity-startup-financial-modeling": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/startup-financial-modeling",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-market-sizing-analysis": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/market-sizing-analysis",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-startup-analyst": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/startup-analyst",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investment_analysis",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-startup-metrics-framework": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/startup-metrics-framework",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-competitive-landscape": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/competitive-landscape",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-data-storytelling": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/data-storytelling",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "communications",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-kpi-dashboard-design": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/kpi-dashboard-design",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-product-manager-toolkit": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/product-manager-toolkit",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-launch-strategy": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/launch-strategy",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "gtm_sales",
        "source_label": "sickn33/antigravity-awesome-skills",
    },
    "antigravity-ai-product": {
        "repo": "sickn33/antigravity-awesome-skills",
        "path": "skills/ai-product",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "sickn33/antigravity-awesome-skills",
    },

    # --- tradermonty/claude-trading-skills ---
    "tradermonty-scenario-analyzer": {
        "repo": "tradermonty/claude-trading-skills",
        "path": "skills/scenario-analyzer",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investment_analysis",
        "source_label": "tradermonty/claude-trading-skills",
    },
    "tradermonty-bubble-detector": {
        "repo": "tradermonty/claude-trading-skills",
        "path": "skills/us-market-bubble-detector",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "investment_analysis",
        "source_label": "tradermonty/claude-trading-skills",
    },

    # --- alirezarezvani/claude-skills ---
    "alirezarezvani-ceo-advisor": {
        "repo": "alirezarezvani/claude-skills",
        "path": "c-level-advisor/ceo-advisor",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "portfolio_operations",
        "source_label": "alirezarezvani/claude-skills",
    },
    "alirezarezvani-financial-analyst": {
        "repo": "alirezarezvani/claude-skills",
        "path": "finance/financial-analyst",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "alirezarezvani/claude-skills",
    },

    # --- anthropics/claude-cookbooks ---
    "cookbooks-creating-financial-models": {
        "repo": "anthropics/claude-cookbooks",
        "path": "skills/custom_skills/creating-financial-models",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "financial_modeling",
        "source_label": "anthropics/claude-cookbooks",
    },

    # --- sundial-org/awesome-openclaw-skills ---
    "sundial-pre-mortem-analyst": {
        "repo": "sundial-org/awesome-openclaw-skills",
        "path": "skills/pre-mortem-analyst",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "due_diligence",
        "source_label": "sundial-org/awesome-openclaw-skills",
    },
    "sundial-competitive-intelligence": {
        "repo": "sundial-org/awesome-openclaw-skills",
        "path": "skills/competitive-intelligence-market-research",
        "files": ["SKILL.md"],
        "dirs": [],
        "category": "market_research",
        "source_label": "sundial-org/awesome-openclaw-skills",
    },

    # --- evolsb/claude-legal-skill ---
    "evolsb-contract-review": {
        "repo": "evolsb/claude-legal-skill",
        "path": ".",
        "files": ["skill.md"],  # Source repo uses lowercase; we rename to SKILL.md locally
        "dirs": [],
        "category": "due_diligence",
        "source_label": "evolsb/claude-legal-skill",
    },
}

# Anthropic FS skills (behind waitlist — stub only)
ANTHROPIC_FS_STUBS = {
    "anthropic-fs-3-statement-modeling": {
        "name": "3-Statement Financial Modeling",
        "description": "Build integrated 3-statement financial models (Income Statement, Balance Sheet, Cash Flow) with linked assumptions and projections.",
        "category": "financial_modeling",
    },
    "anthropic-fs-comps-analysis": {
        "name": "Comps Analysis",
        "description": "Comparable company analysis with automated peer selection, multiple calculation, and valuation ranges.",
        "category": "financial_modeling",
    },
    "anthropic-fs-competitive-landscape": {
        "name": "Competitive Landscape Analysis",
        "description": "Systematic competitive landscape mapping with market positioning, differentiation analysis, and strategic implications.",
        "category": "market_research",
    },
    "anthropic-fs-dcf-modeling": {
        "name": "DCF Modeling",
        "description": "Discounted Cash Flow models with WACC calculation, terminal value estimation, and sensitivity analysis.",
        "category": "financial_modeling",
    },
    "anthropic-fs-dd-data-pack": {
        "name": "Due Diligence Data Pack",
        "description": "Process and analyze data room documents for investment due diligence with structured extraction and risk flagging.",
        "category": "due_diligence",
    },
    "anthropic-fs-earnings-analysis": {
        "name": "Earnings Analysis",
        "description": "Analyze earnings releases, transcripts, and guidance with beat/miss tracking and forward estimate impacts.",
        "category": "investment_analysis",
    },
    "anthropic-fs-initiating-coverage": {
        "name": "Initiating Coverage Research",
        "description": "Generate initiating coverage research reports with thesis development, valuation, and risk assessment.",
        "category": "investment_analysis",
    },
    "anthropic-fs-ib-pitch-deck": {
        "name": "Investment Banking Pitch Deck",
        "description": "Create investment banking pitch books with deal positioning, comparable transactions, and strategic rationale.",
        "category": "investor_relations",
    },
    "anthropic-fs-presentation-checker": {
        "name": "Presentation Quality Checker",
        "description": "Audit financial presentations for accuracy, consistency, formatting standards, and regulatory compliance.",
        "category": "communications",
    },
    "anthropic-fs-company-profile": {
        "name": "Company Profile/Strip Creator",
        "description": "Generate 1-2 page company profiles with key metrics, business overview, and investment highlights.",
        "category": "investment_analysis",
    },
    "anthropic-fs-creating-financial-models": {
        "name": "Creating Financial Models",
        "description": "General-purpose financial modeling skill for building custom financial models from scratch.",
        "category": "financial_modeling",
    },
}

# Knowledge categories and their descriptions
CATEGORIES = {
    "investment_analysis": "Frameworks for evaluating investment opportunities, thesis development, and decision-making",
    "financial_modeling": "Financial model construction, valuation methodologies, and quantitative analysis",
    "market_research": "Market sizing, competitive landscapes, sector analysis, and trend identification",
    "due_diligence": "Structured DD processes, data room analysis, and risk assessment frameworks",
    "portfolio_operations": "Supporting portfolio companies with ops, hiring, planning, and metrics",
    "investor_relations": "LP communication, fundraising materials, pitch decks, and board prep",
    "gtm_sales": "Go-to-market strategy, sales playbooks, outreach, and pipeline management",
    "communications": "Internal comms, content creation, copywriting, and stakeholder updates",
    "sentiment_signals": "Market sentiment analysis, signal tracking, and news aggregation",
}


# =============================================================================
# API helpers
# =============================================================================

def github_request(url, accept="application/vnd.github.v3+json"):
    """Make a GitHub API request with optional auth."""
    global _api_calls, _api_remaining
    headers = {"Accept": accept, "User-Agent": "vc-skills-downloader"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    req = urllib.request.Request(url, headers=headers)
    try:
        _api_calls += 1
        resp = urllib.request.urlopen(req)
        _api_remaining = resp.headers.get("X-RateLimit-Remaining")
        return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 403 and "rate limit" in e.read().decode("utf-8", errors="replace").lower():
            print(f"  [RATE LIMITED] GitHub API rate limit hit after {_api_calls} calls")
            print(f"  Set GITHUB_TOKEN env var for 5000 req/hr (current: 60)")
            return None
        if e.code == 404:
            return None
        raise


def download_raw_file(repo, path):
    """Download a raw file from GitHub."""
    url = f"{RAW_BASE}/{repo}/main/{path}"
    headers = {"User-Agent": "vc-skills-downloader"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req)
        return resp.read().decode("utf-8")
    except urllib.error.HTTPError:
        # Try HEAD branch
        url2 = f"{RAW_BASE}/{repo}/HEAD/{path}"
        req2 = urllib.request.Request(url2, headers=headers)
        try:
            resp2 = urllib.request.urlopen(req2)
            return resp2.read().decode("utf-8")
        except urllib.error.HTTPError:
            return None


def list_directory(repo, path):
    """List files in a GitHub directory via API."""
    url = f"{API_BASE}/repos/{repo}/contents/{path}"
    data = github_request(url)
    if data is None:
        return []
    if isinstance(data, list):
        return data
    return []


def sha256(content):
    """Compute SHA256 hash of content string."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


# =============================================================================
# Download logic
# =============================================================================

def download_skill(skill_id, entry, force=False, verbose=False):
    """Download a single skill's files. Returns status dict."""
    repo = entry["repo"]
    base_path = entry["path"]
    source_dir = SCRIPT_DIR / entry["category"] / skill_id

    result = {
        "skill_id": skill_id,
        "repo": repo,
        "path": base_path,
        "category": entry["category"],
        "source_label": entry["source_label"],
        "files": {},
        "status": "downloaded",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    source_dir.mkdir(parents=True, exist_ok=True)

    # Download main files (SKILL.md etc)
    for filename in entry["files"]:
        file_path = f"{base_path}/{filename}"
        out_path = source_dir / filename

        if out_path.exists() and not force:
            content = out_path.read_text(encoding="utf-8")
            result["files"][filename] = {
                "size": len(content),
                "sha256": sha256(content),
                "cached": True,
            }
            if verbose:
                print(f"    [cached] {filename} ({len(content)} bytes)")
            continue

        if verbose:
            print(f"    Downloading {repo}/{file_path}...")

        content = download_raw_file(repo, file_path)
        if content is None:
            result["files"][filename] = {"status": "not_found"}
            result["status"] = "partial"
            if verbose:
                print(f"    [NOT FOUND] {filename}")
            continue

        out_path.write_text(content, encoding="utf-8")
        result["files"][filename] = {
            "size": len(content),
            "sha256": sha256(content),
            "cached": False,
        }
        if verbose:
            print(f"    [OK] {filename} ({len(content)} bytes)")

    # Download subdirectories
    for subdir in entry.get("dirs", []):
        dir_path = f"{base_path}/{subdir}"
        items = list_directory(repo, dir_path)

        if not items:
            if verbose:
                print(f"    [SKIP] {subdir}/ (empty or not found)")
            continue

        sub_out = source_dir / subdir
        sub_out.mkdir(parents=True, exist_ok=True)

        for item in items:
            if item["type"] != "file":
                continue
            fname = item["name"]
            fout = sub_out / fname

            if fout.exists() and not force:
                content = fout.read_text(encoding="utf-8")
                result["files"][f"{subdir}/{fname}"] = {
                    "size": len(content),
                    "sha256": sha256(content),
                    "cached": True,
                }
                if verbose:
                    print(f"    [cached] {subdir}/{fname}")
                continue

            content = download_raw_file(repo, f"{dir_path}/{fname}")
            if content is None:
                continue

            fout.write_text(content, encoding="utf-8")
            result["files"][f"{subdir}/{fname}"] = {
                "size": len(content),
                "sha256": sha256(content),
                "cached": False,
            }
            if verbose:
                print(f"    [OK] {subdir}/{fname} ({len(content)} bytes)")

    # Check if we got the main SKILL.md
    main_file = entry["files"][0] if entry["files"] else "SKILL.md"
    if result["files"].get(main_file, {}).get("status") == "not_found":
        result["status"] = "failed"

    return result


def create_stubs(verbose=False):
    """Create stub files for unavailable Anthropic FS skills."""
    results = {}
    UNAVAILABLE_DIR.mkdir(parents=True, exist_ok=True)

    for stub_id, info in ANTHROPIC_FS_STUBS.items():
        out_path = UNAVAILABLE_DIR / f"{stub_id}.stub.md"
        content = f"""# {info['name']}

> **Status:** Unavailable — Behind Anthropic Financial Services waitlist

## Description

{info['description']}

## Category

{info['category'].replace('_', ' ').title()}

## Access

This skill is part of Anthropic's Claude for Financial Services offering.
It requires enrollment in the Financial Services program.

See: https://support.claude.com/en/articles/12663107-claude-for-financial-services-skills

---

*This is a placeholder stub. The actual skill content is not publicly available.*
"""
        out_path.write_text(content, encoding="utf-8")
        results[stub_id] = {
            "status": "unavailable",
            "name": info["name"],
            "category": info["category"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        if verbose:
            print(f"  [STUB] {info['name']}")

    return results


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Download VC knowledge skills from GitHub")
    parser.add_argument("--dry-run", action="store_true", help="Show planned downloads without executing")
    parser.add_argument("--force", action="store_true", help="Re-download even if cached")
    parser.add_argument("--skill", type=str, help="Download a single skill by ID")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed progress")
    args = parser.parse_args()

    print("=" * 60)
    print("VC Knowledge Skills Downloader")
    print("=" * 60)

    if GITHUB_TOKEN:
        print(f"GitHub token: configured (5000 req/hr)")
    else:
        print(f"GitHub token: not set (60 req/hr)")
        print(f"  Set GITHUB_TOKEN env var for higher limits")
    print()

    # Filter registry if --skill specified
    registry = REGISTRY
    if args.skill:
        if args.skill in registry:
            registry = {args.skill: registry[args.skill]}
        else:
            print(f"Unknown skill: {args.skill}")
            print(f"Available: {', '.join(sorted(REGISTRY.keys()))}")
            return 1

    # Dry run mode
    if args.dry_run:
        print(f"DRY RUN — {len(registry)} skills to download:\n")
        for sid, entry in sorted(registry.items()):
            files = ", ".join(entry["files"])
            dirs = ", ".join(entry.get("dirs", [])) or "(none)"
            print(f"  {sid}")
            print(f"    Repo:  {entry['repo']}")
            print(f"    Path:  {entry['path']}")
            print(f"    Files: {files}")
            print(f"    Dirs:  {dirs}")
            print(f"    Cat:   {entry['category']}")
            print()
        print(f"\nPlus {len(ANTHROPIC_FS_STUBS)} stub files for unavailable Anthropic FS skills")
        return 0

    # Load existing manifest if present
    manifest = {"skills": {}, "stubs": {}, "generated": None}
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            manifest = json.load(f)

    # Download skills
    print(f"Downloading {len(registry)} skills...\n")
    downloaded = 0
    failed = 0

    for sid, entry in sorted(registry.items()):
        print(f"  [{downloaded+failed+1}/{len(registry)}] {sid}")
        result = download_skill(sid, entry, force=args.force, verbose=args.verbose)
        manifest["skills"][sid] = result

        if result["status"] == "downloaded":
            downloaded += 1
            total_size = sum(f.get("size", 0) for f in result["files"].values())
            cached = all(f.get("cached", False) for f in result["files"].values() if "size" in f)
            tag = "cached" if cached else "OK"
            print(f"    [{tag}] {len(result['files'])} files, {total_size:,} bytes")
        elif result["status"] == "partial":
            downloaded += 1
            print(f"    [PARTIAL] Some files missing")
        else:
            failed += 1
            print(f"    [FAILED]")

        # Brief pause to be nice to the API
        time.sleep(0.1)

    print()

    # Create stubs
    print(f"Creating {len(ANTHROPIC_FS_STUBS)} stub files...")
    stub_results = create_stubs(verbose=args.verbose)
    manifest["stubs"] = stub_results
    print(f"  Done")
    print()

    # Save manifest
    manifest["generated"] = datetime.now(timezone.utc).isoformat()
    manifest["api_calls"] = _api_calls
    manifest["api_remaining"] = _api_remaining

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    # Summary
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"  Downloaded:  {downloaded}")
    print(f"  Failed:      {failed}")
    print(f"  Stubs:       {len(ANTHROPIC_FS_STUBS)}")
    print(f"  API calls:   {_api_calls}")
    print(f"  Manifest:    {MANIFEST_PATH}")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
