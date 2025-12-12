"""
Predict Page - Solar Power Prediction
"""

import streamlit as st
import pandas as pd
import sys
import os
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.config import (
    APP_CONFIG, LOCATION_DATA, INPUT_RANGES, MONTHS, COLORS
)
from utils.model_utils import make_prediction
from utils.gauge import create_gauge, get_performance_tier, create_simple_comparison

st.set_page_config(
    page_title=f"Predict - {APP_CONFIG['title']}",
    page_icon=APP_CONFIG['icon'],
    layout=APP_CONFIG['layout']
)

# Load CSS
try:
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except:
    pass

# Initialize session state
if 'location_key' not in st.session_state:
    st.session_state.location_key = 'camp_murray'
if 'should_predict' not in st.session_state:
    st.session_state.should_predict = False
if 'selected_location_name' not in st.session_state:
    st.session_state.selected_location_name = 'Camp Murray'

# Sidebar: Solar Image
with st.sidebar:
    st.markdown("###")  # Add spacing
    
    # Solar panel image
    try:
        solar_img = Image.open('images/solar.png')
        st.image(solar_img, use_container_width=True)
    except:
        try:
            solar_img = Image.open('images/solar2.png')
            st.image(solar_img, use_container_width=True)
        except:
            pass

# Header
st.title("☀️ Solar Power Prediction")
st.markdown("Predict solar power output based on environmental conditions")

# Add helpful tip
st.info("""
**💡 How to Use:**
1. **Select Location** from the dropdown menu in the sidebar →
2. **Adjust Month & Hour** from the dropdown menus
3. **Set Environmental Conditions** using the sliders (Humidity, Temperature, Wind Speed, Visibility, Pressure, Cloud Ceiling)
4. Click **"Predict Power Output"** button below to generate prediction
5. **Download PDF Report** with the prediction results and analysis
6. Or try **"🎲 Random Sample"** button at the bottom of the sidebar to load real data from the dataset
""")

st.markdown("---")

# Sidebar - Location
st.sidebar.header("Input Parameters")

location_options = {v['display']: k for k, v in LOCATION_DATA.items()}
selected_location_display = st.sidebar.selectbox(
    "Location",
    options=list(location_options.keys()),
    index=list(location_options.keys()).index(st.session_state.selected_location_name)
)
selected_location = location_options[selected_location_display]
st.session_state.location_key = selected_location
st.session_state.selected_location_name = selected_location_display

st.sidebar.markdown("---")

# Environmental Inputs
st.sidebar.subheader("Environmental Conditions")

humidity = st.sidebar.slider(
    "Humidity (%)",
    INPUT_RANGES['humidity']['min'],
    INPUT_RANGES['humidity']['max'],
    st.session_state.get('humidity', INPUT_RANGES['humidity']['default']),
    INPUT_RANGES['humidity']['step']
)

ambient_temp = st.sidebar.slider(
    "Temperature (°C)",
    INPUT_RANGES['ambient_temp']['min'],
    INPUT_RANGES['ambient_temp']['max'],
    st.session_state.get('ambient_temp', INPUT_RANGES['ambient_temp']['default']),
    INPUT_RANGES['ambient_temp']['step']
)

wind_speed = st.sidebar.slider(
    "Wind Speed (m/s)",
    INPUT_RANGES['wind_speed']['min'],
    INPUT_RANGES['wind_speed']['max'],
    st.session_state.get('wind_speed', INPUT_RANGES['wind_speed']['default']),
    INPUT_RANGES['wind_speed']['step']
)

visibility = st.sidebar.slider(
    "Visibility (km)",
    INPUT_RANGES['visibility']['min'],
    INPUT_RANGES['visibility']['max'],
    st.session_state.get('visibility', INPUT_RANGES['visibility']['default']),
    INPUT_RANGES['visibility']['step']
)

pressure = st.sidebar.slider(
    "Pressure (hPa)",
    INPUT_RANGES['pressure']['min'],
    INPUT_RANGES['pressure']['max'],
    st.session_state.get('pressure', INPUT_RANGES['pressure']['default']),
    INPUT_RANGES['pressure']['step']
)

cloud_ceiling = st.sidebar.slider(
    "Cloud Ceiling (ft)",
    INPUT_RANGES['cloud_ceiling']['min'],
    INPUT_RANGES['cloud_ceiling']['max'],
    st.session_state.get('cloud_ceiling', INPUT_RANGES['cloud_ceiling']['default']),
    INPUT_RANGES['cloud_ceiling']['step']
)

st.sidebar.markdown("---")

# Time Parameters
st.sidebar.subheader("Time")

month = st.sidebar.selectbox(
    "Month",
    list(range(1, 13)),
    index=st.session_state.get('month', 6) - 1,
    format_func=lambda x: MONTHS[x-1]
)

