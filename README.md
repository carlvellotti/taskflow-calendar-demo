# Episode Demo Files

Demo files for the "Advanced Claude Code for PMs" video episode.

## Setup Instructions

### 1. Local Files
All local files are ready to use. Copy this folder to your demo location.

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
- Import from `data/survey-responses.csv`
- Or copy the data manually from `data/survey-responses.json`

**Google Doc: "Stakeholder Meeting Notes"**
- Copy content from `data/stakeholder-meeting-notes-content.md`

### 5. Linear Setup
- Create project: "TaskFlow Calendar Integration"
- Ensure your Linear MCP is connected: `npx -y mcp-remote https://mcp.linear.app/mcp`

### 6. Skills
The Research Synthesis skill is pre-installed at `.claude/skills/research-synthesis/`

### 7. GitHub Setup (for Sections 11-12)
- Create a repo for the demo
- Install Claude GitHub Action
- Copy `docs/prd.md` to the repo

## File Structure

```
episode-demo/
├── README.md                 # This file
├── feature-context.md        # Feature 1-pager (Section 3)
├── survey-template.md        # Survey template (Section 3)
├── image_gen.py              # Gemini image generation (Section 5)
├── linear-status-sync.py     # Linear API script (Section 12)
├── hooks-diagram.html        # Visual hooks reference (Section 6)
├── .env.example              # Environment template
├── data/
│   ├── survey-responses.csv          # Survey data for Google Sheets import
│   ├── survey-responses.json         # Survey data (JSON reference)
│   └── stakeholder-meeting-notes-content.md  # Content for Google Doc
├── docs/
│   └── prd.md                # PRD template for GitHub repo
├── outputs/                  # Generated images go here
└── .claude/
    └── skills/
        └── research-synthesis/
            └── SKILL.md      # Research synthesis skill
```

## Demo Flow Reference

| Section | Files Used |
|---------|------------|
| 3. Draft Survey | feature-context.md, survey-template.md |
| 4. Synthesize Research | Google Sheet (survey responses), Research Synthesis skill |
| 5. Draft PRD | image_gen.py, outputs/ |
| 7-8. Stakeholder Feedback | Google Doc (meeting notes) |
| 11-12. GitHub Actions | docs/prd.md, linear-status-sync.py |
