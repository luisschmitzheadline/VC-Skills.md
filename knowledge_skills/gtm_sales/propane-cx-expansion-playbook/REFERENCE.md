# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~support platform` might mean Intercom, Zendesk, or any other support tool with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (support platform, CRM, chat, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Email | `~~email` | Microsoft 365 | — |
| Cloud storage | `~~cloud storage` | Microsoft 365 | — |
| Support platform | `~~support platform` | Intercom | Zendesk, Freshdesk, HubSpot Service Hub |
| CRM | `~~CRM` | HubSpot | Salesforce, Pipedrive |
| Knowledge base | `~~knowledge base` | Guru, Notion | Confluence, Help Scout |
| Project tracker | `~~project tracker` | Atlassian (Jira/Confluence) | Linear, Asana |
| Product analytics | `~~product analytics` | — (optional) | Amplitude, Mixpanel, Pendo, Gainsight |

**Note:** ~~product analytics~~ is optional. Use it for health scoring, churn prediction, and expansion (usage vs entitlement) when an MCP server for product analytics is connected. OVERVIEW Section 7 lists Amplitude/Pendo for CX Tier 2.

## Context (role and company)

This plugin uses `context/role.md` and `context/company.md` in this folder so skills and commands stay aligned with your role and company. Overwrite these files with your own role description and company/board context; they are loaded as content for this plugin. Paths: `context/role.md`, `context/company.md`. When a command or skill says to check role/company context, it means this section and these files.
