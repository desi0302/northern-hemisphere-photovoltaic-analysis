"""
Model Performance Loader - Reads from saved training results
Uses the actual results from your ML training notebook
"""

import os
import pandas as pd
import joblib


def load_model_performance_from_csv(results_file='model_outputs/model_results_corrected.csv'):
    """
    Load model performance metrics from saved training results CSV
    
    Parameters:
    -----------
    results_file : str
        Path to the CSV file containing training results
        
    Returns:
    --------
    tuple : (performance_metrics dict, best_models dict)
    """
    
    if not os.path.exists(results_file):
        print(f"Warning: Results file not found at {results_file}")
        return None, None
    
    try:
        # Read the CSV file
        df = pd.read_csv(results_file)
        
        # Location name mapping (handle potential naming differences)
        location_mapping = {
            'camp_murray': 'camp_murray',
            'grissom': 'grissom',
            'hill_weber': 'hill_weber',
            'jdmt': 'jdmt',
            'kahului': 'kahului',
            'malmstrom': 'malmstrom',
            'march_afb': 'march_afb',
            'mnang': 'mnang',
            'offutt': 'offutt',
            'peterson': 'peterson',
            'travis': 'travis',
            'usafa': 'usafa'
        }
        
        performance_metrics = {}
        best_models = {}
        
        # Process each row in the CSV
        for _, row in df.iterrows():
            location = str(row['location']).lower().strip()
            
            # Map location name
            if location in location_mapping:
                loc_key = location_mapping[location]
                
                # Extract metrics (using correct column names from CSV)
                performance_metrics[loc_key] = {
                    'r2': round(float(row['r2_test']), 4),
                    'mae': round(float(row['mae_test']), 2),
                    'rmse': round(float(row['rmse_test']), 2)
                }
                
                # Extract model name
                model_name = str(row['best_model']).strip()
                best_models[loc_key] = model_name
                
                print(f"✓ {loc_key}: {model_name} - R²={performance_metrics[loc_key]['r2']:.4f}")
        
        print(f"\n✓ Loaded metrics for {len(performance_metrics)} locations from CSV")
        return performance_metrics, best_models
        
    except Exception as e:
        print(f"Error reading results file: {str(e)}")
        import traceback
        traceback.print_exc()
        return None, None


def get_model_performance(models_dir='models', data_dir='data/clean', 
                         results_file='model_outputs/model_results_corrected.csv',
                         use_cached=True):
    """
    Get model performance metrics from saved CSV results
    
    Parameters:
    -----------
    models_dir : str
        Directory containing model files (for cache location)
    data_dir : str
        Not used, kept for compatibility
    results_file : str
        Path to CSV file with training results
    use_cached : bool
        If True, try to load from cached file first
        
    Returns:
    --------
    tuple : (performance_metrics, best_models)
    """
    
    cache_file = os.path.join(models_dir, 'performance_cache.pkl')
    
    # Try to load from cache
    if use_cached and os.path.exists(cache_file):
        try:
            cached_data = joblib.load(cache_file)
            print("✓ Loaded performance metrics from cache")
            return cached_data['performance'], cached_data['models']
        except:
            print("Warning: Cache file corrupted, reloading from CSV...")
    
    # Load from CSV
    print(f"Loading model performance from: {results_file}")
    performance, models = load_model_performance_from_csv(results_file)
    
    if performance is None or models is None:
        print("Failed to load from CSV, using config defaults...")
        # Fallback to config
        try:
            from utils.config import MODEL_PERFORMANCE, BEST_MODELS
            return MODEL_PERFORMANCE, BEST_MODELS
        except:
            return {}, {}
    
    # Cache the results
    try:
        joblib.dump({'performance': performance, 'models': models}, cache_file)
        print(f"✓ Cached performance metrics to {cache_file}")
    except Exception as e:
        print(f"Warning: Could not cache results: {str(e)}")
    
    return performance, models


if __name__ == "__main__":
    """
    Run this script to load performance metrics from CSV
    Usage: python model_performance_loader.py
    """
    
    print("=" * 60)
    print("MODEL PERFORMANCE LOADER (FROM CSV)")
    print("=" * 60)
    print()
    
    # Load metrics from CSV
    perf, models = get_model_performance(use_cached=False)
    
    if perf:
        print()
        print("=" * 60)
        print("RESULTS SUMMARY")
        print("=" * 60)
        print()
        
        # Display results
        results_df = pd.DataFrame([
            {
                'Location': loc.replace('_', ' ').title(),
                'Model': models.get(loc, 'Unknown'),
                'R²': f"{metrics['r2']:.4f}",
                'MAE': f"{metrics['mae']:.2f}",
                'RMSE': f"{metrics['rmse']:.2f}"
            }
            for loc, metrics in sorted(perf.items(), key=lambda x: x[1]['r2'], reverse=True)
        ])
        
        print(results_df.to_string(index=False))
        print()
        
        import numpy as np
        print(f"Average R²: {np.mean([m['r2'] for m in perf.values()]):.4f}")
        print()
        print("✓ Performance metrics loaded from training results")
