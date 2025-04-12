import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO
import textwrap

st.set_page_config(page_title="Text to PDF Converter", layout="centered")

st.title("📝 Text to PDF Converter")
st.write("Enter your text below and click the button to download a PDF.")

text_input = st.text_area("Enter your text here:", height=300)

def generate_pdf(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    width, height = 595, 842  # A4 size in points
    margin = 50
    y = height - margin
    max_line_length = 100  # Adjust for line wrap

    for paragraph in text.split('\n'):
        wrapped_lines = textwrap.wrap(paragraph, width=max_line_length)
        for line in wrapped_lines:
            c.drawString(margin, y, line)
            y -= 15
            if y < margin:
                c.showPage()
                y = height - margin
        y -= 10  # Space between paragraphs

    c.save()
    buffer.seek(0)
    return buffer

if st.button("Convert to PDF"):
    if text_input.strip() == "":
        st.warning("Please enter some text before generating PDF.")
    else:
        pdf_data = generate_pdf(text_input)
        st.success("PDF successfully created!")
        st.download_button(
            label="📥 Download PDF",
            data=pdf_data,
            file_name="converted_text.pdf",
            mime="application/pdf"
        )
