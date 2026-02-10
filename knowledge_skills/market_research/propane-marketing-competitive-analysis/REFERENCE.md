# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~marketing automation` might mean HubSpot, Marketo, or any other marketing platform with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (design, SEO, email marketing, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Design | `~~design` | Canva, Figma | Adobe Creative Cloud |
| Marketing automation | `~~marketing automation` | HubSpot | Marketo, Pardot, Mailchimp |
| CRM | `~~CRM` | HubSpot | Salesforce, Pipedrive |
| Product analytics | `~~product analytics` | Amplitude | Mixpanel, Google Analytics |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru |
| SEO | `~~SEO` | Ahrefs, Similarweb | Semrush, Moz |
| Email marketing | `~~email marketing` | Klaviyo | Mailchimp, Brevo, Customer.io |

**Note:** ~~product analytics~~ is optional. Use it for performance reporting, campaign planning, and SEO audits when an MCP server for product analytics is connected.

## Context (role and company)

This plugin uses `context/role.md` and `context/company.md` in this folder so skills and commands stay aligned with your role and company. Overwrite these files with your own role description and company/board context; they are loaded as content for this plugin. Paths: `context/role.md`, `context/company.md`. When a command or skill says to check role/company context, it means this section and these files.
