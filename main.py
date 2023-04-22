# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from converter import img_converter

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image to img_converter to get the grayscale version
    gray_img = img_converter(camera_image)
    st.image(gray_img)

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    gray_uploaded_img = img_converter(uploaded_image)
    st.image(gray_uploaded_img)
