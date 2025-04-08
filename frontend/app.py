import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.plant_id_api import identify_plant
from backend.trefle_api import get_plant_care_info
import pandas as pd

st.set_page_config(page_title="Smart Plant Care Assistant", layout="wide")
st.title("🌿 Smart Plant Care Assistant")

uploaded_image = st.file_uploader("📤 Upload a plant image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(uploaded_image, caption="🖼️ Uploaded Plant Image", use_column_width=True)

    with col2:
        st.subheader("🔍 Identification Results")
        name, confidence, scientific = identify_plant(uploaded_image)
        st.success(f"**Common Name**: {name}")
        st.info(f"**Scientific Name**: {scientific}")
        st.write(f"**Confidence**: {confidence}%")

        st.subheader("🪴 Plant Care Info (via Trefle API)")
        trefle_common, trefle_sci, care_details = get_plant_care_info(name)
        st.write(f"**Trefle Common Name**: {trefle_common}")
        st.write(f"**Trefle Scientific Name**: {trefle_sci}")
        st.write(f"**Care Info**:\n{care_details}")

st.divider()

st.subheader("📣 Give Feedback")
with st.form("feedback_form"):
    feedback = st.text_area("Your thoughts about this app:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        df = pd.DataFrame([[feedback]], columns=["Feedback"])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)
        st.success("✅ Feedback submitted!")
