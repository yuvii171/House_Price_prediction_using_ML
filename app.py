import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="House Crice Prediction ",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# PREMIUM CUSTOM CSS
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Sleek Prediction Card */
    .prediction-container {
        padding: 3rem;
        border-radius: 16px;
        background: linear-gradient(145deg, rgba(28, 131, 225, 0.05) 0%, rgba(28, 131, 225, 0.1) 100%);
        border: 1px solid rgba(28, 131, 225, 0.2);
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .prediction-container:hover {
        transform: translateY(-5px);
    }
    
    /* Gradient Text for Price */
    .prediction-value {
        font-size: 100rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #1c83e1, #0ea5e9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
        line-height: 1.2;
    }
    
    .prediction-label {
        font-size: 1.1rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 0;
    }
    
    /* Clean Divider */
    hr {
        margin-top: 2rem;
        margin-bottom: 2rem;
        border-color: rgba(150, 150, 150, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ASSET LOADING (With Academic Safeguards)
# -----------------------------------------------------------------------------
@st.cache_resource
def load_assets():
    required_files = ["house_price_model.pkl", "scaler.pkl", "model_columns.pkl"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        return None, None, None, missing_files
        
    try:
        model = joblib.load("house_price_model.pkl")
        scaler = joblib.load("scaler.pkl")
        model_columns = joblib.load("model_columns.pkl")
        return model, scaler, model_columns, []
    except Exception as e:
        return None, None, None, [str(e)]

model, scaler, model_columns, errors = load_assets()

# -----------------------------------------------------------------------------
# SIDEBAR (Project Metadata)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2942/2942205.png", width=60)
    st.markdown("### Valuation Engine v2.0")
    st.caption("Powered by Machine Learning")
    st.divider()
    
    st.markdown("**About this Interface**")
    st.markdown(
        "This tool provides real-time market valuations based on historical property data, "
        "structural dimensions, and localized geographical markers."
    )
    st.divider()
    st.caption("© 2026 Academic Submission")

# -----------------------------------------------------------------------------
# MAIN DASHBOARD HEADER
# -----------------------------------------------------------------------------
st.title("Intelligent Property Valuation")
st.markdown("Enter the architectural and locational parameters below to generate a highly accurate market estimate.")
st.write("")

if errors:
    st.error("⚠️ **System Initialization Error**")
    st.markdown("Missing required model files for deployment:")
    for err in errors:
        st.markdown(f"- `{err}`")
    st.stop()

# -----------------------------------------------------------------------------
# AESTHETIC INPUT FORM
# -----------------------------------------------------------------------------
with st.form("prediction_form", border=True):
    st.markdown("####  Property Parameters")
    st.write("")
    
    col_loc, col_dim, col_feat = st.columns(3, gap="large")
    
    with col_loc:
        st.markdown("Geography")
        city = st.selectbox(
            "Primary City", 
            ["Prayagraj", "Delhi", "Mumbai", "Bangalore", "Pune", "Chennai", "Kolkata"],
            help="Select the primary metropolitan area."
        )
        location = st.selectbox(
            "Zoning Type", 
            ["Urban", "Suburban", "Rural"],
            help="Urban areas typically command higher baseline valuations."
        )
        street_type = st.selectbox("Street Access", ["Paved", "Unpaved"])

    with col_dim:
        st.markdown("Architecture")
        area = st.number_input(
            "Carpet Area (Sq Ft)", 
            min_value=100, max_value=20000, value=1500, step=50,
            help="Total livable interior space."
        )
        rooms = st.number_input("Total Rooms", min_value=1, max_value=20, value=3, step=1)
        build_year = st.number_input(
            "Year of Construction", 
            min_value=1900, max_value=datetime.now().year, value=2015, step=1,
            help="Used to calculate property depreciation."
        )

    with col_feat:
        st.markdown("Amenities")
        property_type = st.selectbox("Structure Type", ["Apartment", "Villa", "Duplex"])
        furnishing = st.selectbox("Interior State", ["Furnished", "Semi-Furnished", "Unfurnished"])
        has_pool = st.selectbox("Swimming Pool Facility", ["Yes", "No"])
        
        st.write("")
        submit = st.form_submit_button("Compute Valuation ", use_container_width=True)

# -----------------------------------------------------------------------------
# MODEL INFERENCE & DISPLAY
# -----------------------------------------------------------------------------
if submit:
    with st.spinner("Compiling parameters and running predictive algorithms..."):
        
        # 1. Build DataFrame (Now includes City)
        input_df = pd.DataFrame({
            "City": [city],
            "Area_SqFt": [area],
            "Rooms": [rooms],
            "Build_Year": [build_year],
            "Location": [location],
            "Street_Type": [street_type],
            "Furnishing": [furnishing],
            "Property_Type": [property_type],
            "Has_Pool": [has_pool]
        })

        # 2. One-Hot Encoding
        input_df = pd.get_dummies(
            input_df,
            columns=["City", "Location", "Street_Type", "Furnishing", "Property_Type", "Has_Pool"],
            drop_first=True
        )

        # 3. Synchronize with Training Features
        # This safely ignores cities the model wasn't originally trained on.
        for col in model_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        
        # Ensure exact column order
        input_df = input_df[model_columns]

        # 4. Predict
        try:
            scaled_input = scaler.transform(input_df)
            prediction = model.predict(scaled_input)[0]
            property_age = datetime.now().year - build_year
            
            # 5. Render Beautiful Output
            st.toast("Valuation computed successfully!")
            
            st.markdown(f"""
                <div class="prediction-container">
                    <p class="prediction-label">Estimated Fair Market Value</p>
                    <p class="prediction-value">₹ {prediction:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)

            # Clean Metrics Row
            st.markdown("####  Property Synopsis")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Location", f"{city} ({location})")
            c2.metric("Footprint", f"{area:,} Sq Ft")
            c3.metric("Effective Age", f"{property_age} Years")
            c4.metric("Layout", f"{rooms} Rooms / {property_type}")

        except Exception as e:
            st.error(f"**Execution Failed:** Encountered an error during inference. \n\n`{e}`")