import streamlit as st
import os

st.set_page_config(page_title="PDF Viewer", layout="wide")
st.title("📄 PDF Uploader, Viewer & Downloader")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Show download button
    st.download_button(
        label="⬇️ Download PDF",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime="application/pdf"
    )

    # Embed PDF.js to display the file
    pdf_viewer = f"""
    <iframe
        src="https://mozilla.github.io/pdf.js/web/viewer.html?file=temp.pdf"
        width="100%" height="600"
        style="border: none;"
    ></iframe>
    """
    st.markdown(pdf_viewer, unsafe_allow_html=True)
else:
    st.info("👆 Upload a PDF to view and download it.")
