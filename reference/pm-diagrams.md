# PM Diagram Generator

Generate professional user journey maps and technical architecture diagrams for product managers using AI image generation.

## Usage

Invoke this skill with `/pm-diagrams` followed by your request:
- `/pm-diagrams user journey for checkout flow`
- `/pm-diagrams architecture for auth system`

## How It Works

This skill uses the `image_gen.py` module to generate diagrams. Run Python code like:

```python
from image_gen import generate, new_session

new_session()  # Start fresh
result = generate(prompt, aspect_ratio="16:9")  # Wide format for diagrams
```

## Diagram Types

### User Journey Maps

For user journeys, structure the prompt with:

1. **Title**: Clear journey name
2. **Persona**: Who is the user
3. **Stages**: 4-6 horizontal stages (Awareness → Consideration → Action → Retention)
4. **Touchpoints**: User actions at each stage
5. **Emotions**: Pain points and delights
6. **Opportunities**: Improvement areas

**Example prompt template for user journeys:**
```
Create a professional user journey map infographic.

Title: "[JOURNEY NAME]"
Persona: [USER TYPE]

Layout: Horizontal flow with 5 stages

Stages (left to right):
1. [STAGE 1] - [Key action] - Emotion: [emoji]
2. [STAGE 2] - [Key action] - Emotion: [emoji]
3. [STAGE 3] - [Key action] - Emotion: [emoji]
4. [STAGE 4] - [Key action] - Emotion: [emoji]
5. [STAGE 5] - [Key action] - Emotion: [emoji]

Include:
- Touchpoints as icons below each stage
- Emotion curve line showing user sentiment
- Pain points highlighted in red
- Opportunities highlighted in green

Style: Clean, professional, white background, blue/purple accent colors,
modern sans-serif fonts, minimal icons, business presentation quality.
```

### Technical Architecture Diagrams

For architecture diagrams, structure the prompt with:

1. **Title**: System name
2. **Layers**: Frontend, Backend, Data, Infrastructure
3. **Components**: Services, databases, APIs
4. **Connections**: Data flow arrows
5. **Labels**: Clear component names

**Example prompt template for architecture:**
```
Create a clean technical architecture diagram.

Title: "[SYSTEM NAME] Architecture"

Layout: Layered diagram with clear separation

Layers (top to bottom):
- Client Layer: [Web App, Mobile App, etc.]
- API Layer: [API Gateway, Load Balancer]
- Service Layer: [Service 1, Service 2, Service 3]
- Data Layer: [Database, Cache, Storage]
- Infrastructure: [Cloud provider, CDN]

Show:
- Arrows indicating data flow direction
- Clear boxes for each component
- Icons representing each service type
- Color coding by layer (blue=client, green=services, orange=data)

Style: Technical diagram aesthetic, white background, clean lines,
monospace labels, professional cloud architecture style, no 3D effects.
```

## Aspect Ratios

- **16:9** - Best for architecture diagrams and presentations
- **4:3** - Good for detailed journey maps
- **1:1** - Square format for social sharing

## Workflow Tips

1. **Start fresh**: Always call `new_session()` for a new diagram
2. **Iterate**: Use `generate()` again to refine - the model remembers context
3. **Be specific**: More detail in prompts = better results
4. **Check output**: Review at `outputs/output_XXX_XXXXXX.png`

## Quick Commands

```python
# User Journey
from image_gen import generate, new_session
new_session()
generate("""
Create a user journey map for [YOUR FLOW].
Stages: [STAGE1] → [STAGE2] → [STAGE3] → [STAGE4]
Show touchpoints, emotions, and pain points.
Style: Professional, clean, horizontal flow.
""", aspect_ratio="16:9")

# Architecture Diagram
from image_gen import generate, new_session
new_session()
generate("""
Create a technical architecture diagram for [YOUR SYSTEM].
Components: [FRONTEND] → [API] → [SERVICES] → [DATABASE]
Show data flow with arrows.
Style: Clean technical diagram, layered layout.
""", aspect_ratio="16:9")
```

## Session Management

- `new_session()` - Clear and start fresh
- `session_info()` - Check current session status
- `revert(turns=1)` - Undo last generation to try again
