import streamlit as st
# from model_helper import predict
import requests
import time

API_URL = "http://127.0.0.1:8000/predict"
st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded File", width=400)
        # prediction = predict(image_path)
        # st.info(f"Predicted Class: **{prediction}**")
        with st.spinner("Processing..."):
         time.sleep(0.5)
         response = requests.post(API_URL, files={"file": uploaded_file})
       # Handle API response
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Class: **{result.get('prediction', 'Unknown')}**")
        else:
            st.error(f"Error: {response.text}")