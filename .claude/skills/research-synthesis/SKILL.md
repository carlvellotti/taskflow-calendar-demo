---
name: research-synthesis
description: Use this skill when analyzing user research data, synthesizing survey responses, customer feedback, interview notes, or any qualitative research data. Triggers on requests to "analyze", "synthesize", or "find patterns" in user research.
---

# Research Synthesis Skill

Transform raw user research data into actionable insights using a structured framework.

## When to Use

- Analyzing survey responses
- Synthesizing customer interview notes
- Finding patterns in feedback data
- Summarizing user research findings
- Creating research reports

## Output Framework

When synthesizing research, always structure your output as follows:

### 1. Executive Summary
- 2-3 sentence overview of key findings
- The single most important insight

### 2. Key Themes
For each theme identified:
- **Theme Name**: Clear, descriptive label
- **Frequency**: How many responses mentioned this (e.g., "12 of 20 respondents")
- **Representative Quotes**: 2-3 direct quotes that exemplify this theme
- **Implications**: What this means for the product/feature

### 3. Quantitative Patterns
- Summary statistics (if applicable)
- Distribution of responses
- Notable segments or groupings

### 4. Recommendations
- Prioritized list of actions based on findings
- Each recommendation tied to specific evidence
- Clear "must have" vs "nice to have" distinction

### 5. Open Questions
- Areas needing further research
- Conflicting signals that need resolution
- Assumptions to validate

## Best Practices

1. **Quote liberally** — Let users speak in their own words
2. **Quantify when possible** — "Many users" → "14 of 20 users (70%)"
3. **Distinguish facts from interpretation** — Be clear about what's data vs inference
4. **Surface surprises** — Highlight unexpected findings
5. **Note limitations** — Sample size, selection bias, etc.

## Example Output Structure

```markdown
## Executive Summary
Users overwhelmingly want [X], but have concerns about [Y]. The most critical finding is [Z].

## Key Themes

### Theme 1: [Name] (mentioned by X of Y respondents)
> "Direct quote from user..."
> "Another supporting quote..."

**Implication**: This suggests we should...

### Theme 2: [Name] (mentioned by X of Y respondents)
...

## Quantitative Patterns
- 75% of respondents rated [feature] as "very important"
- Power users (5+ hours/week) were 2x more likely to request [X]

## Recommendations
1. **Must Have**: [Recommendation] — Based on [evidence]
2. **Should Have**: [Recommendation] — Based on [evidence]
3. **Could Have**: [Recommendation] — Based on [evidence]

## Open Questions
- Do enterprise users have different needs? (only 3 in sample)
- How does this compare to competitor offerings?
```
