import streamlit as st
import fitz  # PyMuPDF
import io

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="PDF Previewer",
    page_icon="📄",
    layout="centered"
)

# --- App Title and Description ---
st.title("📄 PDF Uploader, Previewer, and Downloader")
st.write("Upload a PDF file to see a preview of its pages and download it back.")

# --- PDF File Uploader ---
uploaded_file = st.file_uploader(
    "Choose a PDF file", 
    type="pdf",
    help="Upload a PDF to view and download it."
)

# --- Main Logic ---
if uploaded_file is not None:
    # Read the file into a bytes object
    file_bytes = uploaded_file.getvalue()
    
    st.success(f"Successfully uploaded '{uploaded_file.name}'! 🎉")

    # --- Download Button ---
    # Placed here so you can download immediately after uploading
    st.download_button(
        label="⬇️ Download PDF",
        data=file_bytes,
        file_name=uploaded_file.name,
        mime="application/pdf",
    )
    
    st.markdown("---") # Visual separator

    # --- PDF Preview Section ---
    st.subheader("PDF Preview")
    
    try:
        # Open PDF file from bytes
        pdf_doc = fitz.open(stream=file_bytes, filetype="pdf")
        
        # Check if the PDF has pages
        if pdf_doc.page_count > 0:
            # Add a slider to navigate pages
            page_num = st.slider(
                "Select a page to view", 
                1, 
                pdf_doc.page_count, 
                1,
                help=f"This PDF has {pdf_doc.page_count} pages."
            )
            
            # Load the selected page (page numbers are 0-indexed in PyMuPDF)
            page = pdf_doc.load_page(page_num - 1)
            
            # Get the page as an image (pixmap)
            # You can increase the dpi for higher resolution
            pix = page.get_pixmap(dpi=150)
            
            # Convert the pixmap to a bytes object to display with st.image
            img_bytes = pix.tobytes("png")
            
            # Display the page image
            st.image(
                img_bytes, 
                caption=f"Page {page_num} of {pdf_doc.page_count}", 
                use_column_width=True
            )
        else:
            st.warning("This PDF file has no pages to display.")
            
        # Close the document
        pdf_doc.close()
        
    except Exception as e:
        st.error(f"An error occurred while trying to preview the PDF: {e}")
        st.info("The file might be corrupted, password-protected, or in an unsupported format.")

else:
    st.info("☝️ Upload a PDF file to get started.")
