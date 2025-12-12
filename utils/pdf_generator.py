"""
PDF Report Generator
Creates professional prediction reports
"""

from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from utils.config import COLORS, MONTHS, LOCATION_STATS, MODEL_PERFORMANCE


def generate_prediction_report(location, location_data, inputs, prediction, 
                               model_name, tier_name, percentage):
    """Generate PDF report for a prediction"""
    
    buffer = BytesIO()
    
    doc = SimpleDocTemplate(
        buffer, pagesize=letter,
        rightMargin=0.75*inch, leftMargin=0.75*inch,
        topMargin=1*inch, bottomMargin=0.75*inch
    )
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle', parent=styles['Heading1'],
        fontSize=24, textColor=colors.HexColor(COLORS['primary']),
        spaceAfter=12, alignment=TA_CENTER, fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle', parent=styles['Normal'],
        fontSize=14, textColor=colors.HexColor(COLORS['text_secondary']),
        spaceAfter=20, alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading', parent=styles['Heading2'],
        fontSize=16, textColor=colors.HexColor(COLORS['primary']),
        spaceAfter=12, spaceBefore=12, fontName='Helvetica-Bold'
    )
    
    # Header
    elements.append(Paragraph("Solar Power Prediction Report", title_style))
    elements.append(Paragraph("Northern Hemisphere Photovoltaic Analysis", subtitle_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Prediction Result - FIXED LAYOUT
    prediction_data = [
        ['Predicted Solar Power Output'],
        [f'{prediction:.2f} kW']
    ]
    prediction_table = Table(prediction_data, colWidths=[6*inch], rowHeights=[0.4*inch, 0.8*inch])
    prediction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(COLORS['primary'])),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, 1), 32),
        ('BOTTOMPADDING', (0, 0), (0, 0), 12),
        ('TOPPADDING', (0, 0), (0, 0), 12),
        ('BOTTOMPADDING', (0, 1), (0, 1), 20),
        ('TOPPADDING', (0, 1), (0, 1), 20),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#FFF9E6')),
        ('TEXTCOLOR', (0, 1), (-1, 1), colors.HexColor(COLORS['primary'])),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor(COLORS['primary']))
    ]))
    elements.append(prediction_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Location Information
    elements.append(Paragraph("Location Information", heading_style))
    location_info = [
        ['Location', location_data['display']],
        ['State', location_data['state']],
        ['Coordinates', f"{location_data['lat']}°N, {abs(location_data['lon'])}°W"],
        ['Altitude', f"{location_data['alt']} meters"]
    ]
    location_table = Table(location_info, colWidths=[2*inch, 4*inch])
    location_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F5F5F5')),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(location_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Environmental Conditions
    elements.append(Paragraph("Environmental Conditions", heading_style))
    env_data = [
        ['Parameter', 'Value'],
        ['Humidity', f"{inputs['humidity']:.1f}%"],
        ['Temperature', f"{inputs['ambient_temp']:.1f}°C"],
        ['Wind Speed', f"{inputs['wind_speed']} m/s"],
        ['Visibility', f"{inputs['visibility']:.1f} km"],
        ['Pressure', f"{inputs['pressure']} hPa"],
        ['Cloud Ceiling', f"{inputs['cloud_ceiling']} ft"],
        ['Month', MONTHS[inputs['month']-1]],
        ['Hour', f"{inputs['hour']}:00"]
    ]
    env_table = Table(env_data, colWidths=[3*inch, 3*inch])
    env_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(COLORS['primary'])),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9F9F9')])
    ]))
    elements.append(env_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Performance Analysis
    elements.append(Paragraph("Performance Analysis", heading_style))
    stats = LOCATION_STATS.get(location, {'mean': 0, 'min': 0, 'max': 0})
    perf_metrics = MODEL_PERFORMANCE.get(location, {'r2': 0, 'mae': 0, 'rmse': 0})
    
    perf_data = [
        ['Metric', 'Value'],
        ['Performance Tier', tier_name],
        ['vs Location Average', f"{percentage:.0f}%"],
        ['Location Average', f"{stats['mean']:.2f} kW"],
        ['Location Range', f"{stats['min']:.2f} - {stats['max']:.2f} kW"],
    ]
    perf_table = Table(perf_data, colWidths=[3*inch, 3*inch])
    perf_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(COLORS['secondary'])),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9F9F9')])
    ]))
    elements.append(perf_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Model Information
    elements.append(Paragraph("Model Information", heading_style))
    model_data = [
        ['Model Type', model_name],
        ['R² Score', f"{perf_metrics['r2']:.4f}"],
        ['MAE', f"{perf_metrics['mae']:.2f} kW"],
        ['RMSE', f"{perf_metrics['rmse']:.2f} kW"]
    ]
    model_table = Table(model_data, colWidths=[3*inch, 3*inch])
    model_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F5F5F5')),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(model_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Disclaimer
    disclaimer_text = """
    <b>Disclaimer:</b> This prediction is an estimate based on statistical machine learning models. 
    Actual output may vary due to panel condition, orientation, shading, and weather events. 
    Consult professionals for critical applications.
    """
    elements.append(Paragraph(disclaimer_text, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    # Footer
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    footer_text = f"""
    <para align=center>
    <i>Generated {timestamp}</i><br/>
    Northern Hemisphere Photovoltaic Analysis
    </para>
    """
    elements.append(Paragraph(footer_text, styles['Normal']))
    
    doc.build(elements)
    
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    return pdf_bytes