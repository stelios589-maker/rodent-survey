import streamlit as st
from datetime import datetime
from PIL import Image
from fpdf import FPDF
import pillow_heif
from io import BytesIO
import base64

st.set_page_config(page_title="Rodent Survey", layout="wide")
st.title("Brighter Image Rodent Survey")
st.caption("Complete all steps for full report")

store_code = st.text_input("Store Code + Number", placeholder="LW-13876 or HD-5501")
jo_number = st.text_input("JO #", placeholder="550123")
survey_date = st.date_input("Survey Date", datetime.today())
tech_name = st.text_input("Technician Name", key="tech")
tech_sig = st.text_input("Technician Signature (type name to sign)", key="sig")

# Step 1: Perimeter
with st.expander("Step 1 - Inspect and Photograph the Entire Perimeter of the Store", expanded=True):
    photos_perimeter = st.file_uploader("Take 6-8 photos of the general perimeter", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p1_perimeter")
    photos_compactor = st.file_uploader("Take a photo of the trash compactor area", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p1_compactor")
    photos_entrances = st.file_uploader("Photograph each entrance - inside and outside", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p1_entrances")
    photos_gaskets = st.file_uploader("Photograph the rubber gaskets underneath each set of doors", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p1_gaskets")
    gaps_gaskets = st.radio("Are there gaps or holes in any of the rubber gaskets?", ("Yes", "No"))
    gaps_entrances = st.text_area("At which entrances?")
    bait_boxes = st.radio("Does each entrance have a total of 4 bait boxes (2 inside, 2 outside)?", ("Yes", "No"))
    missing_boxes = st.text_area("If not, indicate which entrances are missing bait boxes")
    food_source = st.radio("Food (ex. overflowing dumpster, nearby fast food restaurant)", ("Yes", "No"))
    food_desc = st.text_area("Description of food source")
    water_source = st.radio("Water (ex. nearby pond)", ("Yes", "No"))
    water_desc = st.text_area("Description of water source")
    shelter_source = st.radio("Shelter (ex. bales of hay)", ("Yes", "No"))
    shelter_desc = st.text_area("Description of shelter source (Note: If hay trailer present, take photos and note here)")
    exclusion_points = st.radio("Are there any potential points of entry that may need exclusion?", ("Yes", "No"))
    exclusion_desc = st.text_area("Description of exclusion points")
    rodents_from = st.text_area("Where might the rodents be coming from? (ex. Nearby drainage ditch, open sewage pipe, etc.)")

# Step 2: Outside Garden
with st.expander("Step 2 - Inspect and Photograph Outside Garden"):
    photos_nests = st.file_uploader("Take photos of plant table supports for nests", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p2_nests")
    nests_present = st.radio("Are there any rodent nests present?", ("Yes", "No"))
    nests_location = st.text_area("Where are the nests located?")
    photos_grease_top = st.file_uploader("Take 1-2 photos of the top of the racking along the CMU wall", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p2_grease_top")
    grease_stains = st.radio("Are there any grease stains present?", ("Yes", "No"))
    grease_desc = st.text_area("Describe grease stains, including Aisle and Bay numbers")
    rodents_running = st.radio("Do you see or hear any rodents running along the top of the walls or racking?", ("Yes", "No"))
    rodents_running_desc = st.text_area("Describe rodents running, including Aisle and Bay numbers")
    photos_racking_under = st.file_uploader("Inspect the racking in the Outside Garden - underneath the racking and behind product. Take 3-5 photos", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p2_racking")
    activity_racking = st.radio("Are there any signs of rodent activity? (ex. droppings, grease stains, debris)", ("Yes", "No"))
    activity_racking_desc = st.text_area("Describe racking activity, including Aisle and Bay numbers")
    photos_product = st.file_uploader("Inspect the product in the Outside Garden, especially flower pots and near food sources. Take 3-5 photos", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p2_product")
    activity_product = st.radio("Are there any signs of rodent activity?", ("Yes", "No"))
    activity_product_desc = st.text_area("Describe product activity, including Aisle and Bay numbers")
    photos_perimeter_og = st.file_uploader("Inspect the perimeter of the Outside Garden. Photograph all possible points of entry", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p2_perimeter")
    entry_points_og = st.text_area("Location and description of each possible entry point")
    associate_comments_og = st.text_area("Associate comments on rodent activity in Outside Garden")
    photos_associate_og = st.file_uploader("Take photos of areas mentioned by associate (Outside Garden)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p2_associate")
    additional_comments_og = st.text_area("Additional Comments/Observations (Outside Garden)")

# Step 3: HPE/Greenhouse
with st.expander("Step 3 - Inspect and Photograph Houseplant Enclosure (HPE)/Greenhouse"):
    photos_nests_hpe = st.file_uploader("Take photos of plant table supports for nests in HPE/Greenhouse", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p3_nests")
    nests_present_hpe = st.radio("Are there any rodent nests present in HPE/Greenhouse?", ("Yes", "No"))
    nests_location_hpe = st.text_area("Where are the nests located in HPE/Greenhouse?")
    photos_grease_top_hpe = st.file_uploader("Take 1-2 photos of the top of the racking along the CMU wall in HPE/Greenhouse", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p3_grease_top")
    grease_stains_hpe = st.radio("Are there any grease stains present in HPE/Greenhouse?", ("Yes", "No"))
    grease_desc_hpe = st.text_area("Describe grease stains in HPE/Greenhouse, including Aisle and Bay numbers")
    rodents_running_hpe = st.radio("Do you see or hear any rodents running along the top of the walls or racking in HPE/Greenhouse?", ("Yes", "No"))
    rodents_running_desc_hpe = st.text_area("Describe rodents running in HPE/Greenhouse, including Aisle and Bay numbers")
    photos_racking_under_hpe = st.file_uploader("Inspect the racking in the HPE/Greenhouse - underneath the racking and behind product. Take 3-5 photos", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p3_racking")
    activity_racking_hpe = st.radio("Are there any signs of rodent activity in HPE/Greenhouse racking?", ("Yes", "No"))
    activity_racking_desc_hpe = st.text_area("Describe racking activity in HPE/Greenhouse, including Aisle and Bay numbers")
    photos_product_hpe = st.file_uploader("Inspect the product in the HPE/Greenhouse, especially flower pots and near food sources. Take 3-5 photos", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p3_product")
    activity_product_hpe = st.radio("Are there any signs of rodent activity in HPE/Greenhouse product?", ("Yes", "No"))
    activity_product_desc_hpe = st.text_area("Describe product activity in HPE/Greenhouse, including Aisle and Bay numbers")
    photos_perimeter_hpe = st.file_uploader("Inspect the perimeter of the HPE/Greenhouse. Photograph all possible points of entry", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p3_perimeter")
    entry_points_hpe = st.text_area("Location and description of each possible entry point in HPE/Greenhouse")
    associate_comments_hpe = st.text_area("Associate comments on rodent activity in HPE/Greenhouse")
    photos_associate_hpe = st.file_uploader("Take photos of areas mentioned by associate (HPE/Greenhouse)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p3_associate")
    additional_comments_hpe = st.text_area("Additional Comments/Observations (HPE/Greenhouse)")

# Step 4: Food Sources
with st.expander("Step 4 - Food Sources"):
    # Organic Fertilizer
    photos_org_fert = st.file_uploader("Take 2-3 photos of the organic fertilizer and the surrounding area", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p4_org_fert")
    tears_org = st.radio("Are there any tears or holes in the packaging (organic fertilizer)?", ("Yes", "No"))
    activity_org = st.radio("Is there any evidence of rodent activity near the organic fertilizer? (ex. rodent nests or droppings)", ("Yes", "No"))
    activity_org_desc = st.text_area("Describe organic fertilizer activity, including Aisle and Bay numbers")
    # Bird Seed
    photos_bird = st.file_uploader("Take 2-3 photos of the bird seed and the surrounding area", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p4_bird")
    bird_location = st.radio("Where is the bird seed located?", ("Inside Garden", "Outside Garden"))
    bird_storage = st.radio("Is the bird seed stored in bags or in plastic containers?", ("Bags", "Plastic Containers"))
    tears_bird = st.radio("If stored in bags, are there any tears or holes in the bags? (Bird seed)", ("Yes", "No"), key="tears_bird")
    sealed_bird = st.radio("If stored in plastic containers, are the containers completely sealed? (Bird seed)", ("Yes", "No"), key="sealed_bird")
    spilled_bird = st.radio("Is there any spilled bird seed?", ("Yes", "No"))
    activity_bird = st.radio("Check the ground and racks around and behind the bird seed. Is there any evidence of rodent activity? (ex. rodent nests or droppings)", ("Yes", "No"))
    activity_bird_desc = st.text_area("Describe bird seed activity, including Aisle and Bay numbers")
    # Grass Seed
    photos_grass = st.file_uploader("Take 2-3 photos of the grass seed and the surrounding area", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p4_grass")
    grass_location = st.radio("Where is the grass seed located?", ("Inside Garden", "Outside Garden"))
    grass_storage = st.radio("Is the grass seed stored in bags or in plastic containers?", ("Bags", "Plastic Containers"))
    tears_grass = st.radio("If stored in bags, are there any tears or holes in the bags? (Grass seed)", ("Yes", "No"), key="tears_grass")
    sealed_grass = st.radio("If stored in plastic containers, are the containers completely sealed? (Grass seed)", ("Yes", "No"), key="sealed_grass")
    spilled_grass = st.radio("Is there any spilled grass seed?", ("Yes", "No"))
    activity_grass = st.radio("Check the ground and racks around and behind the grass seed. Is there any evidence of rodent activity? (ex. rodent nests or droppings)", ("Yes", "No"))
    activity_grass_desc = st.text_area("Describe grass seed activity, including Aisle and Bay numbers")
    # Plant Seed
    photos_plant = st.file_uploader("Take 2-3 photos of the plant seed packet display", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p4_plant")
    plant_location = st.radio("Where is the plant seed packet display located?", ("Inside Garden", "Outside Garden"))
    tears_plant = st.radio("Are there any tears or holes in the packets?", ("Yes", "No"))
    spilled_plant = st.radio("Is there any spilled seed around the display?", ("Yes", "No"))
    activity_plant = st.radio("Is there any evidence of rodent activity near the display? (ex. rodent nests or droppings)", ("Yes", "No"))
    activity_plant_desc = st.text_area("Describe plant seed activity, including Aisle and Bay numbers")
    additional_comments_food = st.text_area("Additional Comments/Observations Regarding Food Sources")

# Step 5: Inside the Store
with st.expander("Step 5 - Inspect and Photograph Inside the Store"):
    photos_cmu_inside = st.file_uploader("Inspect the CMU wall (connected to Outside Garden). Photograph any possible points of entry", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_cmu")
    entry_points_cmu = st.text_area("Location and description of each possible entry point (CMU wall)")
    photos_entrances_inside = st.file_uploader("Photograph the entrance doors leading to Outside Garden", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_entrances")
    doors_open = st.radio("Are the doors open?", ("Yes", "No"))
    gaps_doors = st.radio("Are there gaps or holes around the doors?", ("Yes", "No"))
    gaps_gaskets_inside = st.radio("Are there gaps or holes in any of the rubber gaskets (inside entrances)?", ("Yes", "No"))
    entry_points_inside = st.radio("Are there any other possible points of entry (inside entrances)?", ("Yes", "No"))
    entry_points_inside_desc = st.text_area("Location and description of each possible entry point (inside entrances)")
    associate_comments_inside = st.text_area("Associate comments on rodent activity in inside store")
    photos_associate_inside = st.file_uploader("Take photos of areas mentioned by associate (inside store)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_associate")
    additional_comments_inside = st.text_area("Additional Comments/Observations (inside store)")
    # Receiving
    photos_receiving = st.file_uploader("Take 3-5 photos of the receiving area, including the doors and any signs of activity", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_receiving")
    activity_receiving = st.radio("Are there any signs of rodent activity in receiving? (ex. droppings, grease stains, nests)", ("Yes", "No"))
    activity_receiving_desc = st.text_area("Describe receiving activity, including Aisle and Bay numbers")
    # Back Offices & Training Room
    photos_offices = st.file_uploader("Photograph the back offices & training room areas, including any food, trash bins and power cords", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_offices")
    food_offices = st.radio("Is there any food in the back offices?", ("Yes", "No"))
    activity_desks = st.radio("Inspect underneath and around all desks. Are there any signs of rodent activity?", ("Yes", "No"))
    chewing_cords = st.radio("Inspect the computer and plug cords. Are there any signs of chewing?", ("Yes", "No"))
    activity_trash_offices = st.radio("Inspect the area around all trash bins. Are there any signs of rodent activity?", ("Yes", "No"))
    photos_ceiling_offices = st.file_uploader("Lift up ceiling tiles to inspect for rodent activity above. Take 2-3 photos (back offices)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_ceiling_offices")
    activity_ceiling_offices = st.radio("Are there any signs of rodent activity above ceiling (back offices)?", ("Yes", "No"))
    activity_offices_desc = st.text_area("Describe back offices findings")
    associate_comments_offices = st.text_area("Associate comments on rodent activity in back offices")
    photos_associate_offices = st.file_uploader("Take photos of areas mentioned by associate (back offices)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_associate_offices")
    additional_comments_offices = st.text_area("Additional Comments/Observations (back offices)")
    # Breakroom
    photos_breakroom = st.file_uploader("Photograph breakroom, including the counters, cabinets, and areas around refrigerators, vending machines, trash bins", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_breakroom")
    food_breakroom = st.radio("Is food stored on the countertops or tables?", ("Yes", "No"))
    activity_cabinets = st.radio("Inspect the inside of all cabinets. Are there any signs of rodent activity? (ex. rodent droppings)", ("Yes", "No"))
    activity_fridge = st.radio("Inspect behind and around the refrigerator. Are there any signs of rodent activity?", ("Yes", "No"))
    activity_vending = st.radio("Inspect behind and around any vending machines. Are there any signs of rodent activity?", ("Yes", "No"))
    activity_trash_break = st.radio("Inspect the area around any trash bins. Are there any signs of rodent activity?", ("Yes", "No"))
    photos_ceiling_break = st.file_uploader("Lift up ceiling tiles to inspect for rodent activity above. Take 2-3 photos (breakroom)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_ceiling_break")
    activity_ceiling_break = st.radio("Are there any signs of rodent activity above ceiling (breakroom)?", ("Yes", "No"))
    associate_comments_break = st.text_area("Associate comments on rodent activity in breakroom")
    photos_associate_break = st.file_uploader("Take photos of areas mentioned by associate (breakroom)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_associate_break")
    additional_comments_break = st.text_area("Additional Comments/Observations (breakroom)")
    # Front End
    photos_candy = st.file_uploader("Inspect underneath and around all candy/snack displays. Take 1-2 photos of this area at each register", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_candy")
    activity_candy = st.radio("Are there any signs of rodent activity (candy/snack displays)?", ("Yes", "No"))
    activity_candy_desc = st.text_area("Describe candy/snack findings, include the nearest register number")
    photos_registers = st.file_uploader("Inspect underneath and around all registers. Take 1-2 photos of this area at each register", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_registers")
    activity_registers = st.radio("Are there any signs of rodent activity (registers)?", ("Yes", "No"))
    activity_registers_desc = st.text_area("Describe registers findings, include the register number")
    photos_fridges_front = st.file_uploader("Inspect underneath and around all refrigerators. Take 1-2 photos of this area at each register", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_fridges")
    activity_fridges = st.radio("Are there any signs of rodent activity (refrigerators)?", ("Yes", "No"))
    activity_fridges_desc = st.text_area("Describe refrigerators findings, include the nearest register number")
    associate_comments_front = st.text_area("Associate comments on rodent activity in front end")
    photos_associate_front = st.file_uploader("Take photos of areas mentioned by associate (front end)", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_associate_front")
    # Additional Concerns
    additional_concerns = st.radio("Did either you or management note any additional areas of concern?", ("Yes", "No"))
    additional_desc = st.text_area("Describe the additional areas of concern. Provide photos")
    photos_additional = st.file_uploader("Photos of additional areas of concern", type=["png","jpg","jpeg","heic"], accept_multiple_files=True, key="p5_additional")

if st.button("Generate PDF Report", type="primary"):
    if not store_code or not jo_number or not tech_name:
        st.error("Store Code, JO#, and Technician Name required")
    else:
        with st.spinner("Generating PDF..."):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, "Brighter Image Rodent Survey Report")
            pdf.multi_cell(0, 10, f"Store: {store_code}   JO #: {jo_number}   Date: {survey_date}   Technician: {tech_name}")
            pdf.multi_cell(0, 10, f"Signature: {tech_sig}")

            # Step 1
            pdf.add_page()
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, "Step 1 - Perimeter")
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 10, f"Gaps in gaskets: {gaps_gaskets} - Entrances: {gaps_entrances}")
            pdf.multi_cell(0, 10, f"Bait boxes: {bait_boxes} - Missing: {missing_boxes}")
            pdf.multi_cell(0, 10, f"Food source: {food_source} - Desc: {food_desc}")
            pdf.multi_cell(0, 10, f"Water source: {water_source} - Desc: {water_desc}")
            pdf.multi_cell(0, 10, f"Shelter source: {shelter_source} - Desc: {shelter_desc}")
            pdf.multi_cell(0, 10, f"Exclusion points: {exclusion_points} - Desc: {exclusion_desc}")
            pdf.multi_cell(0, 10, f"Rodents from: {rodents_from}")

            # Add photos for Step 1
            for uploader, title in [(photos_perimeter, "Perimeter Photos"), (photos_compactor, "Compactor"), (photos_entrances, "Entrances"), (photos_gaskets, "Gaskets")]:
                if uploader:
                    pdf.add_page()
                    pdf.multi_cell(0, 10, title)
                    for file in uploader:
                        img = Image.open(file)
                        pdf.image(img, w=100)

            # Similar for other steps – adding all sections and photos
            # Step 2
            pdf.add_page()
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, "Step 2 - Outside Garden")
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 10, f"Nests: {nests_present} - Location: {nests_location}")
            pdf.multi_cell(0, 10, f"Grease stains: {grease_stains} - Desc: {grease_desc}")
            pdf.multi_cell(0, 10, f"Rodents running: {rodents_running} - Desc: {rodents_running_desc}")
            pdf.multi_cell(0, 10, f"Racking activity: {activity_racking} - Desc: {activity_racking_desc}")
            pdf.multi_cell(0, 10, f"Product activity: {activity_product} - Desc: {activity_product_desc}")
            pdf.multi_cell(0, 10, f"Entry points: {entry_points_og}")
            pdf.multi_cell(0, 10, f"Associate comments: {associate_comments_og}")
            pdf.multi_cell(0, 10, f"Additional comments: {additional_comments_og}")

            for uploader, title in [(photos_nests, "Nests"), (photos_grease_top, "Grease Top"), (photos_racking_under, "Racking Under"), (photos_product, "Product"), (photos_perimeter_og, "Perimeter OG"), (photos_associate_og, "Associate OG")]:
                if uploader:
                    pdf.add_page()
                    pdf.multi_cell(0, 10, title)
                    for file in uploader:
                        img = Image.open(file)
                        pdf.image(img, w=100)

            # Step 3
            pdf.add_page()
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, "Step 3 - HPE/Greenhouse")
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 10, f"Nests: {nests_present_hpe} - Location: {nests_location_hpe}")
            pdf.multi_cell(0, 10, f"Grease stains: {grease_stains_hpe} - Desc: {grease_desc_hpe}")
            pdf.multi_cell(0, 10, f"Rodents running: {rodents_running_hpe} - Desc: {rodents_running_desc_hpe}")
            pdf.multi_cell(0, 10, f"Racking activity: {activity_racking_hpe} - Desc: {activity_racking_desc_hpe}")
            pdf.multi_cell(0, 10, f"Product activity: {activity_product_hpe} - Desc: {activity_product_desc_hpe}")
            pdf.multi_cell(0, 10, f"Entry points: {entry_points_hpe}")
            pdf.multi_cell(0, 10, f"Associate comments: {associate_comments_hpe}")
            pdf.multi_cell(0, 10, f"Additional comments: {additional_comments_hpe}")

            for uploader, title in [(photos_nests_hpe, "Nests HPE"), (photos_grease_top_hpe, "Grease Top HPE"), (photos_racking_under_hpe, "Racking Under HPE"), (photos_product_hpe, "Product HPE"), (photos_perimeter_hpe, "Perimeter HPE"), (photos_associate_hpe, "Associate HPE")]:
                if uploader:
                    pdf.add_page()
                    pdf.multi_cell(0, 10, title)
                    for file in uploader:
                        img = Image.open(file)
                        pdf.image(img, w=100)

            # Step 4
            pdf.add_page()
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, "Step 4 - Food Sources")
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 10, f"Organic Fertilizer tears: {tears_org} - Activity: {activity_org} - Desc: {activity_org_desc}")
            pdf.multi_cell(0, 10, f"Bird Seed location: {bird_location} - Storage: {bird_storage} - Tears: {tears_bird} - Sealed: {sealed_bird} - Spilled: {spilled_bird} - Activity: {activity_bird} - Desc: {activity_bird_desc}")
            pdf.multi_cell(0, 10, f"Grass Seed location: {grass_location} - Storage: {grass_storage} - Tears: {tears_grass} - Sealed: {sealed_grass} - Spilled: {spilled_grass} - Activity: {activity_grass} - Desc: {activity_grass_desc}")
            pdf.multi_cell(0, 10, f"Plant Seed location: {plant_location} - Tears: {tears_plant} - Spilled: {spilled_plant} - Activity: {activity_plant} - Desc: {activity_plant_desc}")
            pdf.multi_cell(0, 10, f"Additional food comments: {additional_comments_food}")

            for uploader, title in [(photos_org_fert, "Organic Fertilizer"), (photos_bird, "Bird Seed"), (photos_grass, "Grass Seed"), (photos_plant, "Plant Seed")]:
                if uploader:
                    pdf.add_page()
                    pdf.multi_cell(0, 10, title)
                    for file in uploader:
                        img = Image.open(file)
                        pdf.image(img, w=100)

            # Step 5
            pdf.add_page()
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, "Step 5 - Inside the Store")
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 10, f"CMU entry points: {entry_points_cmu}")
            pdf.multi_cell(0, 10, f"Doors open: {doors_open} - Gaps doors: {gaps_doors} - Gaskets gaps: {gaps_gaskets_inside} - Other entry: {entry_points_inside} - Desc: {entry_points_inside_desc}")
            pdf.multi_cell(0, 10, f"Associate comments inside: {associate_comments_inside}")
            pdf.multi_cell(0, 10, f"Additional comments inside: {additional_comments_inside}")
            pdf.multi_cell(0, 10, f"Receiving activity: {activity_receiving} - Desc: {activity_receiving_desc}")
            pdf.multi_cell(0, 10, f"Offices food: {food_offices} - Desks activity: {activity_desks} - Cords chewing: {chewing_cords} - Trash activity: {activity_trash_offices} - Ceiling activity: {activity_ceiling_offices} - Desc: {activity_offices_desc}")
            pdf.multi_cell(0, 10, f"Associate comments offices: {associate_comments_offices}")
            pdf.multi_cell(0, 10, f"Additional comments offices: {additional_comments_offices}")
            pdf.multi_cell(0, 10, f"Breakroom food: {food_breakroom} - Cabinets activity: {activity_cabinets} - Fridge activity: {activity_fridge} - Vending activity: {activity_vending} - Trash activity: {activity_trash_break} - Ceiling activity: {activity_ceiling_break}")
            pdf.multi_cell(0, 10, f"Associate comments break: {associate_comments_break}")
            pdf.multi_cell(0, 10, f"Additional comments break: {additional_comments_break}")
            pdf.multi_cell(0, 10, f"Candy activity: {activity_candy} - Desc: {activity_candy_desc}")
            pdf.multi_cell(0, 10, f"Registers activity: {activity_registers} - Desc: {activity_registers_desc}")
            pdf.multi_cell(0, 10, f"Fridges activity: {activity_fridges} - Desc: {activity_fridges_desc}")
            pdf.multi_cell(0, 10, f"Associate comments front: {associate_comments_front}")
            pdf.multi_cell(0, 10, f"Additional concerns: {additional_concerns} - Desc: {additional_desc}")

            for uploader, title in [(photos_cmu_inside, "CMU Inside"), (photos_entrances_inside, "Entrances Inside"), (photos_receiving, "Receiving"), (photos_offices, "Offices"), (photos_ceiling_offices, "Ceiling Offices"), (photos_associate_offices, "Associate Offices"), (photos_breakroom, "Breakroom"), (photos_ceiling_break, "Ceiling Break"), (photos_associate_break, "Associate Break"), (photos_candy, "Candy"), (photos_registers, "Registers"), (photos_fridges_front, "Fridges Front"), (photos_associate_front, "Associate Front"), (photos_additional, "Additional")]:
                if uploader:
                    pdf.add_page()
                    pdf.multi_cell(0, 10, title)
                    for file in uploader:
                        img = Image.open(file)
                        pdf.image(img, w=100)

            pdf_bytes = pdf.output(dest='S').encode('latin1')
            b64 = base64.b64encode(pdf_bytes).decode()
            filename = f"Rodent_Survey_{store_code}_{jo_number}_{survey_date}.pdf"
            href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF Report</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("Report ready! Download and email to Brighter Image")
