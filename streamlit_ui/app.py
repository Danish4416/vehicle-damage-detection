import streamlit as st
import requests

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader(
    "Upload the file",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded File",
        width="stretch"
    )

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    response = requests.post(
        "https://vehicle-damage-detection-78bv.onrender.com/predict",
        files=files
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Class: {result['prediction']}")
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")