"""
Gauge Visualization Module
Creates speedometer-style gauge with blue-to-orange gradient
"""

import plotly.graph_objects as go
from utils.config import GAUGE_CONFIG, COLORS, LOCATION_STATS


def create_gauge(predicted_value, location):
    """
    Create a speedometer-style gauge showing predicted power output
    
    Features:
    - Blue (cold) to Orange (hot) gradient
    - Shows location's min, max, and average
    - Current prediction highlighted
    
    Parameters:
    -----------
    predicted_value : float
        Predicted power output in kW
    location : str
        Location name (e.g., 'camp_murray')
        
    Returns:
    --------
    plotly Figure object
    """
    # Get location statistics
    stats = LOCATION_STATS.get(location, {'min': 0, 'max': 35, 'mean': 15})
    loc_min = stats['min']
    loc_max = stats['max']
    loc_mean = stats['mean']
    
    # Gauge configuration
    gauge_min = GAUGE_CONFIG['min_value']
    gauge_max = GAUGE_CONFIG['max_value']
    
    # Create color gradient stops (Blue → Yellow → Orange)
    # 0-12 kW: Blue (cold, low energy)
    # 12-24 kW: Transition (blue → yellow)
    # 24-35 kW: Orange (hot, high energy)
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=predicted_value,
        domain={'x': [0, 1], 'y': [0, 1]},
        number={
            'suffix': " kW",
            'font': {'size': 48, 'color': COLORS['text_primary']}
        },
        gauge={
            'axis': {
                'range': [gauge_min, gauge_max],
                'tickwidth': 2,
                'tickcolor': COLORS['text_secondary'],
                'tickfont': {'size': 14}
            },
            'bar': {
                'color': COLORS['primary'],
                'thickness': 0.75
            },
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': COLORS['text_secondary'],
            'steps': [
                # Blue zone (0-12 kW) - Cold, low energy
                {'range': [0, 12], 'color': '#E3F2FD'},  # Light blue
                # Transition zone (12-24 kW)
                {'range': [12, 24], 'color': '#FFF9E6'},  # Light yellow
                # Orange zone (24-35 kW) - Hot, high energy
                {'range': [24, 35], 'color': '#FFE8CC'},  # Light orange
            ],
            'threshold': {
                'line': {'color': COLORS['accent'], 'width': 4},
                'thickness': 0.75,
                'value': predicted_value
            }
        }
    ))
    
    # Add location markers (min, max, average) as annotations
    annotations = []
    
    # Calculate positions on gauge (approximate arc positions)
    def value_to_angle(value):
        """Convert value to gauge angle (0-180 degrees)"""
        ratio = (value - gauge_min) / (gauge_max - gauge_min)
        return -90 + (180 * ratio)  # Start at -90°, end at +90°
    
    # Add markers for location stats
    marker_size = 12
    
    # Location minimum marker
    annotations.append(dict(
        x=0.5,
        y=0.15,
        xref='paper',
        yref='paper',
        text=f"<b>Location Range</b><br>Min: {loc_min:.1f} kW | Avg: {loc_mean:.1f} kW | Max: {loc_max:.1f} kW",
        showarrow=False,
        font=dict(size=12, color=COLORS['text_secondary']),
        align='center'
    ))
    
    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': COLORS['text_primary'], 'family': "Arial"},
        annotations=annotations
    )
    
    return fig


def get_performance_tier(predicted_value, location):
    """
    Determine performance tier based on predicted value and location average
    
    Parameters:
    -----------
    predicted_value : float
        Predicted power output
    location : str
        Location name
        
    Returns:
    --------
    tuple: (tier_name, tier_color, percentage_of_average)
    """
    stats = LOCATION_STATS.get(location, {'mean': 15})
    loc_mean = stats['mean']
    
    percentage = (predicted_value / loc_mean) * 100
    
    if percentage >= 120:
        return "Excellent", COLORS['success'], percentage
    elif percentage >= 80:
        return "Good", COLORS['primary'], percentage
    elif percentage >= 50:
        return "Fair", COLORS['secondary'], percentage
    else:
        return "Low", COLORS['gauge_cold'], percentage


def create_simple_comparison(predicted_value, location):
    """
    Create a simple comparison bar showing prediction vs location average
    
    Parameters:
    -----------
    predicted_value : float
        Predicted power output
    location : str
        Location name
        
    Returns:
    --------
    plotly Figure object
    """
    stats = LOCATION_STATS.get(location, {'mean': 15, 'min': 0, 'max': 35})
    loc_mean = stats['mean']
    
    fig = go.Figure()
    
    # Add bars
    fig.add_trace(go.Bar(
        x=[loc_mean, predicted_value],
        y=['Location Average', 'Your Prediction'],
        orientation='h',
        marker=dict(
            color=[COLORS['text_secondary'], COLORS['primary']],
            line=dict(width=2, color='white')
        ),
        text=[f'{loc_mean:.2f} kW', f'{predicted_value:.2f} kW'],
        textposition='auto',
    ))
    
    fig.update_layout(
        height=150,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(title='Power Output (kW)', range=[0, 35]),
        yaxis=dict(title=''),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text_primary'])
    )
    
    return fig
