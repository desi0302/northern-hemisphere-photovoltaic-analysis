"""
Configuration file for Solar Power Prediction App
Contains all constants, colors, location data, and app settings
"""

# ============================================================================
# COLOR SCHEME - Professional Solar Theme
# ============================================================================

COLORS = {
    'primary': '#F39C12',      # Solar Orange
    'secondary': '#E67E22',    # Carrot Orange
    'accent': '#D68910',       # Dark Gold
    'success': '#27AE60',      # Green
    
    # Gauge gradient (Cold Blue → Hot Orange)
    'gauge_cold': '#2196F3',   # Sky Blue (low energy)
    'gauge_warm': '#FF9800',   # Orange (high energy)
    
    # UI elements
    'background': '#FFFFFF',
    'text_primary': '#2C3E50',
    'text_secondary': '#7F8C8D',
}

# ============================================================================
# LOCATION DATA - 12 Military Installation Sites
# ============================================================================

LOCATION_DATA = {
    'camp_murray': {
        'display': 'Camp Murray',
        'lat': 47.11,
        'lon': -122.57,
        'alt': 84,
        'state': 'Washington'
    },
    'grissom': {
        'display': 'Grissom',
        'lat': 40.65,
        'lon': -86.15,
        'alt': 250,
        'state': 'Indiana'
    },
    'hill_weber': {
        'display': 'Hill Weber',
        'lat': 41.12,
        'lon': -111.97,
        'alt': 1459,
        'state': 'Utah'
    },
    'jdmt': {
        'display': 'JDMT',
        'lat': 26.98,
        'lon': -80.11,
        'alt': 2,
        'state': 'Florida'
    },
    'kahului': {
        'display': 'Kahului',
        'lat': 20.89,
        'lon': -156.44,
        'alt': 2,
        'state': 'Hawaii'
    },
    'malmstrom': {
        'display': 'Malmstrom',
        'lat': 47.52,
        'lon': -111.18,
        'alt': 1043,
        'state': 'Montana'
    },
    'march_afb': {
        'display': 'March AFB',
        'lat': 33.88,
        'lon': -117.25,
        'alt': 470,
        'state': 'California'
    },
    'mnang': {
        'display': 'MNANG',
        'lat': 44.88,
        'lon': -93.21,
        'alt': 262,
        'state': 'Minnesota'
    },
    'offutt': {
        'display': 'Offutt',
        'lat': 41.12,
        'lon': -95.91,
        'alt': 321,
        'state': 'Nebraska'
    },
    'peterson': {
        'display': 'Peterson',
        'lat': 38.82,
        'lon': -104.71,
        'alt': 1879,
        'state': 'Colorado'
    },
    'travis': {
        'display': 'Travis',
        'lat': 38.16,
        'lon': -121.56,
        'alt': 1,
        'state': 'California'
    },
    'usafa': {
        'display': 'USAFA',
        'lat': 38.95,
        'lon': -104.83,
        'alt': 1947,
        'state': 'Colorado'
    }
}

# ============================================================================
# BEST MODELS PER LOCATION (from ML training results)
# ============================================================================

BEST_MODELS = {
    'camp_murray': 'Ridge',
    'grissom': 'Linear',
    'hill_weber': 'XGBoost',
    'jdmt': 'GradientBoosting',
    'kahului': 'Ridge',
    'malmstrom': 'Ridge',
    'march_afb': 'Linear',
    'mnang': 'GradientBoosting',
    'offutt': 'Ridge',
    'peterson': 'RandomForest',
    'travis': 'GradientBoosting',
    'usafa': 'Ridge'
}

# ============================================================================
# MODEL PERFORMANCE METRICS (from ML training - UPDATED)
# ============================================================================

MODEL_PERFORMANCE = {
    'camp_murray': {'r2': 0.7423, 'mae': 2.56, 'rmse': 3.58},
    'grissom': {'r2': 0.6988, 'mae': 2.68, 'rmse': 3.61},
    'hill_weber': {'r2': 0.7260, 'mae': 2.40, 'rmse': 3.60},
    'jdmt': {'r2': 0.5862, 'mae': 3.49, 'rmse': 4.68},
    'kahului': {'r2': 0.4405, 'mae': 4.72, 'rmse': 5.80},
    'malmstrom': {'r2': 0.6963, 'mae': 2.77, 'rmse': 3.90},
    'march_afb': {'r2': 0.6342, 'mae': 2.00, 'rmse': 2.93},
    'mnang': {'r2': 0.7126, 'mae': 2.74, 'rmse': 4.14},
    'offutt': {'r2': 0.6418, 'mae': 3.94, 'rmse': 4.97},
    'peterson': {'r2': 0.6089, 'mae': 2.87, 'rmse': 4.22},
    'travis': {'r2': 0.7910, 'mae': 1.89, 'rmse': 3.07},
    'usafa': {'r2': 0.5025, 'mae': 2.98, 'rmse': 4.12}
}

