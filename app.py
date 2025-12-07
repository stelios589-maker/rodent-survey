import streamlit as st
from datetime import datetime
import os
from PIL import Image
import img2pdf
import base64
from io import BytesIO

st.set_page_config(page_title="Rodent Survey", layout="centered")
st.title("🐀 Rodent Activity Survey")
st.caption("For Brighter Image jobs — fill once per store")

# === INPUTS ===
col1, col2 = st.columns(2)
store_code = col1.text_input("Store Code + Number", placeholder="LW-13876 or HD-5501", value="")
jo_number = col2.text_input("JO #", placeholder="550123")

date = st.date_input("Survey Date", datetime.today())

with st.expander("Rodent Evidence Questions", expanded=True):
    q1 = st.radio("1. Rodent droppings observed?", ["No", "Yes - few", "Yes - moderate", "Yes - heavy"])
    q2 = st.radio("2. Gnaw marks on product/packaging?", ["No", "Yes"])
    q3 = st.radio("3. Burrows or runways visible?", ["No", "Yes"])
    q4 = st.radio("4. Live rodents observed?", ["No", "Yes"])
    q5 = st.radio("5. Dead rodents found?", ["No", "Yes"])
    q6 = st.number_input("Number of bait stations checked", min_value=0, step=1)
    q7 = st.number_input("Number of bait stations consumed/missing", min_value=0, step=1)
    q8 = st.text_area("Additional notes / recommendations")

st.write("### Photos (take with phone camera)")
uploaded_photos = st.file_uploader("Take or upload photos", type=["png","jpg","jpeg","heic"], accept_multiple_files=True)

tech_signature = st.text_input("Technician Signature (type your name to sign)")
tech_name = st.text_input("Technician Name")
tech_name = st.text_input("Technician Name")

if st.button("Generate PDF Report", type="primary"):
    if not store_code or not jo_number or not tech_name:
        st.error("Please fill Store Code, JO #, and Technician Name")
    else:
        with st.spinner("Building PDF…"):
            # Create text content
            text = f"""
RODENT ACTIVITY SURVEY REPORT
Store: {store_code}
JO #: {jo_number}
Date: {date}
Technician: {tech_name}

EVIDENCE FOUND:
1. Droppings: {q1}
2. Gnaw marks: {q2}
3. Burrows/runways: {q3}
4. Live rodents: {q4}
5. Dead rodents: {q5}
6. Bait stations checked: {q6}
7. Bait stations consumed/missing: {q7}
Additional notes:
{q8}

Technician signature:
"""
            images = []
            if uploaded_photos:
                for up in uploaded_photos:
                    img = Image.open(up)
                    buffered = BytesIO()
                    img.save(buffered, format="JPEG")
                    images.append(buffered.getvalue())

            # Signature
            if signature.image_data is not None:
                sig_img = Image.fromarray(signature.image_data.astype("uint8"))
                sig_buffer = BytesIO()
                sig_img.save(sig_buffer, format="PNG")
                images.append(sig_buffer.getvalue())

            # Build PDF
            pdf_bytes = img2pdf.convert([BytesIO(text.encode("utf-8"))] + images)

            b64 = base64.b64encode(pdf_bytes).decode()
            filename = f"Rodent_Survey_{store_code}_{jo_number}_{date}.pdf"
            href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF Report Now</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("Report ready! Download and send to Brighter Image")
