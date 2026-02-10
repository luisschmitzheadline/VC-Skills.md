# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~project tracker` might mean Linear, Asana, Jira, or any other tracker with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (project tracker, design, product analytics, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Project tracker | `~~project tracker` | Linear, Asana, monday.com, ClickUp, Atlassian (Jira/Confluence) | Shortcut, Basecamp |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Design | `~~design` | Figma | Sketch, Adobe XD |
| Product analytics | `~~product analytics` | Amplitude, Pendo | Mixpanel, Heap, FullStory |
| User feedback | `~~user feedback` | Intercom | Productboard, Canny, UserVoice |
| Meeting transcription | `~~meeting transcription` | Fireflies | Gong, Dovetail, Otter.ai |

## Inputs for planning and reporting

Planning and reporting commands pull from these input categories. Use the placeholders in workflow steps and "Inputs from Tools" sections:

| Input category | Placeholder(s) | What to pull |
|----------------|----------------|--------------|
| **Communications** | ~~chat~~ | Team discussions, decisions, blockers, stakeholder threads |
| **Data** | ~~product analytics~~ | Usage, funnels, cohorts, adoption, metrics |
| **Research** | ~~knowledge base~~, ~~user feedback~~, ~~meeting transcription~~ | Prior research, specs, tickets/feedback, meeting notes |
| **Teams / work** | ~~project tracker~~ | Tickets, status, assignees, milestones, capacity |

## Context (role and company)

This plugin uses `context/role.md` and `context/company.md` in this folder so skills and commands stay aligned with your role and company. Overwrite these files with your own role description and company/board context; they are loaded as content for this plugin. Paths: `context/role.md`, `context/company.md`. When a command or skill says to check role/company context, it means this section and these files.
