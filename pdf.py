import streamlit as st
import base64
import tempfile

st.set_page_config(page_title="PDF Viewer", layout="centered")
st.title("📄 PDF Uploader, Viewer & Downloader")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save to a temporary file
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

    # Display PDF preview
    with open(temp_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
else:
    st.info("👆 Upload a PDF to view and download it.")
