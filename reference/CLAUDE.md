# TaskFlow Calendar Demo

## Project Overview

Demo project for Advanced Claude Code features, including AI-powered image generation.

## Image Generation

This project includes `image_gen.py` for AI image generation using Gemini. Key functions:

- `generate(prompt)` - Generate or refine an image
- `new_session()` - Clear session, start fresh
- `session_info()` - Show current session status
- `revert(turns=1)` - Undo last N turns

Generated images are saved to `outputs/` directory.

## Skills

### /pm-diagrams

Generate professional diagrams for product managers:

- **User Journey Maps** - Visualize customer experiences across touchpoints
- **Technical Architecture Diagrams** - System design and component layouts

Usage: `/pm-diagrams [your request]`

Examples:
- `/pm-diagrams user journey for new user onboarding`
- `/pm-diagrams architecture diagram for microservices backend`

See `.claude/skills/pm-diagrams.md` for full documentation.
