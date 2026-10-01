from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_pdf(overview, insights):
    """
    Generates a PDF business report.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Business Analytics Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Dataset Overview</b>", styles["Heading2"]))

    story.append(Paragraph(f"Rows: {overview['rows']}", styles["Normal"]))
    story.append(Paragraph(f"Columns: {overview['columns']}", styles["Normal"]))
    story.append(Paragraph(f"Missing Values: {overview['missing']}", styles["Normal"]))
    story.append(Paragraph(f"Duplicate Rows: {overview['duplicates']}", styles["Normal"]))
    story.append(Paragraph(f"Memory Usage: {overview['memory']} MB", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Business Insights</b>", styles["Heading2"]))

    for insight in insights:
        story.append(Paragraph(f"• {insight}", styles["Normal"]))

    doc.build(story)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf