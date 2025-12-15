"""
Solar Dashboard - Project Overview and Dataset Information
"""

import streamlit as st
import sys
import os
import pandas as pd
import plotly.graph_objects as go
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.config import APP_CONFIG, COLORS, LOCATION_DATA

st.set_page_config(
    page_title=APP_CONFIG['title'],
    page_icon=APP_CONFIG['icon'],
    layout=APP_CONFIG['layout']
)

# Load CSS
try:
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except:
    pass

# Sidebar: Project Stats + Solar Image
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
    
    # Project Stats Card
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%); 
                    padding: 1.5rem; border-radius: 10px; color: white; margin-top: 1rem;'>
            <h3 style='color: white; text-align: center; margin-bottom: 1rem;'>📊 Project Stats</h3>
            <hr style='border: 1px solid rgba(255,255,255,0.3); margin: 1rem 0;'>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>🌍 Locations:</strong> 12 Sites</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>📈 Observations:</strong> 20,993</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>🤖 ML Models:</strong> 12 Models</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>⚡ Avg R²:</strong> 0.65</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>🏆 Best Site:</strong> Travis (0.79)</p>
            <hr style='border: 1px solid rgba(255,255,255,0.3); margin: 1rem 0;'>
            <p style='text-align: center; font-size: 0.85rem; margin-top: 1rem; font-style: italic;'>
                Location-specific modeling<br/>for optimal accuracy
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("###")  # Add spacing at bottom

# Header
st.title(f"{APP_CONFIG['icon']} Northern Hemisphere Solar Power Prediction")
st.markdown("### Machine Learning-Based Photovoltaic Power Output Prediction System")

# Collapsible Help Banner
with st.expander("💡 Quick Guide - About This Project", expanded=False):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='background-color: {COLORS['primary']}15; padding: 1rem; border-radius: 8px; border-left: 4px solid {COLORS['primary']};'>
            <h4 style='color: {COLORS['primary']}; margin-top: 0;'>🌍 What is This?</h4>
            <p>A machine learning system that predicts solar power output based on weather conditions at 12 military installations across the United States.</p>
            <p><strong>Data Period:</strong> 2017-2018<br/>
            <strong>Total Data:</strong> 20,993 observations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background-color: {COLORS['secondary']}15; padding: 1rem; border-radius: 8px; border-left: 4px solid {COLORS['secondary']};'>
            <h4 style='color: {COLORS['secondary']}; margin-top: 0;'>🎯 Why Location-Specific?</h4>
            <p>Each site has its own model because climate conditions vary dramatically:</p>
            <p>• 2:1 performance ratio between sites<br/>
            • Different seasonal patterns<br/>
            • Location explains 11% of variance</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background-color: {COLORS['accent']}15; padding: 1rem; border-radius: 8px; border-left: 4px solid {COLORS['accent']};'>
            <h4 style='color: {COLORS['accent']}; margin-top: 0;'>🚀 How to Use</h4>
            <p><strong>Dashboard:</strong> Explore data and findings<br/>
            <strong>Predict:</strong> Get power predictions<br/>
            <strong>Performance:</strong> View model accuracy</p>
            <p style='margin-top: 1rem;'><em>Navigate using the sidebar menu</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.info("""
    **📚 Key Features:**
    - **12 Independent Models** - One optimized model per location
    - **Advanced Features** - Incorporates solar physics and atmospheric conditions  
    - **Real-time Predictions** - Based on current environmental inputs
    - **PDF Reports** - Download professional prediction reports
    """)

st.markdown("---")

# Project Overview
st.header("Project Overview")
st.markdown("""
This application predicts solar power output (kW) using machine learning models trained on real-world 
photovoltaic performance data from **12 military installations** across the Northern Hemisphere. 

The system employs **location-specific models** rather than a single global model, based on the critical 
finding that different sites operate under distinct climate regimes with non-transferable patterns.

**Key Features:**
- 12 independent ML models optimized for each location
- Advanced feature engineering incorporating solar physics
- Real-time predictions based on environmental conditions
- Professional PDF report generation
- Comprehensive performance metrics and visualizations
""")

st.markdown("---")

# Dataset Information
st.header("Dataset Information")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    **Data Source:**  
    [Northern Hemisphere Horizontal Photovoltaic Dataset](https://www.kaggle.com/datasets/saurabhshahane/northern-hemisphere-horizontal-photovoltaic)
    
    **Collection Period:** 2017-2018  
    **Total Observations:** 20,993  
    **Geographic Coverage:** 12 sites across the United States
    
    **Measured Features:**
    - Environmental: Humidity, Temperature, Wind Speed, Visibility, Pressure, Cloud Ceiling
    - Temporal: Month, Hour, Day of Year
    - Geographic: Latitude, Longitude, Altitude
    - Target: Solar Power Output (kW)
    """)

with col2:
    st.metric("Locations", "12 Sites")
    st.metric("Observations", "20,993")
    st.metric("Average R²", "0.65")
    st.metric("Best R²", "0.79")

st.markdown("---")

# Monitoring Locations Table
st.header("Monitoring Locations")

# Create locations dataframe
locations_df = pd.DataFrame([
    {
        'Location': data['display'],
        'State': data['state'],
        'Latitude': data['lat'],
        'Longitude': data['lon'],
        'Altitude (m)': data['alt']
    }
    for name, data in LOCATION_DATA.items()
]).sort_values('State')

st.dataframe(
    locations_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# Interactive Map
st.subheader("Geographic Distribution")

# Create map with all 12 locations
fig_map = go.Figure()

# Add markers for each location
for name, data in LOCATION_DATA.items():
    fig_map.add_trace(go.Scattergeo(
        lon=[data['lon']],
        lat=[data['lat']],
        text=data['display'],
        name=data['display'],
        mode='markers+text',
        marker=dict(
            size=12,
            color=COLORS['primary'],
            line=dict(width=2, color='white')
        ),
        textposition="top center",
        textfont=dict(size=10, color=COLORS['text_primary']),
        hovertemplate=f"<b>{data['display']}</b><br>" +
                     f"State: {data['state']}<br>" +
                     f"Lat: {data['lat']}°<br>" +
                     f"Lon: {data['lon']}°<br>" +
                     f"Alt: {data['alt']}m<br>" +
                     "<extra></extra>"
    ))

fig_map.update_layout(
    title='12 Military Installation Sites',
    geo=dict(
        scope='usa',
        projection_type='albers usa',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        coastlinecolor='rgb(204, 204, 204)',
        showlakes=True,
        lakecolor='rgb(230, 245, 255)',
        showcountries=True,
        countrycolor='rgb(204, 204, 204)'
    ),
    height=500,
    showlegend=False,
    margin=dict(l=0, r=0, t=40, b=0)
)

st.plotly_chart(fig_map, use_container_width=True)

st.markdown("---")

# Key Findings from EDA
st.header("Key Findings from Exploratory Data Analysis")

st.markdown("""
### Feature Importance Summary

The analysis revealed that solar power output is primarily driven by temporal and environmental factors, 
with **location playing a critical role** in determining baseline performance.
""")

# Feature importance table
findings_data = {
    'Feature': ['Month (Season)', 'Location', 'Cloud Ceiling', 'Humidity', 'Visibility', 
                'Hour', 'Hour × Month', 'Altitude'],
    'Effect Size': ['η² = 0.160', 'η² = 0.112', 'r = +0.42', 'r = -0.40', 'r = +0.35', 
                    'η² = 0.045', 'p < 0.001', 'ε² = 0.005'],
    'Variance Explained': ['16.0%', '11.2%', '~18%', '~16%', '~12%', '4.5%', '0.4%', '0.5%'],
    'Status': ['✓ Critical', '✓ Critical', '✓ Strong', '✓ Strong', '✓ Moderate', 
               '✓ Important', '✓ Interaction', '✗ Negligible']
}

findings_df = pd.DataFrame(findings_data)
st.dataframe(findings_df, use_container_width=True, hide_index=True)

st.markdown("**Variance breakdown:** Temporal (21%) + Environmental (30-40%) + Location (11%) = ~62-72% explained")

st.markdown("---")

# NEW SECTION: Exploratory Data Analysis Highlights
st.subheader("Exploratory Data Analysis Highlights")

st.markdown("""
Visual analysis of the dataset reveals distinct patterns in solar power generation across locations, 
temporal dimensions, and environmental conditions.
""")

# Image 1: Total Energy Production by Location
try:
    img1 = Image.open('images/1.png')
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img1, use_container_width=True)
    st.markdown("""
    **Total Energy Production by Location**
    
    The pie chart shows significant variation in energy contribution across the 12 sites. Travis, Hill Weber, 
    JDMT, and USAFA are the largest contributors, each accounting for over 12% of total energy production. 
    The distribution reflects both the performance characteristics and data collection periods at each installation, 
    highlighting the importance of location-specific modeling approaches.
    """)
    st.markdown("")
except:
    st.info("Place image 1.png in the images/ folder to display the energy production distribution chart.")

# Image 2: Temporal Patterns
try:
    img2 = Image.open('images/2.png')
    st.image(img2, use_container_width=True)
    st.markdown("""
    **Temporal Patterns in Solar Power Generation**
    
    Three complementary visualizations reveal temporal dynamics: **(1) Hour of Day** shows peak production 
    around 13:00 (1 PM) with a characteristic bell curve from sunrise to sunset. **(2) Monthly Distribution** 
    demonstrates higher median output during summer months (May-August) with winter months showing compressed 
    ranges. **(3) Seasonal Patterns** clearly distinguish winter's low baseline from summer's peak performance, 
    with spring and autumn showing transitional characteristics. These patterns validate hypothesis H3 
    (summer midday peaks) with strong statistical support.
    """)
    st.markdown("")
except:
    st.info("Place image 2.png in the images/ folder to display temporal pattern charts.")

# Image 3: Hour × Month Interaction
try:
    img3 = Image.open('images/3.png')
    st.image(img3, use_container_width=True)
    st.markdown("""
    **Hour × Month Interaction Effects**
    
    The interaction heatmap reveals the combined influence of time and season on power output. Peak values 
    (18+ kW) occur during midday hours (11-14) in summer months (May-July), shown in dark purple. Winter months 
    (November-February) show consistently lower output across all hours. The line plots emphasize that monthly 
    patterns vary substantially by hour, and hourly patterns shift dramatically across months, demonstrating 
    why this interaction term explains 0.4% additional variance (p < 0.001) beyond individual effects.
    """)
    st.markdown("")
except:
    st.info("Place image 3.png in the images/ folder to display interaction heatmaps.")

# Image 4: Environmental Correlations
try:
    img4 = Image.open('images/4.png')
    st.image(img4, use_container_width=True)
    st.markdown("""
    **Environmental Factors vs Solar Power Output**
    
    Scatter plots reveal weak-to-moderate correlations between environmental variables and power output. 
    **Visibility** shows the strongest positive relationship (r = 0.205), with clear skies (high visibility) 
    associated with higher output. **Wind Speed** (r = 0.071) and **Atmospheric Pressure** (r = 0.073) show 
    very weak correlations, suggesting these variables contribute minimally to prediction accuracy. The vertical 
    banding patterns reflect diurnal cycles and seasonal variations captured more effectively by temporal features. 
    These findings support the use of cloud ceiling and humidity as primary environmental predictors.
    """)
    st.markdown("")
except:
    st.info("Place image 4.png in the images/ folder to display environmental correlation plots.")

st.markdown("---")

# Hypothesis Testing
st.subheader("Hypothesis Testing Results")

hypothesis_data = {
    'Hypothesis': [
        'H1: Humidity reduces output',
        'H2: Clear skies increase output',
        'H3: Summer midday peaks',
        'H4: Altitude affects efficiency',
        'H5: Location matters'
    ],
    'Result': ['✅ SUPPORTED', '✅ SUPPORTED', '✅ STRONGLY SUPPORTED', '❌ REJECTED', '✅ STRONGLY SUPPORTED'],
    'Evidence': [
        'r = -0.40 (moderate)',
        'r = +0.42 (moderate)',
        'F = 347 (month), F = 168 (hour), interaction p < 0.001',
        'ε² = 0.005 (negligible, spurious)',
        'η² = 0.112, F = 240, 2:1 ratio'
    ]
}

hypothesis_df = pd.DataFrame(hypothesis_data)
st.dataframe(hypothesis_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Critical Finding
st.subheader("Critical Finding: Site-Specific Performance Heterogeneity")

st.warning("""
**Location performance varies dramatically** with a 2:1 ratio between best and worst performing sites.  
This led to the strategic decision to build **12 location-specific models** rather than a single global model.
""")

performance_data = {
    'Site': ['JDMT', 'Kahului', 'Hill Weber', 'Grissom'],
    'Mean Output (kW)': [18.57, 15.22, 14.44, 9.43],
    'Climate Type': ['Subtropical Florida', 'Tropical Hawaii', 'High-altitude Utah', 'Midwest Indiana'],
    'Relative Performance': ['Best (+97% vs worst)', 'High', 'High', 'Worst']
}

performance_df = pd.DataFrame(performance_data)
st.dataframe(performance_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Why Location-Specific Models
st.subheader("Why Location-Specific Models Are Necessary")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **1. Different Production Baselines**
    - JDMT's average (18.57 kW) exceeds Grissom's 90th percentile
    - Global models would systematically mispredict
    
    **2. Climate-Specific Interactions**
    - Humidity impact varies by baseline climate
    - Cloud effects differ coastal vs inland
    
    **3. Seasonal Response Differences**
    - Northern sites: 4× winter-to-summer variation
    - Southern sites: 1.7× variation
    """)

with col2:
    st.markdown("""
    **4. Data Imbalance**
    - Travis (2,746 obs) vs MNANG (780 obs)
    - 3.5× difference affects global models
    
    **5. Location Effect Size**
    - η² = 0.112 is 10× larger than altitude
    - 2.5× larger than hour effect
    - Cannot be captured by other features
    """)

st.markdown("---")

# 3D Environmental Analysis
st.header("3D Environmental Analysis")
st.markdown("Interactive visualization showing relationships between environmental factors and solar power output")

try:
    # Load and display 3D HTML chart
    html_path = 'jupyter_notebooks/plots/3d_environmental_analysis.html'
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)
    else:
        st.info("3D chart will be displayed here. Place the file at: jupyter_notebooks/plots/3d_environmental_analysis.html")
except Exception as e:
    st.error(f"Error loading 3D chart: {str(e)}")

st.markdown("---")

# Model Strategy
st.header("Modeling Strategy")

st.markdown("""
**Approach: 12 Location-Specific Models**

**Why location-specific:**
- Location explains 11.2% of variance (comparable to all temporal features combined at 21%)
- 2:1 performance ratio between sites
- Climate regimes differ fundamentally
- Non-transferable environmental relationships

**Feature Engineering:**
- Cyclic encoding for temporal features (hour, month)
- Solar physics calculations (elevation, day length, temperature efficiency)
- Atmospheric attenuation factors (cloud, humidity)
- Environmental interaction terms

**Model Selection:**
- Tested: Linear Regression, Ridge, Lasso, Gradient Boosting, Random Forest, XGBoost
- Best model selected per location based on R² and overfitting gap
- Proper scaling applied for linear models
- Rigorous prevention of data leakage

**Validation:**
- Per-site train/test split (80/20)
- Temporal validation to test on future data
- Performance metrics: R², MAE, RMSE
""")

st.markdown("---")

# Limitations
st.header("⚠️ Important Limitations")

st.markdown("""
**Model Limitations:**
- Models trained on historical data (2017-2018) may not capture unprecedented weather patterns
- Predictions assume normal panel operation (no degradation, soiling, or failures)
- Geographic applicability limited to Northern Hemisphere military installations
- Does not account for panel orientation, tilt angle, or shading
- Input ranges should stay within training data bounds for reliable predictions

**Appropriate Use Cases:**
- Energy production forecasting and planning
- Site performance comparison and analysis
- Environmental impact assessment
- Educational demonstrations and research

**Not Suitable For:**
- Real-time operational control systems
- Financial investment decisions without validation
- Safety-critical applications
- Locations significantly different from training sites
""")

st.markdown("---")

# Footer
st.markdown(
    f"""
    <div style='text-align: center; color: {COLORS['text_secondary']}; padding: 1rem 0;'>
        <p><strong>Northern Hemisphere Photovoltaic Analysis</strong></p>
        <p>Machine learning predictions based on environmental conditions and temporal patterns</p>
        <p style='font-size: 0.9rem;'><i>Developed by Desi Ilieva | 2025</i></p>
        <p style='font-size: 0.85rem;'>For educational and research purposes</p>
    </div>
    """,
    unsafe_allow_html=True
)