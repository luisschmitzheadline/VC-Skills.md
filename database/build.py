#!/usr/bin/env python3
"""
Build script for VC Skills Database.

Run this after editing vc_skills_database.json to regenerate all exports:
  python3 build.py

This will update:
  - index.html (dashboard with embedded data)
  - vc_skills_database.csv (spreadsheet export)
  - by_workflow/*.md (workflow documentation)
"""

import json
import csv
import os
from collections import defaultdict, Counter
from pathlib import Path

# Get script directory
SCRIPT_DIR = Path(__file__).parent

def load_data():
    """Load the JSON database."""
    with open(SCRIPT_DIR / 'vc_skills_database.json', 'r') as f:
        return json.load(f)

def validate_data(data):
    """Check for duplicates and missing fields."""
    skills = data['skills']
    errors = []

    # Check duplicates
    names = [s['name'] for s in skills]
    dupes = [n for n, c in Counter(names).items() if c > 1]
    if dupes:
        errors.append(f"Duplicate names found: {dupes}")

    # Check required fields
    required = ['id', 'name', 'source', 'source_type', 'description', 'vc_workflows', 'skill_type']
    for skill in skills:
        for field in required:
            if not skill.get(field):
                errors.append(f"Missing {field} in {skill.get('name', skill.get('id', 'unknown'))}")

    # Validate new enum fields
    valid_categories = {
        None, 'investment_analysis', 'financial_modeling', 'market_research',
        'due_diligence', 'portfolio_operations', 'investor_relations',
        'gtm_sales', 'communications', 'sentiment_signals', 'founder_toolkit'
    }
    valid_download = {None, 'downloaded', 'unavailable'}

    for skill in skills:
        cat = skill.get('knowledge_category')
        if cat not in valid_categories:
            errors.append(f"Invalid knowledge_category '{cat}' in {skill.get('id')}")
        dl = skill.get('download_status')
        if dl not in valid_download:
            errors.append(f"Invalid download_status '{dl}' in {skill.get('id')}")

    return errors

