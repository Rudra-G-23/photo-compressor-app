import streamlit as st
from PIL import Image
import io

st.set_page_config(
    page_title="🗜️ Photo Compressor", 
    layout="wide"
)
st.title("🗜️ Photo Compressor App")

# 🎈 Balloons on first load
if "first_load" not in st.session_state:
    st.session_state.first_load = True
    st.balloons()

uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    original_bytes = uploaded_file.getbuffer()
    original_size = len(original_bytes)

    # Compression slider
    quality = st.slider("🛠️ Select Compression Quality", 0, 100, 80, step=10)

    # Compress the image
    img_bytes_io = io.BytesIO()
    image.save(img_bytes_io, format="JPEG", quality=quality)
    img_bytes_io.seek(0)
    compressed_size = len(img_bytes_io.getvalue())

    # File size metrics
    col1, col2 = st.columns(2)
    col1.metric("📦 Original Size", f"{original_size / 1024:.2f} KB")
    col2.metric("📉 Compressed Size", f"{compressed_size / 1024:.2f} KB")

    # 🖼️ Small original image preview
    with st.expander("🖼️ Original Image"):
        st.image(image, caption="Original Image")

    # 🔍 Large Before/After comparison
    st.header("🔍 Compare Before and After")
    col1, col2 = st.columns(2)
    col1.image(image, caption="Before Compression", use_container_width=True)
    col2.image(Image.open(img_bytes_io), caption="After Compression", use_container_width=True)

    # 📥 Download button with 🎈
    if st.download_button(
        label="📥 Download Compressed Image",
        data=img_bytes_io,
        file_name="compressed_image.jpg",
        mime="image/jpeg"
    ):
        st.balloons()
