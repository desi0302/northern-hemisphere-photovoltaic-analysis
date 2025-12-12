"""
Feature Engineering Module
Creates enhanced features matching the ML pipeline with solar physics
"""

import pandas as pd
import numpy as np


def engineer_features(df):
    """
    Create all engineered features for prediction including solar physics
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe with base features
        
    Returns:
    --------
    DataFrame with 24 additional engineered features
    """
    df = df.copy()
    
    # Basic interaction features
    df['temp_humidity'] = df['ambient_temp'] * df['humidity']
    df['temp_cloud'] = df['ambient_temp'] * df['cloud_ceiling']
    df['humidity_cloud'] = df['humidity'] * df['cloud_ceiling']
    
    # Cyclic time features
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    
    # Solar position calculations
    day_of_year = df['month'] * 30.5
    hour_angle = (df['hour'] - 12) * 15
    declination = 23.45 * np.sin(np.radians((360 / 365) * (day_of_year - 81)))
    
    lat_rad = np.radians(df['latitude'])
    dec_rad = np.radians(declination)
    hour_rad = np.radians(hour_angle)
    
    solar_elevation = np.degrees(np.arcsin(
        np.sin(lat_rad) * np.sin(dec_rad) + 
        np.cos(lat_rad) * np.cos(dec_rad) * np.cos(hour_rad)
    ))
    
    df['solar_elevation'] = np.maximum(solar_elevation, 0)
    df['solar_elevation_sq'] = df['solar_elevation'] ** 2
    df['day_length'] = 12 + 2 * declination / 15
    
    # Temperature efficiency
    df['temp_above_25'] = np.maximum(df['ambient_temp'] - 25, 0)
    df['temp_efficiency_factor'] = 1 - 0.005 * df['temp_above_25']
    df['ambient_temp_sq'] = df['ambient_temp'] ** 2
    
    # Atmospheric attenuation
    df['cloud_attenuation'] = 1 / (1 + df['cloud_ceiling'] / 500)
    df['humidity_attenuation'] = df['humidity'] / 100
    df['humidity_sq'] = df['humidity'] ** 2
    
    # Advanced interactions
    df['solar_temp'] = df['solar_elevation'] * df['ambient_temp']
    df['solar_humidity'] = df['solar_elevation'] * df['humidity']
    df['solar_cloud'] = df['solar_elevation'] * df['cloud_ceiling']
    df['wind_temp'] = df['wind_speed'] * df['ambient_temp']
    
    return df


def prepare_input_data(humidity, ambient_temp, wind_speed, visibility, 
                       pressure, cloud_ceiling, month, hour, 
                       latitude, longitude, altitude):
    """
    Prepare input data for prediction with all enhanced features
    
    Parameters:
    -----------
    All environmental and temporal input parameters
    
    Returns:
    --------
    DataFrame with base and engineered features (35 total features)
    """
    # Create base input dataframe
    input_data = pd.DataFrame({
        'humidity': [humidity],
        'ambient_temp': [ambient_temp],
        'wind_speed': [wind_speed],
        'visibility': [visibility],
        'pressure': [pressure],
        'cloud_ceiling': [cloud_ceiling],
        'month': [month],
        'hour': [hour],
        'altitude': [altitude],
        'latitude': [latitude],
        'longitude': [longitude]
    })
    
    # Engineer all features (basic + solar physics)
    input_data = engineer_features(input_data)
    
    return input_data