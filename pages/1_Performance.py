"""
Performance Page - Model Performance Dashboard
Shows R² scores, MAE, RMSE, and comparisons across all locations
Dynamically loads metrics from trained models
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

# Add parent directory to path to find utils module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.config import APP_CONFIG, LOCATION_DATA, COLORS

# Page configuration
st.set_page_config(
    page_title=f"Performance - {APP_CONFIG['title']}",
    page_icon=APP_CONFIG['icon'],
    layout=APP_CONFIG['layout']
)

# Load custom CSS
try:
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except:
    pass

# Sidebar: Solar Image + Performance Summary
with st.sidebar:
    st.markdown("###")  # Add spacing
    
    # Solar panel image
    try:
        from PIL import Image
        solar_img = Image.open('images/solar.png')
        st.image(solar_img, use_container_width=True)
    except:
        try:
            solar_img = Image.open('images/solar2.png')
            st.image(solar_img, use_container_width=True)
        except:
            pass
    
    # Performance Summary Card
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%); 
                    padding: 1.5rem; border-radius: 10px; color: white; margin-top: 1rem;'>
            <h3 style='color: white; text-align: center; margin-bottom: 1rem;'>🎯 Performance Overview</h3>
            <hr style='border: 1px solid rgba(255,255,255,0.3); margin: 1rem 0;'>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>📊 Average R²:</strong> 0.65</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>🏆 Best Model:</strong> Travis (0.79)</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>✓ Tier 1:</strong> 4 locations</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>● Tier 2:</strong> 5 locations</p>
            <p style='margin: 0.5rem 0; font-size: 0.95rem;'><strong>● Tier 3:</strong> 3 locations</p>
            <hr style='border: 1px solid rgba(255,255,255,0.3); margin: 1rem 0;'>
            <p style='text-align: center; font-size: 0.85rem; margin-top: 1rem; font-style: italic;'>
                Each location has its own<br/>optimized algorithm
            </p>
            <details style='margin-top: 1rem; font-size: 0.82rem;'>
                <summary style='cursor: pointer; margin-bottom: 0.5rem;'>🔍 Model Selection Process</summary>
                <p style='margin: 0.5rem 0; line-height: 1.4;'>
                    <strong>Candidates:</strong> Linear, Ridge, Lasso, Gradient Boosting, Random Forest, XGBoost, LightGBM
                </p>
                <p style='margin: 0.5rem 0; line-height: 1.4;'>
                    <strong>Selection:</strong> Best model chosen per location using adjusted score = R² - (overfitting_gap × 0.2)
                </p>
                <p style='margin: 0.5rem 0; line-height: 1.4;'>
                    <strong>Validation:</strong> 80/20 train-test split with strong regularization to prevent overfitting
                </p>
            </details>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("###")  # Add spacing at bottom

# Page title
st.title("📊 Model Performance Dashboard")
st.markdown("Compare model accuracy and performance metrics across all 12 monitoring locations.")

# Collapsible Help Banner - Understanding Metrics
with st.expander("💡 Understanding Performance Metrics", expanded=False):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='background-color: {COLORS['primary']}15; padding: 1rem; border-radius: 8px; border-left: 4px solid {COLORS['primary']};'>
            <h4 style='color: {COLORS['primary']}; margin-top: 0;'>📊 R² Score</h4>
            <p><strong>What it means:</strong> Measures model accuracy</p>
            <p><strong>Range:</strong> 0 to 1 (higher = better)</p>
            <p><strong>Guide:</strong> 0.70+ Excellent, 0.60+ Good</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background-color: {COLORS['secondary']}15; padding: 1rem; border-radius: 8px; border-left: 4px solid {COLORS['secondary']};'>
            <h4 style='color: {COLORS['secondary']}; margin-top: 0;'>🎯 MAE</h4>
            <p><strong>What it means:</strong> Average prediction error</p>
            <p><strong>Range:</strong> Lower = better (0 = perfect)</p>
            <p><strong>Example:</strong> MAE = 2.5 kW → ±2.5 kW error</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background-color: {COLORS['accent']}15; padding: 1rem; border-radius: 8px; border-left: 4px solid {COLORS['accent']};'>
            <h4 style='color: {COLORS['accent']}; margin-top: 0;'>📈 RMSE</h4>
            <p><strong>What it means:</strong> Penalizes large errors</p>
            <p><strong>Range:</strong> Lower = better (0 = perfect)</p>
            <p><strong>Note:</strong> Always ≥ MAE, gap = variability</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.info("""
    **💡 Why Performance Varies by Location:**
    - **Climate Predictability** - Some locations have more consistent weather patterns
    - **Data Quality** - Measurement accuracy and completeness varies by site
    - **Seasonal Extremes** - Locations with dramatic seasonal swings are harder to model
    - **Unique Characteristics** - Hawaii (Kahului) and high-altitude sites (USAFA) present unique challenges
    """)

st.markdown("---")


@st.cache_data
def load_model_performance():
    """
    Load model performance metrics dynamically from pkl files
    Uses caching to avoid recomputing every time
    """
    try:
        from utils.model_performance_loader import get_model_performance
        performance, models = get_model_performance(
            models_dir=APP_CONFIG.get('models_dir', 'models'),
            data_dir=APP_CONFIG.get('data_dir', 'data/clean'),
            use_cached=True
        )
        return performance, models
    except Exception as e:
        st.error(f"Error loading model performance: {str(e)}")
        # Fallback to config values if dynamic loading fails
        from utils.config import MODEL_PERFORMANCE, BEST_MODELS
        return MODEL_PERFORMANCE, BEST_MODELS


# Load performance metrics
with st.spinner("Loading model performance metrics..."):
    MODEL_PERFORMANCE, BEST_MODELS = load_model_performance()

if not MODEL_PERFORMANCE:
    st.error("Could not load model performance metrics. Please check your model files.")
    st.stop()

# Add refresh button
col_refresh = st.columns([4, 1])[1]
with col_refresh:
    if st.button("🔄 Refresh Metrics", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

st.markdown("---")

# Prepare performance dataframe
perf_df = pd.DataFrame([
    {
        'Location': LOCATION_DATA[name]['display'],
        'State': LOCATION_DATA[name]['state'],
        'Model': BEST_MODELS.get(name, 'Unknown'),
        'R² Score': metrics['r2'],
        'MAE (kW)': metrics['mae'],
        'RMSE (kW)': metrics['rmse']
    }
    for name, metrics in MODEL_PERFORMANCE.items()
]).sort_values('R² Score', ascending=False)

# Summary metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average R²",
        f"{perf_df['R² Score'].mean():.3f}",
        help="Average R² score across all locations"
    )

with col2:
    st.metric(
        "Best Model",
        f"{perf_df.iloc[0]['Location']}",
        f"R²: {perf_df.iloc[0]['R² Score']:.3f}",
        help="Location with highest R² score"
    )

with col3:
    st.metric(
        "Average MAE",
        f"{perf_df['MAE (kW)'].mean():.2f} kW",
        help="Average Mean Absolute Error"
    )

with col4:
    st.metric(
        "Average RMSE",
        f"{perf_df['RMSE (kW)'].mean():.2f} kW",
        help="Average Root Mean Squared Error"
    )

st.markdown("---")

# R² Score Comparison Chart
st.subheader("R² Score by Location")
fig_r2 = px.bar(
    perf_df,
    x='Location',
    y='R² Score',
    color='R² Score',
    color_continuous_scale=['#2196F3', '#FFA726', '#F39C12'],
    title='Model Performance (R² Score) Across Locations',
    labels={'R² Score': 'R² Score (higher is better)'}
)
fig_r2.update_layout(
    xaxis_tickangle=-45,
    height=400,
    showlegend=False,
    font=dict(size=12)
)
st.plotly_chart(fig_r2, use_container_width=True)

st.markdown("---")

# Error Metrics Comparison
col1, col2 = st.columns(2)

with col1:
    st.subheader("Mean Absolute Error (MAE)")
    fig_mae = px.bar(
        perf_df.sort_values('MAE (kW)'),
        x='Location',
        y='MAE (kW)',
        color='MAE (kW)',
        color_continuous_scale=['#27AE60', '#FFA726', '#E67E22'],
        title='MAE by Location (lower is better)'
    )
    fig_mae.update_layout(xaxis_tickangle=-45, height=350, showlegend=False)
    st.plotly_chart(fig_mae, use_container_width=True)

with col2:
    st.subheader("Root Mean Squared Error (RMSE)")
    fig_rmse = px.bar(
        perf_df.sort_values('RMSE (kW)'),
        x='Location',
        y='RMSE (kW)',
        color='RMSE (kW)',
        color_continuous_scale=['#27AE60', '#FFA726', '#E67E22'],
        title='RMSE by Location (lower is better)'
    )
    fig_rmse.update_layout(xaxis_tickangle=-45, height=350, showlegend=False)
    st.plotly_chart(fig_rmse, use_container_width=True)

st.markdown("---")

# Model Distribution
st.subheader("Model Type Distribution")
model_counts = perf_df['Model'].value_counts()

# Define HIGHLY distinct colors - maximum contrast
distinct_colors = {
    'Ridge': '#FF6B35',           # Bright Orange-Red
    'GradientBoosting': '#004E89', # Deep Blue
    'Linear': '#1DD3B0',          # Bright Teal
    'XGBoost': '#B45FCF',         # Bright Purple
    'RandomForest': '#FFD23F',    # Bright Yellow
    'Lasso': '#06A77D',           # Green
    'LightGBM': '#D62246'         # Crimson Red
}

# Create color list based on actual models in data
pie_colors = [distinct_colors.get(model, COLORS['primary']) for model in model_counts.index]

fig_models = px.pie(
    values=model_counts.values,
    names=model_counts.index,
    title='Distribution of Model Types Across Locations',
    color_discrete_sequence=pie_colors
)
fig_models.update_traces(
    textposition='inside', 
    textinfo='percent+label',
    textfont_size=14,
    marker=dict(line=dict(color='white', width=2))  # Add white borders for clarity
)
st.plotly_chart(fig_models, use_container_width=True)

st.markdown("---")

# Detailed Performance Table
st.subheader("Detailed Performance Metrics")
st.dataframe(
    perf_df.style.background_gradient(subset=['R² Score'], cmap='RdYlGn')
                .format({
                    'R² Score': '{:.4f}',
                    'MAE (kW)': '{:.2f}',
                    'RMSE (kW)': '{:.2f}'
                }),
    use_container_width=True,
    hide_index=True
)

# Performance Tiers
st.markdown("---")
st.subheader("Performance Tiers")

tier_1 = perf_df[perf_df['R² Score'] >= 0.70]
tier_2 = perf_df[(perf_df['R² Score'] >= 0.60) & (perf_df['R² Score'] < 0.70)]
tier_3 = perf_df[perf_df['R² Score'] < 0.60]

col1, col2, col3 = st.columns(3)

with col1:
    st.success(f"""
    **✓ Tier 1 - Excellent (R² ≥ 0.70)**
    
    {tier_1.shape[0]} locations
    
    {', '.join(tier_1['Location'].tolist())}
    """)

with col2:
    st.info(f"""
    **● Tier 2 - Good (0.60 ≤ R² < 0.70)**
    
    {tier_2.shape[0]} locations
    
    {', '.join(tier_2['Location'].tolist())}
    """)

with col3:
    st.warning(f"""
    **● Tier 3 - Fair (R² < 0.60)**
    
    {tier_3.shape[0]} locations
    
    {', '.join(tier_3['Location'].tolist())}
    """)

# Footer
st.markdown("---")
st.markdown(
    f"""
    <div style='text-align: center; color: {COLORS['text_secondary']}; padding: 1rem 0;'>
        <p style='font-size: 0.9rem;'>
            <strong>Note:</strong> R² scores indicate how well the model explains variance in solar power output. 
            MAE and RMSE show average prediction errors in kilowatts.
        </p>
        <p style='font-size: 0.8rem;'>
            <i>Metrics are dynamically calculated from trained models and cached for performance.</i>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)