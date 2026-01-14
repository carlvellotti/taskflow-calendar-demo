# Advanced Claude Code for PMs - Demo Files

Demo files for the ["Advanced Claude Code for PMs" video episode](https://www.youtube.com/watch?v=59gy_24KIVE) with Aakash Gupta.

## Folder Structure

```
├── start/          ← START HERE to follow along with the video
├── reference/      ← Finished outputs from the demo (for reference)
└── (root files)    ← Config & setup files
```

### `start/` - Beginning of the Lesson
Copy these files to follow along with the video from the beginning. Contains:
- Survey data (CSV/JSON)
- Stakeholder meeting notes
- Feature context document
- Survey template
- Research Synthesis skill
- Python scripts for image generation & Linear sync

### `reference/` - Finished Outputs
The completed artifacts I created during the demo:
- Final PRD (`calendar-integration-prd.md`)
- Survey synthesis document
- Journey map image
- Full slide deck (HTML + PowerPoint)
- CLAUDE.md with project context

Use these to compare your work or see what the end result should look like.

---

## Setup Instructions

### 1. Copy Start Files
```bash
# Clone this repo
git clone https://github.com/carlvellotti/taskflow-calendar-demo.git
cd taskflow-calendar-demo

# Copy start files to your working directory
cp -r start/* .
```

### 2. Environment Variables
```bash
cp .env.example .env
# Edit .env and add your API keys:
# - GEMINI_API_KEY: Get from https://aistudio.google.com/apikey
# - LINEAR_API_KEY: Get from https://linear.app/settings/api
```

### 3. Python Dependencies
```bash
pip install google-genai pillow python-dotenv
```

### 4. Google Workspace Setup
Create these assets in Google Drive:

**Google Sheet: "Calendar Integration Survey Responses"**
- Import from `start/data/survey-responses.csv`

**Google Doc: "Stakeholder Meeting Notes"**
- Copy content from `start/data/stakeholder-meeting-notes-content.md`

### 5. Linear Setup
- Create project: "TaskFlow Calendar Integration"
- Connect Linear MCP: `npx -y mcp-remote https://mcp.linear.app/mcp`

### 6. GitHub Setup (for Sections 11-12)
- Create a repo for the demo
- Install Claude GitHub Action
- Copy `start/docs/prd.md` to the repo

---

## Video Timestamps

| Time | Section | Files Used |
|------|---------|------------|
| 11:04 | Setting Up Linear MCP | - |
| 14:07 | Essential MCP Stack | - |
| 21:25 | End-to-End PM Workflow | feature-context.md, survey-template.md |
| 28:00 | Skills Introduction | .claude/skills/ |
| 38:00 | Image Generation | image_gen.py |
| 44:12 | Creating PRD from Survey | Google Sheet, Research Synthesis skill |
| 51:00 | Hooks Feature | hooks-diagram.html |
| 55:30 | Creating Presentation | workspace/slides/ |
| 1:01:49 | Creating Linear Tickets | Linear MCP |
| 1:08:08 | GitHub Integration | docs/prd.md, linear-status-sync.py |

---

## Questions?

- Video: https://www.youtube.com/watch?v=59gy_24KIVE
- Carl on LinkedIn: https://linkedin.com/in/carlvellotti
- Carl on Twitter/X: https://x.com/carlvellotti
