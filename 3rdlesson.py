import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="Smart photo editor",
                   page_icon="https://img.magnific.com/free-psd/black-dslr-camera-with-lens_530521-1824.jpg?semt=ais_hybrid&w=740&q=80",
                   layout="wide")

st.title("Smart photo editor")
st.write("Load your photo and show us your image!")

st.sidebar.header("User Input")

uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_array = np.array(image)

    col1, col2 = st.columns(2)
    with col1:
        st.header("Original Image")
        st.image(image_array , width="stretch")

    filter_option = st.sidebar.selectbox(
        "Choose the filter you like:",
        ["Original", "Monochrome", "Brightness", "Inversion", "Contrast", "Blur","Sketch", "Flip"]
    )

    processed_img = image_array.copy()

    if filter_option == "Monochrome":
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    elif filter_option == "Brightness":
        processed_img = cv2.convertScaleAbs(image_array, alpha=1.0, beta=50)

    elif filter_option == "Contrast":
        processed_img = cv2.convertScaleAbs(image_array, alpha=1.7, beta=0)

    elif filter_option == "Blur":
        processed_img = cv2.GaussianBlur(image_array, (15,15), 0)

    elif filter_option == "Inversion":
        processed_img = 255 - image_array

    elif filter_option == "Sketch":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        inverted = 255 - gray
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

        sketch = cv2.divide(gray, 255 - blurred, scale=256.0)

    elif filter_option == "Flip":
        processed_img = cv2.flip(image_array, 1)
        st.image(processed_img, caption="Flipped Image")




    with col2:
        st.header("Processed Image")
        st.image(processed_img, width="stretch")

        buf = io.BytesIO()

        result_image = Image.fromarray(processed_img).convert("RGB")
        result_image.save(buf, format="JPEG")

        result_image.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download the image",
            data=byte_im,
            file_name="result.jpeg",
            mime="image/jpeg"
        )
