# ---------------------------------------------------------
# File: pdf_generator.py
# Author: Ahtesham Shaikh
# Description: Part of AI Engineer Assignment – Slackbot Content Pipeline
# ---------------------------------------------------------


from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import io

def build_pdf_report(cleaned, groups, outlines, ideas, output_path='report.pdf'):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph('<b>Content Research Report</b>', styles['Title']))
    story.append(Spacer(1,12))
    story.append(Paragraph('<b>Raw Keywords</b>', styles['Heading3']))
    story.append(Paragraph(', '.join(cleaned[:200]), styles['Normal']))
    story.append(Spacer(1,12))
    for gid, kws in groups.items():
        story.append(Paragraph(f'<b>Group {gid} - {len(kws)} keywords</b>', styles['Heading4']))
        story.append(Paragraph(', '.join(kws), styles['Normal']))
        story.append(Spacer(1,6))
        if gid in outlines:
            story.append(Paragraph('<b>Outline</b>', styles['Normal']))
            story.append(Paragraph(outlines[gid], styles['Normal']))
            story.append(Spacer(1,6))
        if gid in ideas:
            story.append(Paragraph('<b>Post Idea</b>', styles['Normal']))
            story.append(Paragraph(ideas[gid], styles['Normal']))
            story.append(Spacer(1,12))
    doc.build(story)
    return output_path
