import streamlit as st
from datetime import datetime
from PIL import Image
import img2pdf
import base64
from io import BytesIO

st.set_page_config(page_title="Rodent Survey", layout="centered")
st.title("Rodent Activity Survey")
st.caption("Brighter Image – fill once per store")

# --- INPUTS ---
c1, c2 = st.columns(2)
store_code = c1.text_input("Store Code + Number", placeholder="LW-13876 or HD-5501")
jo_number = c2.text_input("JO #", placeholder="550123")

survey_date = st.date_input("Survey Date", datetime.today())

with st.expander("Rodent Evidence Questions", expanded=True):
    q1 = st.radio("1. Rodent droppings observed?", ["No", "Yes - few", "Yes - moderate", "Yes - heavy"])
    q2 = st.radio("2. Gnaw marks on product/packaging?", ["No", "Yes"])
    q3 = st.radio("3. Burrows or runways visible?", ["No", "Yes"])
    q4 = st.radio("4. Live rodents observed?", ["No", "Yes"])
    q5 = st.radio("5. Dead rodents found?", ["No", "Yes"])
    q6 = st.number_input("Bait stations checked", min_value=0, step=1)
    q7 = st.number_input("Bait stations consumed/missing", min_value=0, step=1)
    q8 = st.text_area("Additional notes / recommendations")

st.write("### Photos")
photos = st.file_uploader("Take or upload photos of evidence", type=["png","jpg","jpeg","heic"], accept_multiple_files=True)

tech_name = st.text_input("Technician Name", key="tech")
tech_sig  = st.text_input("Technician Signature (type name to sign)", key="sig")

if st.button("Generate PDF Report", type="primary"):
    if not store_code or not jo_number or not tech_name:
        st.error("Store, JO#, and Technician Name are required")
    else:
        with st.spinner("Creating PDF…"):
            # Text content
            text = f"""
RODENT ACTIVITY SURVEY REPORT
Store: {store_code}          JO #: {jo_number}
Date: {survey_date}          Technician: {tech_name}

EVIDENCE FOUND
1. Droppings: {q1}
2. Gnaw marks: {q2}
3. Burrows/runways: {q3}
4. Live rodents: {q4}
5. Dead rodents: {q5}
6. Bait stations checked: {q6}
7. Consumed/missing: {q7}
Notes: {q8}

Technician signature: {tech_sig}
"""

            # Collect images
            img
