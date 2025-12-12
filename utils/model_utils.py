"""
Model Utilities Module
Handles model loading and prediction
"""

import os
import joblib
import streamlit as st
from utils.config import BEST_MODELS, MODEL_PERFORMANCE, APP_CONFIG
from utils.feature_engineering import prepare_input_data


@st.cache_resource
def load_model(location, models_dir=None):
    """
    Load trained model and scaler for a location
    Cached to avoid reloading
    """
    if models_dir is None:
        models_dir = APP_CONFIG['models_dir']
    
    model_path = os.path.join(models_dir, f'{location}_model.pkl')
    scaler_path = os.path.join(models_dir, f'{location}_scaler.pkl')
    features_path = os.path.join(models_dir, f'{location}_features.pkl')
    
    if not os.path.exists(model_path):
        return None, None, None
    
    model = joblib.load(model_path)
    
    scaler = None
    if os.path.exists(scaler_path):
        scaler = joblib.load(scaler_path)
    
    features = None
    if os.path.exists(features_path):
        features = joblib.load(features_path)
    
    return model, scaler, features


def make_prediction(location, humidity, ambient_temp, wind_speed, visibility, 
                   pressure, cloud_ceiling, month, hour, 
                   latitude, longitude, altitude):
    """
    Make prediction using trained model
    """
    model, scaler, feature_names = load_model(location)
    
    if model is None:
        return None, None, False
    
    # Prepare input with enhanced features
    input_data = prepare_input_data(
        humidity, ambient_temp, wind_speed, visibility,
        pressure, cloud_ceiling, month, hour,
        latitude, longitude, altitude
    )
    
    # Match feature order from training
    if feature_names is not None:
        input_data = input_data[feature_names]
    
    model_name = BEST_MODELS[location]
    
    # Store model R² in session state
    if location in MODEL_PERFORMANCE:
        st.session_state['model_r2'] = f"{MODEL_PERFORMANCE[location]['r2']:.4f}"
    
    try:
        if scaler is not None:
            input_scaled = scaler.transform(input_data)
            predicted_power = model.predict(input_scaled)[0]
        else:
            predicted_power = model.predict(input_data)[0]
        
        predicted_power = max(0, predicted_power)
        
        return predicted_power, model_name, True
        
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None, model_name, False


def get_model_name(location):
    """Get model type for location"""
    return BEST_MODELS.get(location, 'Unknown')