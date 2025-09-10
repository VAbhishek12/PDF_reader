import streamlit as st
import base64

st.set_page_config(page_title="PDF Viewer", layout="wide")
st.title("📄 PDF Upload, Preview & Download")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Read PDF and encode in base64
    pdf_bytes = uploaded_file.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    # Embed PDF.js viewer (more reliable than Chrome's preview)
    pdf_display = f"""
        <iframe
            src="https://mozilla.github.io/pdf.js/web/viewer.html?file=data:application/pdf;base64,{base64_pdf}"
            width="100%" height="600"
            style="border: none;"
        ></iframe>
    """
    st.components.v1.html(pdf_display, height=600, scrolling=True)

    # Reset file pointer for download
    uploaded_file.seek(0)

    # Download button
    st.download_button(
        label="📥 Download PDF",
        data=pdf_bytes,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )
