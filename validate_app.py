"""
Validation Script: Test if Streamlit App Predictions Match ML Notebook Predictions

This script will:
1. Load the same test data used in ML training
2. Make predictions using the saved models (same as the app)
3. Compare with actual values
4. Show model performance metrics
"""

import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def engineer_features(df_loc):
    """
    Create engineered features (same as app and ML notebook)
    """
    df_loc = df_loc.copy()
    
    # Interaction features
    df_loc['temp_humidity'] = df_loc['ambient_temp'] * df_loc['humidity']
    df_loc['temp_cloud'] = df_loc['ambient_temp'] * df_loc['cloud_ceiling']
    df_loc['humidity_cloud'] = df_loc['humidity'] * df_loc['cloud_ceiling']
    
    # Cyclic time features
    df_loc['month_sin'] = np.sin(2 * np.pi * df_loc['month'] / 12)
    df_loc['month_cos'] = np.cos(2 * np.pi * df_loc['month'] / 12)
    df_loc['hour_sin'] = np.sin(2 * np.pi * df_loc['hour'] / 24)
    df_loc['hour_cos'] = np.cos(2 * np.pi * df_loc['hour'] / 24)
    
    return df_loc

def validate_single_location(df, location, models_dir='models'):
    """
    Validate predictions for a single location
    """
    print(f"\n{'='*70}")
    print(f"VALIDATING: {location.upper()}")
    print(f"{'='*70}")
    
    # Get location data
    df_loc = df[df['location'] == location].copy()
    print(f"Total samples: {len(df_loc)}")
    
    # Feature engineering
    df_loc = engineer_features(df_loc)
    
    # Define features
    exclude_cols = ['poly_pwr', 'location', 'datetime', 'season', 'date', 'time']
    feature_cols = [col for col in df_loc.columns if col not in exclude_cols]
    
    X = df_loc[feature_cols].copy()
    y = df_loc['poly_pwr'].copy()
    
    # Same train/test split as in training (random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )
    
    print(f"Test samples: {len(X_test)}")
    
    # Load saved model
    model_path = os.path.join(models_dir, f'{location}_model.pkl')
    scaler_path = os.path.join(models_dir, f'{location}_scaler.pkl')
    features_path = os.path.join(models_dir, f'{location}_features.pkl')
    
    if not os.path.exists(model_path):
        print(f"❌ Model not found: {model_path}")
        return None
    
    # Load model and scaler
    model = joblib.load(model_path)
    print(f"✓ Loaded model: {type(model).__name__}")
    
    scaler = None
    if os.path.exists(scaler_path):
        scaler = joblib.load(scaler_path)
        print(f"✓ Loaded scaler: StandardScaler")
    
    # Load feature names
    feature_names = joblib.load(features_path)
    X_test = X_test[feature_names]
    
    # Make predictions (same logic as app)
    if scaler is not None:
        X_test_scaled = scaler.transform(X_test)
        y_pred = model.predict(X_test_scaled)
    else:
        y_pred = model.predict(X_test)
    
    # Calculate metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"\n📊 MODEL PERFORMANCE:")
    print(f"   R² Score:  {r2:.4f}")
    print(f"   MAE:       {mae:.4f} kW")
    print(f"   RMSE:      {rmse:.4f} kW")
    
    # Show some example predictions
    print(f"\n🔍 SAMPLE PREDICTIONS (first 5 test samples):")
    print(f"{'Actual':<12} {'Predicted':<12} {'Error':<12}")
    print("-" * 40)
    for i in range(min(5, len(y_test))):
        actual = y_test.iloc[i]
        predicted = y_pred[i]
        error = abs(actual - predicted)
        print(f"{actual:<12.2f} {predicted:<12.2f} {error:<12.2f}")
    
    # Return one sample for manual testing in app
    print(f"\n🧪 SAMPLE INPUT FOR MANUAL APP TESTING:")
    sample_idx = 0
    sample = X_test.iloc[sample_idx]
    
    # Get original features (before engineering)
    print(f"   Location: {location}")
    print(f"   Humidity: {sample['humidity']:.1f}%")
    print(f"   Ambient Temp: {sample['ambient_temp']:.1f}°C")
    print(f"   Wind Speed: {sample['wind_speed']:.0f} m/s")
    print(f"   Visibility: {sample['visibility']:.1f} km")
    print(f"   Pressure: {sample['pressure']:.0f} hPa")
    print(f"   Cloud Ceiling: {sample['cloud_ceiling']:.0f} feet")
    print(f"   Month: {sample['month']:.0f}")
    print(f"   Hour: {sample['hour']:.0f}")
    print(f"\n   Expected Output: {y_test.iloc[sample_idx]:.2f} kW")
    print(f"   Model Prediction: {y_pred[sample_idx]:.2f} kW")
    print(f"   Error: {abs(y_test.iloc[sample_idx] - y_pred[sample_idx]):.2f} kW")
    
    return {
        'location': location,
        'r2': r2,
        'mae': mae,
        'rmse': rmse,
        'n_test': len(y_test)
    }

