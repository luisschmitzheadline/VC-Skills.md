# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~CRM` might mean Salesforce, HubSpot, or any other CRM with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (CRM, chat, email, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Calendar | `~~calendar` | Microsoft 365 | Google Calendar |
| Chat | `~~chat` | Slack | Microsoft Teams |
| CRM | `~~CRM` | HubSpot, Close | Salesforce, Pipedrive, Copper |
| Data enrichment | `~~data enrichment` | Clay, ZoomInfo | Apollo, Clearbit, Lusha |
| Email | `~~email` | Microsoft 365 | Gmail |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru |
| Meeting transcription | `~~conversation intelligence` | Fireflies | Gong, Chorus, Otter.ai |
| Project tracker | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |

## Context (role and company)

This plugin uses `context/role.md` and `context/company.md` in this folder so skills and commands stay aligned with your role and company. Overwrite these files with your own role description and company/board context; they are loaded as content for this plugin. Paths: `context/role.md`, `context/company.md`. When a command or skill says to check role/company context, it means this section and these files.
