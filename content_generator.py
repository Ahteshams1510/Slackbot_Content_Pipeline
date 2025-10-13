# ---------------------------------------------------------
# File: content_generator.py
# Author: Ahtesham Shaikh
# Description: Part of AI Engineer Assignment – Slackbot Content Pipeline
# ---------------------------------------------------------

# content_generator.py
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime
import os

def generate_report(topic_text, output_dir="outputs"):
    """
    Create a simple PDF report that summarizes the requested topic_text.
    This is a local (mock) AI-style report generator for assignment demo.
    Returns the path to the generated PDF.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Build a simple mock summary (you can replace this with real AI later)
    now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"AI_Report_{now}.pdf"
    output_path = os.path.join(output_dir, filename)

    # Create PDF
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    title = f"Automated Content Report"
    story.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    story.append(Spacer(1, 12))

    story.append(Paragraph(f"<b>Topic:</b> {topic_text}", styles['Heading3']))
    story.append(Spacer(1, 8))

    # Mock "AI" summary paragraphs (simple programmatic summary)
    summary = (
        f"This report provides a concise overview and recommended talking points about: {topic_text}. "
        "The following points are programmatically derived as a mock summary for the assignment demonstration."
    )
    story.append(Paragraph(summary, styles['Normal']))
    story.append(Spacer(1, 8))

    bullets = [
        "Key trend 1: Rapid advancement and adoption.",
        "Key trend 2: Practical business use-cases and ROI focus.",
        "Key trend 3: Implementation challenges and data needs.",
        "Recommendation: Start with pilot projects and measure impact."
    ]
    for b in bullets:
        story.append(Paragraph(f"• {b}", styles['Normal']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))

    doc.build(story)
    return output_path
