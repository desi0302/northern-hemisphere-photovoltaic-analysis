import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Page configuration
st.set_page_config(
    page_title="Solar Power Predictor",
    page_icon="☀️",
    layout="wide"
)

# Title and description
st.title("☀️ Solar Power Prediction System")
st.markdown("""
This application predicts solar power output (kW) based on environmental conditions 
at 12 military installation sites across the Northern Hemisphere.
""")

# Location data with coordinates and altitude
LOCATION_DATA = {
    'camp_murray': {'lat': 47.11, 'lon': -122.57, 'alt': 84, 'display': 'Camp Murray'},
    'grissom': {'lat': 40.65, 'lon': -86.15, 'alt': 250, 'display': 'Grissom'},
    'hill_weber': {'lat': 41.12, 'lon': -111.97, 'alt': 1459, 'display': 'Hill Weber'},
    'jdmt': {'lat': 26.98, 'lon': -80.11, 'alt': 2, 'display': 'JDMT'},
    'kahului': {'lat': 20.89, 'lon': -156.44, 'alt': 2, 'display': 'Kahului'},
    'malmstrom': {'lat': 47.52, 'lon': -111.18, 'alt': 1043, 'display': 'Malmstrom'},
    'march_afb': {'lat': 33.88, 'lon': -117.25, 'alt': 470, 'display': 'March AFB'},
    'mnang': {'lat': 44.88, 'lon': -93.21, 'alt': 262, 'display': 'MNANG'},
    'offutt': {'lat': 41.12, 'lon': -95.91, 'alt': 321, 'display': 'Offutt'},
    'peterson': {'lat': 38.82, 'lon': -104.71, 'alt': 1879, 'display': 'Peterson'},
    'travis': {'lat': 38.16, 'lon': -121.56, 'alt': 1, 'display': 'Travis'},
    'usafa': {'lat': 38.95, 'lon': -104.83, 'alt': 1947, 'display': 'USAFA'}
}

# Best models per location (from your ML notebook results)
BEST_MODELS = {
    'camp_murray': 'GradientBoosting',
    'grissom': 'Linear',
    'hill_weber': 'GradientBoosting',
    'jdmt': 'GradientBoosting',
    'kahului': 'Lasso',
    'malmstrom': 'GradientBoosting',
    'march_afb': 'GradientBoosting',
    'mnang': 'GradientBoosting',
    'offutt': 'Lasso',
    'peterson': 'RandomForest',
    'travis': 'GradientBoosting',
    'usafa': 'Linear'
}

def engineer_features(df):
    """
    Create engineered features matching the ML pipeline
    """
    df = df.copy()
    
    # Interaction features
    df['temp_humidity'] = df['ambient_temp'] * df['humidity']
    df['temp_cloud'] = df['ambient_temp'] * df['cloud_ceiling']
    df['humidity_cloud'] = df['humidity'] * df['cloud_ceiling']
    
    # Cyclic time features
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    
    return df

def get_model_by_name(model_name):
    """Return model instance by name"""
    models = {
        'Linear': LinearRegression(),
        'Ridge': Ridge(alpha=1.0),
        'Lasso': Lasso(alpha=0.1, max_iter=10000),
        'GradientBoosting': GradientBoostingRegressor(
            n_estimators=100,
            max_depth=4,
            min_samples_split=20,
            min_samples_leaf=10,
            learning_rate=0.05,
            subsample=0.8,
            random_state=42
        ),
        'RandomForest': RandomForestRegressor(
            n_estimators=200,
            max_depth=10,
            min_samples_split=10,
            min_samples_leaf=5,
            random_state=42
        )
    }
    return models.get(model_name)

@st.cache_resource
def load_model(location, models_dir='models'):
    """
    Load trained model and scaler (if exists) for a location
    Cached to avoid reloading on every prediction
    """
    model_path = os.path.join(models_dir, f'{location}_model.pkl')
    scaler_path = os.path.join(models_dir, f'{location}_scaler.pkl')
    features_path = os.path.join(models_dir, f'{location}_features.pkl')
    
    # Check if model exists
    if not os.path.exists(model_path):
        return None, None, None
    
    # Load model
    model = joblib.load(model_path)
    
    # Load scaler if it exists (for Linear/Ridge/Lasso models)
    scaler = None
    if os.path.exists(scaler_path):
        scaler = joblib.load(scaler_path)
    
    # Load feature names
    features = None
    if os.path.exists(features_path):
        features = joblib.load(features_path)
    
    return model, scaler, features

