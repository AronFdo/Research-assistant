from fpdf import FPDF
from datetime import datetime
import os

def save_to_pdf(summary: str, analysis: str, query: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    sanitized_query = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in query)
    filename = f"reports/{sanitized_query.replace(' ', '_')}_{timestamp}.pdf"

    if not os.path.exists("reports"):
        os.makedirs("reports")

    pdf = FPDF()
    pdf.add_page()

    # Use a better supported Unicode font (DejaVuSans is a good alternative)
    font_path = "DejaVuSans.ttf"  # Make sure this path exists
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", "", 12)

    pdf.multi_cell(0, 10, f"📘 Summary for: {query}\n\n", align="L")
    pdf.multi_cell(0, 10, str(summary) + "\n\n", align="L")
    pdf.multi_cell(0, 10, "📝 Analysis:\n" + str(analysis), align="L")

    pdf.output(filename)
    return filename
