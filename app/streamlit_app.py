import streamlit as st
from classify_tool import classify_image
import tempfile

st.title("Oil Quality Classifier")
st.markdown("Upload an oil drop image to classify its quality stage (1 to 5).")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.image(tmp_path, caption="Uploaded Image", use_column_width=True)
    result = classify_image(tmp_path)
    st.success(result)
