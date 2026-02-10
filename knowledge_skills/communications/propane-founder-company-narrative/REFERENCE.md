# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~CRM` might mean Salesforce, HubSpot, or any other CRM with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (CRM, chat, cap table, ATS, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| CRM | `~~CRM` | HubSpot | Salesforce, Pipedrive |
| Cap table / spreadsheet | `~~cap table` / `~~spreadsheet` | Microsoft 365 | Carta, Google Sheets, Notion |
| ATS | `~~ATS` | — (optional) | Greenhouse, Lever |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru |
| Project tracker | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |
| BI / data | `~~BI` / `~~spreadsheet` | Microsoft 365 | Looker, Tableau, Mode, Hex |
| Product analytics | `~~product analytics` | — (optional) | Amplitude, Mixpanel, Pendo |
| Email | `~~email` | Microsoft 365 | Gmail |

**Note:** ~~product analytics~~ is optional. Use it with ~~BI~~ for **views and reports from data tools** when an MCP server for product analytics is connected.

## Context (role and company)

This plugin uses `context/role.md` and `context/company.md` in this folder so skills and commands stay aligned with your role and company. Overwrite these files with your own role description and company/board context; they are loaded as content for this plugin. Paths: `context/role.md`, `context/company.md`. When a command or skill says to check role/company context, it means this section and these files.