hour = st.sidebar.selectbox(
    "Hour",
    list(range(0, 24)),
    index=st.session_state.get('hour', 12)
)

st.sidebar.markdown("---")

# Random Sample at bottom of sidebar
st.sidebar.markdown("### 🎲 Try Random Data")
if st.sidebar.button("🎲 Random Sample", use_container_width=True, type="secondary"):
    try:
        data_path = os.path.join(APP_CONFIG['data_dir'], 'photovoltaic_cleaned.csv')
        if os.path.exists(data_path):
            df = pd.read_csv(data_path)
            sample = df.sample(n=1).iloc[0]
            
            # Update session state with selected_location_name instead of widget key
            st.session_state.selected_location_name = LOCATION_DATA[sample['location']]['display']
            st.session_state.update({
                'humidity': float(sample['humidity']),
                'ambient_temp': float(sample['ambient_temp']),
                'wind_speed': int(sample['wind_speed']),
                'visibility': float(sample['visibility']),
                'pressure': int(sample['pressure']),
                'cloud_ceiling': int(sample['cloud_ceiling']),
                'month': int(sample['month']),
                'hour': int(sample['hour']),
                'should_predict': True
            })
            st.rerun()
    except Exception as e:
        st.sidebar.error(f"Error: {str(e)}")

st.sidebar.caption("Loads actual data point from the dataset")

# Store values
st.session_state.update({
    'humidity': humidity,
    'ambient_temp': ambient_temp,
    'wind_speed': wind_speed,
    'visibility': visibility,
    'pressure': pressure,
    'cloud_ceiling': cloud_ceiling,
    'month': month,
    'hour': hour
})

# Main area - Location info
loc_info = LOCATION_DATA[selected_location]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Location", loc_info['display'])
with col2:
    st.metric("Latitude", f"{loc_info['lat']}°")
with col3:
    st.metric("Longitude", f"{loc_info['lon']}°")
with col4:
    st.metric("Altitude", f"{loc_info['alt']} m")

st.markdown("---")

# Predict button
predict_clicked = st.button("🔮 Predict Power Output", type="primary", use_container_width=True)

# Initialize variables for PDF generation (FIX for PDF error)
predicted_power = None
model_name = None
tier_name = None
percentage = None

# Make prediction
if st.session_state.get('should_predict', False) or predict_clicked:
    st.session_state.should_predict = False
    
    with st.spinner("Calculating..."):
        predicted_power, model_name, success = make_prediction(
            selected_location, humidity, ambient_temp, wind_speed,
            visibility, pressure, cloud_ceiling, month, hour,
            loc_info['lat'], loc_info['lon'], loc_info['alt']
        )
    
    if success and predicted_power is not None:
        st.success("Prediction Complete")
        
        # Results
        result_col1, result_col2 = st.columns([3, 2])
        
        with result_col1:
            gauge_fig = create_gauge(predicted_power, selected_location)
            st.plotly_chart(gauge_fig, use_container_width=True)
        
        with result_col2:
            st.markdown(f"""
            <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%); border-radius: 12px; color: white;'>
                <h3 style='color: white; margin: 0;'>Predicted Output</h3>
                <h1 style='color: white; font-size: 3.5rem; margin: 1rem 0;'>{predicted_power:.2f}</h1>
                <p style='color: white; font-size: 1.2rem; margin: 0;'>kW</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            tier_name, tier_color, percentage = get_performance_tier(predicted_power, selected_location)
            st.info(f"""
            **Performance:** {tier_name}  
            **vs Average:** {percentage:.0f}%  
            **Model:** {model_name}
            """)
        
        # Comparison
        st.markdown("---")
        comparison_fig = create_simple_comparison(predicted_power, selected_location)
        st.plotly_chart(comparison_fig, use_container_width=True)
        
        # PDF Download (now variables are defined)
        st.markdown("---")

        try:
            from utils.pdf_generator import generate_prediction_report
            
            pdf_bytes = generate_prediction_report(
                location=selected_location,
                location_data=loc_info,
                inputs={
                    'humidity': humidity, 'ambient_temp': ambient_temp,
                    'wind_speed': wind_speed, 'visibility': visibility,
                    'pressure': pressure, 'cloud_ceiling': cloud_ceiling,
                    'month': month, 'hour': hour
                },
                prediction=predicted_power,
                model_name=model_name,
                tier_name=tier_name,
                percentage=percentage
            )
            
            col_pdf = st.columns([1, 1, 1])[1]
            with col_pdf:
                st.download_button(
                    "📄 Download PDF Report",
                    pdf_bytes,
                    f"solar_prediction_{selected_location}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    "application/pdf",
                    use_container_width=True,
                    type="primary"
                )
        except Exception as e:
            st.error(f"PDF generation error: {str(e)}")
    else:
        st.error("Prediction failed. Please check your inputs and try again.")