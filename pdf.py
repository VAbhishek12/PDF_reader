import streamlit as st
import tempfile
import streamlit.components.v1 as components

st.set_page_config(page_title="PDF Viewer", layout="centered")
st.title("📄 PDF Uploader, Viewer & Downloader")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        temp_path = tmp_file.name

    # Download button
    st.download_button(
        label="⬇️ Download PDF",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime="application/pdf"
    )

    # Show PDF using Google Docs Viewer
    gdoc_viewer = f"""
    <iframe src="https://docs.google.com/viewer?url=file://{temp_path}&embedded=true" 
    width="700" height="500" style="border: none;"></iframe>
    """
    components.html(gdoc_viewer, height=600, scrolling=True)
else:
    st.info("👆 Upload a PDF to view and download it.")