def validate_all_locations(df, models_dir='models'):
    """
    Validate all locations and create summary report
    """
    print("\n" + "="*70)
    print("VALIDATION REPORT: SAVED MODELS vs ACTUAL TEST DATA")
    print("="*70)
    
    results = []
    
    for location in sorted(df['location'].unique()):
        result = validate_single_location(df, location, models_dir)
        if result is not None:
            results.append(result)
    
    # Summary table
    print("\n" + "="*70)
    print("SUMMARY: ALL LOCATIONS")
    print("="*70)
    
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('r2', ascending=False)
    
    print(f"\n{'Location':<15} {'R²':<8} {'MAE':<10} {'RMSE':<10} {'Samples':<10}")
    print("-" * 70)
    for _, row in results_df.iterrows():
        print(f"{row['location']:<15} {row['r2']:<8.4f} {row['mae']:<10.2f} {row['rmse']:<10.2f} {row['n_test']:<10.0f}")
    
    print("\n" + "="*70)
    print(f"Average R² Score: {results_df['r2'].mean():.4f}")
    print(f"Average MAE:      {results_df['mae'].mean():.2f} kW")
    print(f"Average RMSE:     {results_df['rmse'].mean():.2f} kW")
    print("="*70)
    
    print("\n✅ VALIDATION COMPLETE!")
    print("\nIf these metrics match your ML notebook results, the app is working correctly!")
    
    return results_df

if __name__ == "__main__":
    print("\n🔬 STREAMLIT APP VALIDATION SCRIPT")
    print("="*70)
    
    # Try different possible paths for the data file
    possible_paths = [
        'data/clean/photovoltaic_cleaned.csv',
        '../data/clean/photovoltaic_cleaned.csv',
        './data/clean/photovoltaic_cleaned.csv'
    ]
    
    data_path = None
    for path in possible_paths:
        if os.path.exists(path):
            data_path = path
            break
    
    if data_path is None:
        print(f"❌ Data file not found. Tried these paths:")
        for path in possible_paths:
            print(f"   - {path}")
        print("\nCurrent directory:", os.getcwd())
        print("Please run from project root or update the path.")
        exit(1)
    
    print(f"Loading data from: {data_path}")
    df = pd.read_csv(data_path)
    print(f"✓ Loaded {len(df)} samples from {df['location'].nunique()} locations")
    
    # Try different possible paths for models directory
    possible_model_dirs = ['models', '../models', './models']
    
    models_dir = None
    for path in possible_model_dirs:
        if os.path.exists(path):
            models_dir = path
            break
    
    if models_dir is None:
        print(f"\n❌ Models directory not found. Tried these paths:")
        for path in possible_model_dirs:
            print(f"   - {path}")
        print("\nPlease run the save_trained_models() function from your ML notebook first.")
        exit(1)
    
    print(f"✓ Found models directory: {models_dir}")
    
    # Validate all locations
    results_df = validate_all_locations(df, models_dir)
    
    print("\n" + "="*70)
    print("HOW TO USE THIS VALIDATION:")
    print("="*70)
    print("1. Compare the R² scores above with your ML notebook results")
    print("2. Use the 'SAMPLE INPUT FOR MANUAL APP TESTING' values")
    print("3. Enter those exact values in your Streamlit app")
    print("4. The app prediction should match the 'Model Prediction' shown above")
    print("5. If they match → Your app is working correctly! ✅")
    print("="*70)