def build_csv(data):
    """Generate CSV export."""
    skills = data['skills']

    headers = [
        'ID', 'Name', 'Source', 'Source Type', 'Description',
        'VC Workflows', 'VC Tasks', 'Skill Type', 'Installation',
        'Official', 'Verified', 'Tags', 'Notes', 'VC Relevance',
        'Requires Integration', 'Knowledge Category', 'Download Status'
    ]

    with open(SCRIPT_DIR / 'vc_skills_database.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for s in skills:
            ri = s.get('requires_integration')
            writer.writerow([
                s['id'],
                s['name'],
                s['source'],
                s['source_type'],
                s['description'],
                ', '.join(s.get('vc_workflows', [])),
                ', '.join(s.get('vc_tasks', [])),
                s['skill_type'],
                s.get('installation', ''),
                'Yes' if s.get('official') else 'No',
                'Yes' if s.get('verified') else 'No',
                ', '.join(s.get('tags', [])),
                s.get('notes', ''),
                s.get('vc_relevance', ''),
                'Yes' if ri is True else ('No' if ri is False else ''),
                s.get('knowledge_category', '') or '',
                s.get('download_status', '') or ''
            ])

    print(f"✓ CSV: {len(skills)} skills exported")

def build_dashboard(data):
    """Rebuild dashboard with embedded JSON."""
    html_path = SCRIPT_DIR / 'index.html'

    with open(html_path, 'r') as f:
        html = f.read()

    # Find and replace the embedded data
    start_marker = 'const DATA = '
    end_marker = ';\n    const skills = DATA.skills'

    start_idx = html.find(start_marker) + len(start_marker)
    end_idx = html.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("✗ Dashboard: Could not find data markers")
        return

    # Create minified JSON
    json_str = json.dumps(data, separators=(',', ':'))

    # Rebuild HTML
    new_html = html[:start_idx] + json_str + html[end_idx:]

    with open(html_path, 'w') as f:
        f.write(new_html)

    print(f"✓ Dashboard: {len(data['skills'])} skills embedded ({len(new_html):,} bytes)")

def build_workflow_docs(data):
    """Generate workflow markdown files."""
    skills = data['skills']

    # Group by workflow
    by_workflow = defaultdict(list)
    for s in skills:
        for wf in s.get('vc_workflows', []):
            by_workflow[wf].append(s)

    # Workflow metadata
    workflow_info = {
        'deal_sourcing': {
            'title': 'Deal Sourcing & Flow',
            'description': 'Skills for finding and evaluating new investment opportunities including thematic research, market mapping, and company identification.'
        },
        'due_diligence': {
            'title': 'Due Diligence',
            'description': 'Skills for evaluating investment opportunities including financial analysis, technical DD, market sizing, and management research.'
        },
        'portfolio_support': {
            'title': 'Portfolio Support',
            'description': 'Skills for supporting existing portfolio companies including KPI tracking, board materials, and competitor monitoring.'
        },
        'fund_operations': {
            'title': 'Fund Operations',
            'description': 'Skills for managing the fund including LP reporting, document generation, and investor relations.'
        },
        'data_infrastructure': {
            'title': 'Data Infrastructure',
            'description': 'Skills for building data systems including database queries, web scraping, data enrichment, and signal generation.'
        },
        'automation': {
            'title': 'Automation & Productivity',
            'description': 'Skills for automating workflows including research automation, email management, and process orchestration.'
        },
        'founder_support': {
            'title': 'Founder Support',
            'description': 'Skills for supporting founders including fundraising, GTM strategy, pricing, growth frameworks, and startup validation.'
        }
    }

    type_order = ['connector', 'skill', 'mcp_server', 'knowledge']
    type_labels = {
        'connector': 'Official Connectors',
        'skill': 'Claude Code Skills',
        'mcp_server': 'MCP Servers',
        'knowledge': 'Knowledge Skills'
    }

    workflow_dir = SCRIPT_DIR / 'by_workflow'
    workflow_dir.mkdir(exist_ok=True)

    for wf, info in workflow_info.items():
        skills_list = by_workflow[wf]

        # Group by type
        by_type = defaultdict(list)
        for s in skills_list:
            by_type[s['skill_type']].append(s)

        # Build markdown
        md = f"# {info['title']}\n\n"
        md += f"{info['description']}\n\n"
        md += f"**Total Skills:** {len(skills_list)}\n\n"
        md += "---\n\n"

        for t in type_order:
            if t not in by_type:
                continue
            items = sorted(by_type[t], key=lambda x: x['name'])
            md += f"## {type_labels[t]}\n\n"
            md += "| Name | Description | Tasks | Official |\n"
            md += "|------|-------------|-------|----------|\n"
            for s in items:
                desc = s['description'][:80] + '...' if len(s['description']) > 80 else s['description']
                tasks = ', '.join(s.get('vc_tasks', [])[:3])
                official = 'Yes' if s.get('official') else 'No'
                md += f"| {s['name']} | {desc} | {tasks} | {official} |\n"
            md += "\n"

        with open(workflow_dir / f'{wf}.md', 'w') as f:
            f.write(md)

    print(f"✓ Workflow docs: {len(workflow_info)} files updated")

def build_workflow_readme(data):
    """Update the by_workflow README with correct counts."""
    skills = data['skills']

    # Count by workflow
    counts = defaultdict(int)
    for s in skills:
        for wf in s.get('vc_workflows', []):
            counts[wf] += 1

    readme = """# Skills by Workflow

This folder contains skills organized by VC workflow category. Each file lists all skills relevant to that workflow, grouped by type (Connector, Skill, MCP Server).

| File | Workflow | Skills |
|------|----------|--------|
| [deal_sourcing.md](deal_sourcing.md) | Deal Sourcing & Flow | {deal_sourcing} |
| [due_diligence.md](due_diligence.md) | Due Diligence | {due_diligence} |
| [portfolio_support.md](portfolio_support.md) | Portfolio Support | {portfolio_support} |
| [fund_operations.md](fund_operations.md) | Fund Operations | {fund_operations} |
| [data_infrastructure.md](data_infrastructure.md) | Data Infrastructure | {data_infrastructure} |
| [automation.md](automation.md) | Automation & Productivity | {automation} |

Note: Skills can appear in multiple workflows, so totals exceed {total}.

For interactive browsing, use the [dashboard](../index.html) in the parent folder.
""".format(
        deal_sourcing=counts['deal_sourcing'],
        due_diligence=counts['due_diligence'],
        portfolio_support=counts['portfolio_support'],
        fund_operations=counts['fund_operations'],
        data_infrastructure=counts['data_infrastructure'],
        automation=counts['automation'],
        total=len(skills)
    )

    with open(SCRIPT_DIR / 'by_workflow' / 'README.md', 'w') as f:
        f.write(readme)

def main():
    print("=" * 50)
    print("VC Skills Database Build")
    print("=" * 50)
    print()

    # Load data
    print("Loading vc_skills_database.json...")
    data = load_data()
    skills = data['skills']
    print(f"Found {len(skills)} skills (v{data['metadata']['version']})")
    print()

    # Validate
    print("Validating...")
    errors = validate_data(data)
    if errors:
        print("✗ Validation errors:")
        for e in errors:
            print(f"  - {e}")
        print("\nFix errors before building.")
        return 1
    print("✓ Validation passed")
    print()

    # Build all outputs
    print("Building outputs...")
    build_csv(data)
    build_dashboard(data)
    build_workflow_docs(data)
    build_workflow_readme(data)
    print()

    # Summary
    print("=" * 50)
    print("Build complete!")
    print(f"  Skills: {len(skills)}")
    print(f"  Types: {dict(Counter(s['skill_type'] for s in skills))}")
    print("=" * 50)

    return 0

if __name__ == '__main__':
    exit(main())
