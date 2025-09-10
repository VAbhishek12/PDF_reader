import streamlit as st
import base64

st.set_page_config(page_title="PDF Viewer", layout="wide")
st.title("📄 PDF Uploader, Viewer & Downloader")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Read PDF as bytes
    pdf_bytes = uploaded_file.read()

    # --- Download button ---
    st.download_button(
        label="⬇️ Download PDF",
        data=pdf_bytes,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )

    # --- PDF Preview (base64 embedding works on Streamlit Cloud + Chrome) ---
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
else:
    st.info("👆 Upload a PDF to view and download it.")
