import streamlit as st
from datetime import datetime
from PIL import Image
from fpdf import FPDF
from io import BytesIO
import base64

st.set_page_config(page_title="Brighter Image Rodent Survey", layout="wide")
st.title("Brighter Image Rodent Survey")
st.caption("Complete every section – matches the official 8-page form exactly")

# === HEADER ===
c1, c2, c3 = st.columns(3)
store = c1.text_input("Store Code + Number", placeholder="LW-13876", key="store")
jo = c2.text_input("JO #", placeholder="550123", key="jo")
date = c3.date_input("Date", datetime.today(), key="date")
tech = st.text_input("Technician Name", key="tech")
sig = st.text_input("Technician Signature (type name)", key="sig")

# === STEP 1 ===
with st.expander("Step 1 – Perimeter of the Store", expanded=True):
    st.markdown("**Take 6–8 photos of the general perimeter**")
    p1_1 = st.file_uploader("General perimeter photos", ["jpg","jpeg","png","heic"], True, key="p1_1")
    st.markdown("**Take a photo of the trash compactor area**")
    p1_2 = st.file_uploader("Trash compactor area", ["jpg","jpeg","png","heic"], True, key="p1_2")
    st.markdown("**Photograph each entrance – inside and outside**")
    p1_3 = st.file_uploader("Entrances inside/outside", ["jpg","jpeg","png","heic"], True, key="p1_3")
    st.markdown("**Photograph the rubber gaskets underneath each set of doors**")
    p1_4 = st.file_uploader("Rubber gaskets", ["jpg","jpeg","png","heic"], True, key="p1_4")

    gasket_gaps = st.radio("Gaps/holes in rubber gaskets?", ("Yes", "No"), horizontal=True, key="gasket_gaps")
    if gasket_gaps == "Yes":
        st.text_area("Which entrances?", key="gasket_which")
    
    bait_4 = st.radio("Each entrance has 4 bait boxes (2 in / 2 out)?", ("Yes", "No"), horizontal=True, key="bait4")
    if bait_4 == "No":
        st.text_area("Which entrances are missing boxes?", key="bait_missing")

    st.markdown("### Sources that may attract rodents")
    food = st.radio("Food (dumpster, fast food, etc.)", ("Yes", "No"), horizontal=True, key="food")
    if food == "Yes": st.text_area("Food description", key="food_desc")
    water = st.radio("Water (pond, leaks, etc.)", ("Yes", "No"), horizontal=True, key="water")
    if water == "Yes": st.text_area("Water description", key="water_desc")
    shelter = st.radio("Shelter (hay, debris, etc.)", ("Yes", "No"), horizontal=True, key="shelter")
    if shelter_desc = st.text_area("Shelter description / hay trailer note", key="shelter_desc")

    exclusion = st.radio("Potential points of entry needing exclusion?", ("Yes", "No"), horizontal=True, key="exclusion")
    if exclusion == "Yes": st.text_area("Exclusion description", key="exclusion_desc")

