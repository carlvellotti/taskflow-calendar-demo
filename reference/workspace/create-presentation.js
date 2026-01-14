const pptxgen = require('pptxgenjs');
const path = require('path');
const html2pptx = require('/Users/carl/.claude/plugins/cache/anthropic-agent-skills/document-skills/f23222824449/skills/pptx/scripts/html2pptx.js');

async function createPresentation() {
    const pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9';
    pptx.author = 'TaskFlow Product Team';
    pptx.title = 'Calendar Integration PRD';
    pptx.subject = 'Product Requirements Document';

    const slidesDir = path.join(__dirname, 'slides');

    // Slide 1: Title
    await html2pptx(path.join(slidesDir, 'slide01-title.html'), pptx);

    // Slide 2: Problem & Opportunity
    await html2pptx(path.join(slidesDir, 'slide02-problem.html'), pptx);

    // Slide 3: Success Metrics
    await html2pptx(path.join(slidesDir, 'slide03-metrics.html'), pptx);

    // Slide 4: User Research
    await html2pptx(path.join(slidesDir, 'slide04-research.html'), pptx);

    // Slide 5: User Segments
    await html2pptx(path.join(slidesDir, 'slide05-segments.html'), pptx);

    // Slide 6: MVP Scope
    await html2pptx(path.join(slidesDir, 'slide06-mvp.html'), pptx);

    // Slide 7: Roadmap
    await html2pptx(path.join(slidesDir, 'slide07-roadmap.html'), pptx);

    // Slide 8: Technical Architecture
    await html2pptx(path.join(slidesDir, 'slide08-architecture.html'), pptx);

    // Slide 9: Risks & Mitigations
    await html2pptx(path.join(slidesDir, 'slide09-risks.html'), pptx);

    // Slide 10: Launch Plan
    await html2pptx(path.join(slidesDir, 'slide10-launch.html'), pptx);

    // Slide 11: Open Questions
    await html2pptx(path.join(slidesDir, 'slide11-questions.html'), pptx);

    // Slide 12: Competitive Advantage with table
    const { slide: slide12, placeholders } = await html2pptx(path.join(slidesDir, 'slide12-competitive.html'), pptx);

    // Add comparison table
    const tableData = [
        [
            { text: 'Feature', options: { fill: { color: '277884' }, color: 'FFFFFF', bold: true, align: 'center' } },
            { text: 'TaskFlow', options: { fill: { color: '277884' }, color: 'FFFFFF', bold: true, align: 'center' } },
            { text: 'Jira', options: { fill: { color: '277884' }, color: 'FFFFFF', bold: true, align: 'center' } },
            { text: 'Asana', options: { fill: { color: '277884' }, color: 'FFFFFF', bold: true, align: 'center' } }
        ],
        ['Google Calendar', { text: 'MVP', options: { color: '5EA8A7', bold: true } }, 'Yes', 'Yes'],
        ['Outlook', { text: 'Phase 2', options: { color: '666666' } }, 'Yes', 'Yes'],
        ['Two-way Sync', { text: 'Phase 2', options: { color: '666666' } }, 'No', 'Yes'],
        ['Team Calendar', { text: 'Phase 2', options: { color: '666666' } }, 'Yes', 'Yes'],
        ['Custom Filters', { text: 'MVP', options: { color: '5EA8A7', bold: true } }, 'Limited', 'Limited'],
        ['Focus Time Blocking', { text: 'Phase 3', options: { color: 'FE4447', bold: true } }, 'No', 'No']
    ];

    if (placeholders.length > 0) {
        slide12.addTable(tableData, {
            x: placeholders[0].x,
            y: placeholders[0].y,
            w: placeholders[0].w,
            h: placeholders[0].h,
            colW: [2, 1.8, 1.5, 1.5],
            border: { pt: 1, color: 'CCCCCC' },
            align: 'center',
            valign: 'middle',
            fontSize: 11,
            fontFace: 'Arial'
        });
    }

    // Save presentation
    const outputPath = path.join(__dirname, 'TaskFlow-Calendar-Integration-PRD.pptx');
    await pptx.writeFile({ fileName: outputPath });
    console.log('Presentation created:', outputPath);
}

createPresentation().catch(console.error);