# ============================================================================
# LOCATION STATISTICS (typical ranges from training data)
# ============================================================================

LOCATION_STATS = {
    'camp_murray': {'mean': 10.78, 'min': 0.32, 'max': 30.14},
    'grissom': {'mean': 9.43, 'min': 0.32, 'max': 28.99},
    'hill_weber': {'mean': 11.19, 'min': 0.35, 'max': 29.47},
    'jdmt': {'mean': 18.40, 'min': 0.64, 'max': 34.29},
    'kahului': {'mean': 15.22, 'min': 0.57, 'max': 32.09},
    'malmstrom': {'mean': 9.89, 'min': 0.30, 'max': 28.59},
    'march_afb': {'mean': 13.76, 'min': 0.31, 'max': 26.18},
    'mnang': {'mean': 9.64, 'min': 0.40, 'max': 29.08},
    'offutt': {'mean': 11.33, 'min': 0.48, 'max': 29.39},
    'peterson': {'mean': 11.71, 'min': 0.27, 'max': 29.39},
    'travis': {'mean': 13.30, 'min': 0.28, 'max': 30.42},
    'usafa': {'mean': 12.85, 'min': 0.38, 'max': 30.47}
}

# ============================================================================
# QUICK PRESETS - Generic weather scenarios
# ============================================================================

PRESETS = {
    'sunny': {
        'name': '☀️ Sunny Day',
        'humidity': 30.0,
        'ambient_temp': 25.0,
        'wind_speed': 5,
        'visibility': 10.0,
        'pressure': 1013,
        'cloud_ceiling': 700,
        'month': 6,
        'hour': 12,
        'description': 'Clear sky, optimal solar conditions'
    },
    'cloudy': {
        'name': '☁️ Cloudy Day',
        'humidity': 75.0,
        'ambient_temp': 18.0,
        'wind_speed': 8,
        'visibility': 6.0,
        'pressure': 1010,
        'cloud_ceiling': 100,
        'month': 11,
        'hour': 14,
        'description': 'Overcast, reduced solar output'
    },
    'winter': {
        'name': '❄️ Winter',
        'humidity': 50.0,
        'ambient_temp': 5.0,
        'wind_speed': 10,
        'visibility': 8.0,
        'pressure': 1020,
        'cloud_ceiling': 400,
        'month': 1,
        'hour': 12,
        'description': 'Cold, short daylight'
    },
    'summer': {
        'name': '🌻 Summer',
        'humidity': 40.0,
        'ambient_temp': 30.0,
        'wind_speed': 6,
        'visibility': 10.0,
        'pressure': 1010,
        'cloud_ceiling': 600,
        'month': 7,
        'hour': 13,
        'description': 'Hot, long daylight'
    }
}

# ============================================================================
# INPUT RANGES (expanded to match training data)
# ============================================================================

INPUT_RANGES = {
    'humidity': {'min': 0.0, 'max': 100.0, 'step': 1.0, 'default': 50.0},
    'ambient_temp': {'min': -20.0, 'max': 50.0, 'step': 0.5, 'default': 20.0},
    'wind_speed': {'min': 0, 'max': 30, 'step': 1, 'default': 5},
    'visibility': {'min': 0.0, 'max': 20.0, 'step': 0.5, 'default': 10.0},
    'pressure': {'min': 850, 'max': 1050, 'step': 1, 'default': 1013},
    'cloud_ceiling': {'min': 0, 'max': 722, 'step': 10, 'default': 300},
}

# Input validation hints
INPUT_HINTS = {
    'humidity': 'Typical: 30-80%',
    'ambient_temp': 'Typical: 5-35°C',
    'wind_speed': 'Typical: 0-15 m/s',
    'visibility': 'Typical: 5-10 km',
    'pressure': 'Typical: 980-1030 hPa',
    'cloud_ceiling': 'Typical: 100-600 feet AGL',
}