def make_prediction(location, humidity, ambient_temp, wind_speed, visibility, 
                   pressure, cloud_ceiling, month, hour, models_dir='models'):
    """
    Make a prediction using the trained model for the location
    """
    # Get location data
    loc_data = LOCATION_DATA[location]
    
    # Load the trained model
    model, scaler, feature_names = load_model(location, models_dir)
    
    if model is None:
        st.error(f"❌ Model not found for {loc_data['display']}. Please train and save models first.")
        return None, None
    
    # Create input dataframe
    input_data = pd.DataFrame({
        'humidity': [humidity],
        'ambient_temp': [ambient_temp],
        'wind_speed': [wind_speed],
        'visibility': [visibility],
        'pressure': [pressure],
        'cloud_ceiling': [cloud_ceiling],
        'month': [month],
        'hour': [hour],
        'altitude': [loc_data['alt']],
        'latitude': [loc_data['lat']],
        'longitude': [loc_data['lon']]
    })
    
    # Engineer features
    input_data = engineer_features(input_data)
    
    # Ensure feature order matches training
    if feature_names is not None:
        input_data = input_data[feature_names]
    
    # Get model name
    model_name = BEST_MODELS[location]
    
    # Make prediction
    if scaler is not None:
        # Scale features for Linear/Ridge/Lasso models
        input_scaled = scaler.transform(input_data)
        predicted_power = model.predict(input_scaled)[0]
    else:
        # Tree-based models don't need scaling
        predicted_power = model.predict(input_data)[0]
    
    return predicted_power, model_name

# Sidebar for inputs
st.sidebar.header("Input Parameters")

# Location selection
location_options = {v['display']: k for k, v in LOCATION_DATA.items()}
selected_location_display = st.sidebar.selectbox(
    "Select Location",
    options=list(location_options.keys())
)
selected_location = location_options[selected_location_display]

st.sidebar.markdown("---")
st.sidebar.subheader("Environmental Conditions")

# Input fields for environmental parameters
humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=1.0,
    help="Relative humidity percentage"
)

ambient_temp = st.sidebar.slider(
    "Ambient Temperature (°C)",
    min_value=-20.0,
    max_value=50.0,
    value=20.0,
    step=0.5,
    help="Air temperature in Celsius"
)

wind_speed = st.sidebar.slider(
    "Wind Speed (m/s)",
    min_value=0,
    max_value=30,
    value=5,
    step=1,
    help="Wind speed in meters per second"
)

visibility = st.sidebar.slider(
    "Visibility (km)",
    min_value=0.0,
    max_value=20.0,
    value=10.0,
    step=0.5,
    help="Atmospheric visibility in kilometers"
)

pressure = st.sidebar.slider(
    "Atmospheric Pressure (hPa)",
    min_value=950,
    max_value=1050,
    value=1013,
    step=1,
    help="Atmospheric pressure in hectopascals"
)

cloud_ceiling = st.sidebar.slider(
    "Cloud Ceiling (feet AGL)",
    min_value=0,
    max_value=722,
    value=300,
    step=10,
    help="Height of cloud base above ground level in feet"
)

st.sidebar.markdown("---")
st.sidebar.subheader("Time Parameters")

month = st.sidebar.selectbox(
    "Month",
    options=list(range(1, 13)),
    index=5,
    format_func=lambda x: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][x-1]
)

hour = st.sidebar.selectbox(
    "Hour of Day",
    options=list(range(0, 24)),
    index=12
)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Selected Location Information")
    loc_info = LOCATION_DATA[selected_location]
    
    info_col1, info_col2, info_col3 = st.columns(3)
    with info_col1:
        st.metric("Latitude", f"{loc_info['lat']}°")
    with info_col2:
        st.metric("Longitude", f"{loc_info['lon']}°")
    with info_col3:
        st.metric("Altitude", f"{loc_info['alt']} m")
    
    st.markdown("---")
    
    # Prediction button
    if st.button("🔮 Predict Solar Power Output", type="primary", use_container_width=True):
        with st.spinner("Calculating prediction..."):
            predicted_power, model_name = make_prediction(
                selected_location, humidity, ambient_temp, wind_speed,
                visibility, pressure, cloud_ceiling, month, hour
            )
        
        if predicted_power is not None:
            st.success("Prediction Complete!")
            st.markdown("### Predicted Solar Power Output")
            st.markdown(f"# {predicted_power:.2f} kW")
            
            st.info(f"""
            **Model Used:** {model_name}  
            **Location:** {loc_info['display']}  
            **Coordinates:** {loc_info['lat']}°, {loc_info['lon']}°  
            **Altitude:** {loc_info['alt']} m
            """)

with col2:
    st.subheader("Input Summary")
    summary_data = {
        "Parameter": [
            "Location",
            "Humidity",
            "Temperature",
            "Wind Speed",
            "Visibility",
            "Pressure",
            "Cloud Ceiling",
            "Month",
            "Hour"
        ],
        "Value": [
            loc_info['display'],
            f"{humidity:.1f}%",
            f"{ambient_temp:.1f}°C",
            f"{wind_speed} m/s",
            f"{visibility:.1f} km",
            f"{pressure} hPa",
            f"{cloud_ceiling} ft",
            ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][month-1],
            f"{hour}:00"
        ]
    }
    st.dataframe(
        pd.DataFrame(summary_data),
        hide_index=True,
        use_container_width=True
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Solar Power Prediction System | Site-Specific ML Models</p>
    <p>Based on 12 location-specific models trained on Northern Hemisphere data</p>
</div>
""", unsafe_allow_html=True)