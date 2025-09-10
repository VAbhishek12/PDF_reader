import streamlit as st

st.set_page_config(page_title="PDF Viewer", layout="centered")
st.title("📄 PDF Uploader, Viewer & Downloader")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Download button
    st.download_button(
        label="⬇️ Download PDF",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime="application/pdf"
    )

    # Display PDF directly
    st.pdf(uploaded_file)
else:
    st.info("👆 Upload a PDF to view and download it.")