# ============================================================================
# GAUGE SETTINGS
# ============================================================================

GAUGE_CONFIG = {
    'min_value': 0,
    'max_value': 35,  # kW - covers all locations
    'cold_zone': 12,  # 0-12 kW (blue)
    'warm_zone': 24,  # 24-35 kW (orange)
}

# ============================================================================
# APP SETTINGS
# ============================================================================

APP_CONFIG = {
    'title': 'Solar Power Prediction System',
    'icon': '☀️',
    'layout': 'wide',
    'models_dir': 'models',
    'data_dir': 'data/clean',
    'page_names': {
        'home': 'About',
        'predict': 'Predict',
        'performance': 'Performance',
        'insights': 'Insights'
    }
}

# ============================================================================
# MONTH AND HOUR LABELS
# ============================================================================

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# ============================================================================
# ABOUT PAGE CONTENT
# ============================================================================

ABOUT_CONTENT = {
    'title': 'Northern Hemisphere Photovoltaic Analysis',
    'subtitle': 'Machine Learning-Based Solar Power Prediction System',
    
    'overview': """
    This application predicts solar power output (kW) based on environmental conditions 
    at 12 military installation sites across the Northern Hemisphere. The system employs 
    site-specific machine learning models trained on real-world photovoltaic performance data.
    """,
    
    'data_sources': """
    **Data Collection:**
    - 12 military installation monitoring sites
    - Northern Hemisphere locations (USA)
    - 20,993 total observations
    - Environmental and power generation measurements
    
    **Features Measured:**
    - Humidity (%)
    - Ambient Temperature (°C)
    - Wind Speed (m/s)
    - Visibility (km)
    - Atmospheric Pressure (hPa)
    - Cloud Ceiling (feet above ground level)
    - Temporal factors (month, hour)
    - Geographic coordinates (latitude, longitude, altitude)
    """,
    
    'methodology': """
    **Approach:**
    
    A key finding from exploratory data analysis revealed that location explains significant 
    variance in solar power output, with the best-performing site producing roughly twice 
    the output of the worst-performing site. This led to a site-specific modeling strategy 
    rather than a single global model.
    
    **Model Development:**
    - 12 independent models (one per location)
    - Per-site train/test split (80/20)
    - Multiple algorithms evaluated: Linear Regression, Ridge, Lasso, Gradient Boosting, 
      Random Forest, XGBoost
    - Best model selected per location based on test R² score and overfitting gap
    - Feature engineering: interaction terms and cyclic time encodings
    - Proper scaling applied (StandardScaler for linear models)
    - Rigorous prevention of data leakage
    """,
    
    'models_used': """
    **Model Distribution:**
    - Gradient Boosting: 7 locations (most common)
    - Linear Regression: 2 locations
    - Lasso Regression: 2 locations
    - Random Forest: 1 location
    
    Each location's model was independently optimized for its unique climate patterns 
    and geographic characteristics.
    """,
    
    'performance': """
    **Overall Performance:**
    - Average R² Score: 0.65
    - Best Performing: Travis (R² = 0.79)
    - Model Performance Range: R² = 0.44 to 0.79
    
    Performance varies by location due to differences in climate predictability, 
    data quality, and site-specific factors.
    """,
    
    'limitations': """
    **Model Limitations:**
    
    - Models are trained on historical data and may not capture unprecedented weather patterns
    - Predictions assume normal panel operation (no degradation, soiling, or technical failures)
    - Geographic applicability limited to Northern Hemisphere military installations
    - Seasonal and diurnal patterns captured but extreme events may reduce accuracy
    - Models do not account for panel orientation, tilt angle, or shading
    - Input ranges should stay within training data bounds for reliable predictions
    
    **Use Cases:**
    - Energy production forecasting
    - Site performance comparison
    - Environmental impact assessment
    - Educational demonstrations
    
    **Not Suitable For:**
    - Real-time operational control
    - Financial investment decisions (without validation)
    - Safety-critical applications
    """,
    
    'disclaimer': """
    **Disclaimer:**
    
    This application provides predictions based on statistical machine learning models. 
    Predictions are estimates and should not be considered guarantees of actual power output. 
    Users should validate predictions against site-specific conditions and consult with 
    qualified professionals for critical applications.
    """
}
