# Demo Cheat Sheet

Quick reference for the episode recording. Copy-paste ready.

---

## PRE-RECORDING SETUP

### 1. MCPs

**Linear MCP:** Will install LIVE during demo (Section 2)
```bash
claude mcp add --transport http linear https://mcp.linear.app/mcp
```
Then run `/mcp` to authenticate.

**Google Workspace MCP:** PRE-CONFIGURED (don't disconnect!)
- Too complex to set up live (requires Google Cloud Console, OAuth, 10+ APIs)
- Talking point: "Similar process, just more APIs to enable. The AI can walk you through it."

### 2. Pre-Created Assets (already done)

| Asset | Location | Status |
|-------|----------|--------|
| Google Sheet: "Calendar Integration Survey Responses" | Google Drive | ✅ Created |
| Google Doc: "Stakeholder Meeting Notes" | Google Drive | ✅ Created |
| Linear Project: "TaskFlow Calendar Integration" | Linear | ✅ Created |

### 3. Local Files (in episode-demo/)

| File | Purpose |
|------|---------|
| `feature-context.md` | @ reference for survey creation |
| `survey-template.md` | @ reference for survey creation |
| `image_gen.py` | Gemini API script (wrap in skill) |
| `.env` | Has GEMINI_API_KEY |
| `docs/prd.md` | Template for GitHub repo version |
| `linear-status-sync.py` | Pre-written for Section 12 |
| `hooks-diagram.html` | Visual reference for Section 6 |

### 4. Skills Pre-Installed

| Skill | Location |
|-------|----------|
| Research Synthesis | `.claude/skills/research-synthesis/SKILL.md` |

---

## DEMO FLOW

### Section 2: Install Linear MCP Live

**Command to run:**
```bash
claude mcp add --transport http linear https://mcp.linear.app/mcp
```

**Then authenticate:**
```
/mcp
```

**Show Google Workspace is already connected:**
> "Read a file from my Google Drive"

**Talking point:**
> "I already have Google Workspace connected. It's a similar process — just more APIs to enable in Google Cloud Console. If you want to set it up, just ask Claude to help you through it."

---

### Section 3: Create UXR Survey

**Prompt:**
> Create a user research survey for calendar integration based on @feature-context.md and @survey-template.md. Save it to Google Docs.

**Files used:** `feature-context.md`, `survey-template.md`
**Created during demo:** Google Doc (UXR Survey)

---

### Section 4: Synthesize Research + Skills Deep Dive

**THREE SKILL SCENARIOS:**
1. ✅ **Use pre-installed skill** — research-synthesis auto-triggers
2. ✅ **Get from marketplace** — download document-skills
3. ✅ **Build live** — create image-generation skill

---

**1️⃣ USE PRE-INSTALLED SKILL**

**Prompt:**
> Read the survey responses from the "Calendar Integration Survey Responses" Google Sheet and analyze them.

**What happens:** Research Synthesis skill auto-triggers

**Show skill structure:**
```
.claude/skills/research-synthesis/
└── SKILL.md
```

**2️⃣ GET FROM MARKETPLACE**

Step 1 — Add marketplace (one-time):
```
/plugin marketplace add anthropics/skills
```

Step 2 — Install:
```
/plugin install document-skills@anthropic-agent-skills
```

Step 3 — Restart Claude Code to load the plugin

---

**3️⃣ BUILD SKILL LIVE**

**Prompt:**
> Create a skill that wraps image_gen.py for generating images, diagrams, and user journey maps

**Skill to create:** `.claude/skills/image-generation/SKILL.md`
```markdown
---
name: image-generation
description: Use this when the user wants to generate images, diagrams, user journey maps, flowcharts, or visual assets for documents.
---

# Image Generation Skill

Generate images using the Gemini API via the image_gen.py script.

## When to Use
- User asks for a visual, diagram, or image
- User wants a user journey map or flowchart
- User needs an illustration for a document

## How to Use
Call the generate() function from image_gen.py with a descriptive prompt.
```

---

### Section 5: Create PRD + User Journey Map

**Prompt:**
> Create a PRD for the calendar integration feature based on the research synthesis. Save it to Google Docs.

**Created during demo:** Google Doc (PRD)

**Then ask for visual (skill payoff):**
> Add a user journey map showing the calendar integration flow

**What happens:** Image generation skill auto-triggers and runs:
```python
from image_gen import generate
generate('user journey map showing calendar integration flow: user opens TaskFlow, clicks sync, authorizes calendar, sees tasks appear in calendar')
```

Image saves to `outputs/` folder

---

### Section 6: Create Slides + Notification Hook

**Build notification hook:**
> Create a hook that sends me a Mac notification when you finish a task

**Hook config (for reference):**
```json
{
  "hooks": {
    "Stop": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "osascript -e 'display notification \"Claude finished!\" with title \"Claude Code\"'"
      }]
    }]
  }
}
```

**Kick off slides:**
> Create a stakeholder presentation based on the PRD

**Show:** `hooks-diagram.html` while waiting

---

### Section 7-8: Stakeholder Feedback

**Show:** "Stakeholder Meeting Notes" Google Doc

**Prompt:**
> Read the "Stakeholder Meeting Notes" Google Doc and update the PRD with the new requirements

---

### Section 9: Create Linear Tickets

**Prompt:**
> Break the PRD into engineering tickets and create them in Linear in the "TaskFlow Calendar Integration" project

**Created during demo:** 4-5 Linear tickets

---

### Section 10: Add Tickets to PRD

**Prompt:**
> Add a ticket status table to the PRD with links to the Linear tickets you just created

---

### Section 10b: Update Ticket Status

**Prompt:**
> Update a couple of the tickets — mark some as "In Progress" and one as "Done"

---

### Section 11: GitHub Actions (@mention)

**PRE-SETUP (before demo):**

1. Create GitHub repo (e.g., `taskflow-calendar-demo`)

2. Copy `docs/prd.md` to the repo

3. Install Claude GitHub App: https://github.com/apps/claude

4. Add repository secret:
   - Go to repo → Settings → Secrets and variables → Actions
   - Add secret: `ANTHROPIC_API_KEY` = your Claude API key

5. Create `.github/workflows/claude.yml`:
```yaml
name: Claude
on:
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created, edited]

jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

6. Test: Create an issue with `@claude say hello`

---

**DURING DEMO:**

**Create GitHub issue with:**
```
@claude we discovered Arizona doesn't observe DST. Please add a requirement to handle non-DST timezones to the PRD and create a ticket for it.
```

---

### Section 12: GitHub Actions (Scheduled)

**Show this workflow (add to repo):** `.github/workflows/daily-sync.yml`
```yaml
name: Daily Status Sync
on:
  schedule:
    - cron: '0 8 * * *'  # 8am daily
  workflow_dispatch:  # Manual trigger for demo

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Run the linear-status-sync.py script to fetch ticket statuses
            from Linear and update docs/prd.md with the current status table.
```

**Show:** `linear-status-sync.py` script

**Explain:** Claude calls Linear API directly (not MCP) in GitHub runners

---

## THINGS CREATED DURING DEMO

| What | Section | Where |
|------|---------|-------|
| UXR Survey | 3 | Google Docs |
| Image Generation Skill | 4 | `.claude/skills/image-generation/` |
| PRD | 5 | Google Docs |
| User Journey Map | 5 | `outputs/` folder |
| Notification Hook | 6 | `.claude/settings.json` |
| Slides | 6 | Local file |
| Updated PRD | 8 | Google Docs |
| Linear Tickets | 9 | Linear |
| PRD with ticket table | 10 | Google Docs |
| GitHub Issue | 11 | GitHub |
| New Linear Ticket (DST) | 11 | Linear |

---

## DISCONNECT BEFORE DEMO

To show MCP installation live, disconnect Linear first:

```bash
# Edit ~/.claude.json and remove the "linear" entry from mcpServers
# Or just start fresh session without it configured
```
