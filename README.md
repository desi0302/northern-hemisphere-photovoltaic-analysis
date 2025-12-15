>                                     🚧 **IN PROGRESS...** 🚧


<table>
  <tr>
    <td>
      <img src="images/solar.png" alt="Logo" width="500" height="100">
    </td>
    <td>
      <h1>Northern Hemisphere Photovoltaic Analysis</h1>

[Northern Hemisphere Photovoltaic Analysis](https://solarpower.streamlit.app/)
is a comprehensive machine learning project that predicts solar power generation across 12 military installations in the Northern Hemisphere. By analyzing weather conditions, geographic features, and time-based patterns, this project helps energy managers forecast photovoltaic output and optimize renewable energy operations.

The project follows the complete data science pipeline—from **data cleaning and exploratory analysis** to **building location-specific predictive models** and deploying an **interactive web application**. With over 20,000 observations spanning 14 months (2017-2018), the analysis reveals how environmental factors like temperature, humidity, and cloud cover impact solar efficiency across diverse climate regions.

  </tr>
</table>

## Dataset

This dataset accompanies the research paper *"Machine Learning Modeling of Horizontal Photovoltaics Using Weather and Location Data"* published in the *Journal of Renewable Energy*. It contains **20,000+ power output measurements** from horizontal photovoltaic panels across **12 military installations** in the Northern Hemisphere, collected over **14 months** (2017-2018).

### What's in the Data?

Each observation captures solar panel performance at a specific moment in time, along with environmental conditions and location details. The dataset includes 17 variables covering weather, geography, and temporal information:

<div align="center">

<table>
  <thead>
    <tr>
      <th>Column Name</th>
      <th>Data Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Location</td>
      <td>object</td>
      <td>Military installation identifier (12 unique sites)</td>
    </tr>
    <tr>
      <td>Date</td>
      <td>int64</td>
      <td>Observation date in YYYYMMDD format</td>
    </tr>
    <tr>
      <td>Time</td>
      <td>int64</td>
      <td>Observation time in 24-hour HHMM format</td>
    </tr>
    <tr>
      <td>Latitude</td>
      <td>float64</td>
      <td>Geographic coordinate (degrees north)</td>
    </tr>
    <tr>
      <td>Longitude</td>
      <td>float64</td>
      <td>Geographic coordinate (degrees east/west)</td>
    </tr>
    <tr>
      <td>Altitude</td>
      <td>int64</td>
      <td>Elevation above sea level (meters)</td>
    </tr>
    <tr>
      <td>YRMODAHRMI</td>
      <td>float64</td>
      <td>Combined timestamp (Year-Month-Day-Hour-Minute)</td>
    </tr>
    <tr>
      <td>Month</td>
      <td>int64</td>
      <td>Month of year (1–12)</td>
    </tr>
    <tr>
      <td>Hour</td>
      <td>int64</td>
      <td>Hour of day (0–23)</td>
    </tr>
    <tr>
      <td>Season</td>
      <td>object</td>
      <td>Season derived from date (Winter, Spring, Summer, Autumn)</td>
    </tr>
    <tr>
      <td>Humidity</td>
      <td>float64</td>
      <td>Relative humidity (%)</td>
    </tr>
    <tr>
      <td>AmbientTemp</td>
      <td>float64</td>
      <td>Ambient air temperature (°C)</td>
    </tr>
    <tr>
      <td><strong>PolyPwr</strong></td>
      <td>float64</td>
      <td><strong>Target variable: Photovoltaic power output (Watts)</strong></td>
    </tr>
    <tr>
      <td>Wind.Speed</td>
      <td>int64</td>
      <td>Wind speed (m/s)</td>
    </tr>
    <tr>
      <td>Visibility</td>
      <td>float64</td>
      <td>Horizontal visibility distance (km)</td>
    </tr>
    <tr>
      <td>Pressure</td>
      <td>float64</td>
      <td>Atmospheric pressure (hPa)</td>
    </tr>
    <tr>
      <td>Cloud.Ceiling</td>
      <td>int64</td>
      <td>Height of lowest cloud layer (feet)</td>
    </tr>
  </tbody>
</table>

</div>

This rich dataset enables analysis of how **weather patterns, time of day, seasonal changes, and geographic location** influence solar panel performance—essential for building accurate predictive models.


## Business Requirements

This project addresses real-world challenges in solar energy management across multiple military installations. The goal is to build predictive models and analytical tools that help energy managers make informed decisions about grid operations, maintenance scheduling, and renewable energy optimization.

### Project Objectives

| # | Requirement | What Success Looks Like |
|---|-------------|------------------------|
| 1 | **Forecast Solar Power Output** | Accurate predictions of photovoltaic output using weather, time, and location data. Models help energy managers plan grid operations and optimize energy storage. |
| 2 | **Identify Key Drivers of Performance** | Clear understanding of which environmental factors (temperature, humidity, cloud cover, wind) most impact solar efficiency at different locations. |
| 3 | **Compare Site Performance** | Identify high-performing and underperforming installations. Highlight periods of expected low output to support maintenance planning without disrupting operations. |
| 4 | **Visualize Trends and Patterns** | Present key findings from exploratory analysis through clear visualizations showing solar power trends by time of day, season, and location. Help stakeholders understand performance differences across installations. |
| 5 | **Deploy an Accessible Tool** | Web-based application where users can explore EDA findings, input weather conditions to generate predictions, and review model performance metrics—no coding required. |

### Modeling Strategy

Initially, the project explored building a single global model using location as a feature. However, exploratory analysis revealed that **location alone explains 11.2% of variance** in solar output, with a **2:1 performance ratio** between the best and worst sites. This finding led to the decision to build **12 location-specific models**, each trained on site-specific data to capture unique climate patterns and maximize prediction accuracy.



## Hypotheses and Validation

Before diving into modeling, I developed testable hypotheses about what factors might influence solar power generation. Each hypothesis was validated through statistical analysis and visualization during the exploratory data analysis phase.

| # | Hypothesis | How I Tested It | Result |
|---|------------|-----------------|--------|
| 1 | **Higher humidity reduces solar power output** | Calculated Pearson correlation between `Humidity` and `PolyPwr`; visualized relationship with scatter plots and regression analysis. | ✓ **Supported** - Moderate negative correlation (r = -0.40) |
| 2 | **Clear skies increase photovoltaic output** | Analyzed correlation between `Cloud.Ceiling` and `PolyPwr`; tested relationship strength with scatter plots and correlation analysis. | ✓ **Supported** - Moderate positive correlation (r = +0.42) |
| 3 | **Solar output peaks in summer and at midday** | Used two-way ANOVA to test effects of `Month` and `Hour` on `PolyPwr`, including interaction effects. Visualized with boxplots and heatmaps. | ✓ **Strongly Supported** - Significant month effect (F = 347), hour effect (F = 168), and interaction (p < 0.001) |
| 4 | **Altitude affects solar panel efficiency** | Compared `PolyPwr` across altitude bins using Kruskal-Wallis test; calculated effect size (ε²) to assess practical significance. | ✗ **Rejected** - Statistically significant but negligible effect size (ε² = 0.005) indicates spurious relationship |
| 5 | **Location is a major factor in performance** | Performed one-way ANOVA comparing `PolyPwr` across 12 locations; calculated eta-squared (η²) for effect size; compared site averages. | ✓ **Strongly Supported** - Large effect (η² = 0.112, F = 240); 2:1 performance ratio between sites |

**Key Insights:** 

- **Hypothesis #4 demonstrates an important lesson:** Statistical significance ≠ practical significance. With 20,000+ observations, the Kruskal-Wallis test detected a "significant" altitude effect (p < 0.001), but the effect size was negligible (ε² = 0.005, explaining only 0.5% of variance). The 1.25W difference is dwarfed by seasonal (~10W) and weather variations (0-35W), likely reflecting confounding site factors rather than true altitude effects.

- **Hypothesis #5 proved critical:** Location explains 11.2% of variance in solar output—a substantial effect with major implications. The 2:1 performance ratio between best and worst sites, combined with distinct climate patterns at each installation, drove the strategic decision to build **12 location-specific models** rather than a single global model.

- **Environmental factors matter:** Both humidity (r = -0.40) and cloud ceiling (r = +0.42) show moderate correlations with output, confirming that weather conditions significantly impact solar panel performance.


## Project Plan

This project follows a structured data science methodology from raw data to deployed application. The workflow is divided into three main phases, each documented in its own Jupyter notebook for reproducibility and clarity.

### 1. Extract, Transform, Load (ETL)
**Notebook:** `ETL.ipynb`

**Objective:** Clean and prepare raw data for analysis

**Key Steps:**
- **Data Loading:** Imported 20,993 observations from 12 Northern Hemisphere sites spanning May 2017 to October 2018
- **Data Quality Assessment:** 
  - Examined data types, missing values, and statistical summaries
  - Identified and investigated anomalies (52 rows with 0% humidity, 4 rows with zero cloud ceiling)
  - Verified consistent geographic coordinates for each location
- **Data Cleaning:**
  - Standardized column names and categorical values to lowercase with underscores
  - Removed 52 rows (0.25%) with invalid 0% humidity readings
  - Dropped redundant `yrmodahrmi` column (captured only year-month, no additional information)
  - Created proper datetime column by combining separate date and time fields
- **Outlier Analysis:** 
  - Applied IQR method to detect statistical outliers in environmental variables
  - Retained all outliers as they represent valid real-world measurements (extreme weather conditions)
- **Optimization:** Converted categorical columns (location, season) to category dtype for memory efficiency
- **Output:** Saved cleaned dataset (`photovoltaic_clean.csv`) ready for exploratory analysis

**Data Management:** Organized files in structured directories (`../data/raw/` and `../data/clean/`) with clear naming conventions. All file paths defined as variables at notebook start for easy updates.

### 2. Exploratory Data Analysis (EDA)
**Notebook:** `EDA.ipynb`

**Objective:** Discover patterns, test hypotheses, and guide modeling decisions

**Key Steps:**
- **Univariate Analysis:**
  - Examined distributions of all numerical features (power output, temperature, humidity, wind, etc.)
  - Analyzed categorical distributions to assess data balance across locations and seasons
- **Bivariate Analysis:**
  - Tested correlations between environmental factors and solar power output
  - Created scatter plots and regression lines to visualize relationships
  - Discovered moderate correlations: humidity (r = -0.40), cloud ceiling (r = +0.42)
- **Temporal Analysis:**
  - Visualized power output time series for each location over 14 months
  - Analyzed hourly, monthly, and seasonal patterns using boxplots and line charts
  - Created interactive 3D visualizations showing environmental variable interactions
- **Hypothesis Testing:**
  - Formally tested 5 hypotheses using appropriate statistical methods:
    - **H1 (Humidity):** Pearson correlation confirmed moderate negative effect (r = -0.40)
    - **H2 (Cloud Ceiling):** Pearson correlation confirmed moderate positive effect (r = +0.42)
    - **H3 (Temporal Patterns):** Two-way ANOVA revealed strong month effect (F = 347) and hour effect (F = 168) with significant interaction
    - **H4 (Altitude):** Kruskal-Wallis showed statistical significance (p < 0.001) but negligible effect size (ε² = 0.005)—**hypothesis rejected** as practically meaningless
    - **H5 (Location):** One-way ANOVA demonstrated strong effect (η² = 0.112, F = 240) with 2:1 performance ratio between sites
- **Critical Finding:** Location explains 11.2% of variance—this discovery drove the strategic decision to build location-specific models

**Why These Methods?**
- **Pearson correlation** for linear relationships between continuous variables
- **ANOVA** to compare means across groups and test interaction effects  
- **Kruskal-Wallis** as non-parametric alternative when normality assumptions violated
- **Effect size calculations (η², ε²)** to distinguish statistical significance from practical significance—essential with large sample sizes where p-values alone can be misleading

### 3. Machine Learning Modeling
**Notebook:** `ML.ipynb`

**Objective:** Build accurate, location-specific predictive models

**Key Steps:**
- **Feature Engineering:**
  - Started with 11 base environmental measurements
  - Created 24 additional features incorporating solar physics:
    - **Solar geometry:** elevation angle, azimuth, day length
    - **Temperature effects:** panel efficiency factors, temperature-humidity interactions
    - **Atmospheric conditions:** attenuation proxies, pressure-visibility interactions
  - Final feature set: **35 total features** capturing non-linear relationships
- **Algorithm Selection:**
  - Tested 7 algorithms per location: Ridge, Lasso, ElasticNet, Gradient Boosting, XGBoost, Random Forest, Extra Trees
  - Used proper train/test split (80/20) to prevent overfitting
  - Applied cross-validation and regularization appropriate to each algorithm
- **Model Training:**
  - Trained separate models for each of 12 locations (84 total models evaluated across 7 algorithms)
  - Selected best-performing algorithm per location based on R² score
  - Most common winners: Gradient Boosting (6 sites), Random Forest (3 sites), Extra Trees (3 sites)
- **Performance Evaluation:**
  - Average R² = 0.65 across all locations
  - Top performers: Travis (0.79), Camp Murray (0.73), Hill Weber (0.73), MNANG (0.72)
  - Average prediction error: 2.92 kW (RMSE)
  - 9 of 12 locations meet deployment threshold (R² > 0.60)
- **Model Interpretation:**
  - Analyzed feature importance across locations
  - Most influential features: month cosine, day length, solar elevation (confirming solar physics matter)
  - Examined residuals to detect systematic biases
- **Results Management:**
  - Saved trained models using joblib for deployment
  - Exported performance metrics to `model_performance.csv` for application use
  - Created visualizations: predictions vs actuals, residuals, feature importance, performance rankings

**Why Location-Specific Models?**

The EDA revealed that location alone explains 11.2% of variance with a 2:1 performance ratio between sites. This indicated distinct climate regimes with non-transferable patterns. Building 12 separate models allows each to specialize in its location's unique weather patterns, resulting in better predictions than a single global model attempting to generalize across all sites.

**Why These Algorithms?**

The project tested both linear (Ridge, Lasso, ElasticNet) and tree-based (Gradient Boosting, XGBoost, Random Forest, Extra Trees) algorithms:
- **Linear models:** Good baseline, interpretable, work well with properly scaled features
- **Tree-based models:** Capture non-linear relationships and interactions without manual feature scaling
- **Ensemble methods (boosting/bagging):** Reduce overfitting and improve generalization

Final model selection was data-driven—the best algorithm for each location was chosen based on actual test performance, not assumptions.

### 4. Application Deployment
**Tool:** Streamlit

**Objective:** Make predictions accessible to non-technical stakeholders

**Features:**
- **Dashboard:** Project overview, dataset description, key EDA findings with visualizations
- **Predict:** Interactive tool where users input weather conditions and receive solar power predictions
- **Performance:** Model accuracy metrics (R², RMSE, MAE) dynamically loaded from training results

**Why Streamlit?**
- Python-native framework allowing direct integration with trained models
- Quick development cycle for data science applications
- Professional appearance without frontend coding
- **Free deployment** via Streamlit Community Cloud

### Data Management Throughout

**File Organization:**
```
NORTHERN-HEMISPHERE-PHOTOVOLTAIC-ANALYSIS/
├── venv/                            # Virtual environment
├── assets/                          # Project assets
├── data/
│   ├── raw/                         # Original photovoltaic.csv
│   └── clean/                       # Processed photovoltaic_clean.csv
├── images/                          # Project images and logo
│   ├── 1.png, 2.png, 3.png, 4.png   # EDA visualizations
│   ├── solar.png                    # Project logo
│   └── solar2.jpg
├── jupyter_notebooks/              # Analysis notebooks
│   ├── plots/                      # Generated visualizations
│   ├── EDA.ipynb                   # Exploratory Data Analysis
│   ├── ETL.ipynb                   # Data cleaning pipeline
│   └── ML.ipynb                    # Machine learning modeling
├── model_outputs/                  # Training results and visualizations
│   ├── feature_importance.png
│   ├── model_results_corrected.csv
│   ├── performance_dashboard.png
│   ├── predictions_vs_actuals.png
│   └── residual_analysis.png
├── models/                         # Saved trained models (.pkl files)
├── pages/                          # Streamlit multi-page app
│   ├── 1_Performance.py            # Model metrics page
│   └── 2_Predict.py                # Prediction interface
├── utils/                          # Helper functions and utilities
│   ├── __pycache__/
│   ├── __init__.py
│   ├── config.py                    # Configuration settings
│   ├── feature_engineering.py       # Feature creation functions
│   ├── gauge.py                     # Gauge chart visualization
│   ├── model_performance_loader.py  # Load training results
│   ├── model_utils.py               # Model loading utilities
│   └── pdf_generator.py             # PDF report generation
├── _Dashboard.py                    # Main Streamlit dashboard (landing page)
├── app.py                           # Streamlit app entry point
├── config.py                        # App configuration
├── .gitignore                       # Git ignore rules
├── .slugignore                      # Streamlit deployment ignore
├── python-version                   # Python version specification
├── Procfile                         # Deployment configuration
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
└── setup.sh                         # Setup script
```

**Reproducibility Practices:**
- All file paths defined as variables at notebook start
- Sequential cell execution required (documented in each notebook)
- Clear markdown documentation before each code section
- Saved intermediate results (cleaned data, trained models, performance metrics)
- Version control friendly structure with proper `.gitignore`

**Quality Assurance:**
- Data validation checks before each phase
- Statistical rigor (hypothesis testing with proper effect size reporting)
- Model evaluation on holdout test sets
- Residual analysis to detect systematic errors
- Dynamic performance loading in app (reflects actual training results via `model_performance_loader.py`)

## Motivation

The global energy transition requires diverse low-carbon power sources working together to meet growing electricity demands while reducing emissions. Clean energy technologies—from renewable solar and wind to reliable nuclear baseload—are transforming how we generate and manage electricity. Each plays a vital role in building a sustainable energy future.

As organizations increasingly invest in clean energy infrastructure, accurate forecasting becomes essential for effective energy management. For solar installations across military bases, industrial facilities, and utility-scale farms, predicting output enables better grid integration, operational planning, and coordination with other power sources. Data-driven forecasting helps energy managers optimize storage systems, schedule maintenance during low-production periods, and ensure reliable electricity supply.

However, solar output is highly variable and complex. Weather conditions, time of day, seasons, and geographic location all interact to influence panel performance. Simple rules-of-thumb aren't enough—we need intelligent solutions that account for local climate patterns and environmental factors specific to each installation.

This project demonstrates how machine learning can transform raw environmental data into reliable solar predictions that support clean energy operations. By building location-specific models rather than one-size-fits-all solutions, the system recognizes that each installation has unique climate characteristics—a site in Alaska requires different modeling approaches than one in Nevada to deliver accurate forecasts.

Beyond its practical application in energy management, this project showcases the complete data science pipeline—from hypothesis-driven exploratory analysis to deploying an accessible web application. It reflects a commitment to using analytical skills to contribute meaningfully to the energy transition and the organizations working to deliver clean, reliable power.

## Machine Learning Approach

### Why Location-Specific Models?

The exploratory analysis revealed a critical insight: **location alone explains 11.2% of variance in solar output**, with a 2:1 performance ratio between the best and worst sites. This finding indicated that each installation operates under distinct climate regimes with non-transferable patterns. A single global model would struggle to capture these location-specific nuances, leading to the strategic decision to build **12 separate models**—one for each site.

This approach allows each model to specialize in its location's unique weather patterns, seasonal behaviors, and environmental characteristics, resulting in more accurate predictions than a one-size-fits-all solution.

### Feature Engineering Strategy

Starting with 11 base environmental measurements, I engineered 24 additional features to capture complex, non-linear relationships that simple models might miss. The expanded feature set incorporates **solar physics principles**:

**Solar Geometry Features:**
- Solar elevation angle (sun's position above horizon)
- Day length (hours of daylight)
- Seasonal indicators (month as cyclical features)

**Temperature Efficiency Factors:**
- Panel efficiency declines as temperature rises
- Temperature-humidity interaction effects
- Heat stress indicators

**Atmospheric Conditions:**
- Atmospheric attenuation proxies (combining pressure, visibility, humidity)
- Cloud cover impact factors
- Wind cooling effects

**Final Feature Count:** 35 engineered features from 11 base measurements

This physics-informed approach ensures models understand not just correlation patterns, but the underlying mechanisms of solar power generation.

### Algorithm Selection & Testing

Seven different algorithms were tested at each location to find the best performer. The selection spans linear models (with regularization) and tree-based ensemble methods:

<div align="center">

| Algorithm | Type | Why Test It? |
|-----------|------|--------------|
| **Ridge Regression** | Linear with L2 regularization | Prevents overfitting with many features; interpretable coefficients; handles multicollinearity well |
| **Lasso Regression** | Linear with L1 regularization | Automatic feature selection by zeroing weak predictors; creates sparse models |
| **ElasticNet** | Linear with L1 + L2 | Combines Ridge and Lasso benefits; balanced approach for feature-rich datasets |
| **Gradient Boosting** | Ensemble (sequential trees) | Builds trees iteratively to correct previous errors; excels at capturing complex patterns |
| **XGBoost** | Optimized gradient boosting | Faster implementation with regularization; industry standard for tabular data |
| **Random Forest** | Ensemble (parallel trees) | Reduces overfitting through bootstrap aggregation; robust to outliers |
| **Extra Trees** | Ensemble (randomized trees) | More random than Random Forest; faster training; good generalization |

</div>

**Training Process:**
- 80/20 train-test split for each location
- Cross-validation to tune hyperparameters
- Regularization strength adjusted to prevent overfitting
- Best algorithm selected based on test set R² score

**Model Selection Results:**
- **Ridge Regression:** 5 locations (42%) - most frequent winner, validating regularization strategy
- **Gradient Boosting:** 3 locations (25%) - captured complex non-linear patterns
- **Random Forest:** 2 locations (17%) - provided robust predictions
- **Extra Trees:** 2 locations (17%) - strong generalization

The fact that different algorithms won at different locations confirms that each site has unique predictive patterns—further validating the location-specific modeling approach.

---

## Model Performance

### Overall Results

The 12 location-specific models achieved an **average R² of 0.65** with an **average prediction error of 2.92 kW (RMSE)**. Nine out of twelve locations (75%) meet the deployment threshold of R² > 0.60, indicating reliable predictions suitable for operational use.

**What Does R² = 0.65 Mean?**

R² measures how much of the variance in solar output the model can explain. An R² of 0.65 means the model accounts for 65% of the variability in power generation. For environmental prediction tasks—where weather, cloud patterns, and atmospheric conditions are inherently noisy—this represents **solid performance**. Perfect predictions (R² = 1.0) are virtually impossible without real-time irradiance sensors directly measuring sunlight hitting the panels.

### Performance by Location

<div align="center">

| Location | R² Score | RMSE (kW) | MAE (kW) | Best Algorithm | Performance Tier |
|----------|----------|-----------|----------|----------------|------------------|
| **Travis AFB** | 0.79 | 2.31 | 1.68 | Gradient Boosting | ⭐ Strong |
| **Camp Murray** | 0.73 | 2.54 | 1.89 | Ridge | ⭐ Strong |
| **Hill Weber** | 0.73 | 2.48 | 1.82 | Extra Trees | ⭐ Strong |
| **MNANG** | 0.72 | 2.61 | 1.94 | Ridge | ⭐ Strong |
| **March AFB** | 0.69 | 2.77 | 2.06 | Gradient Boosting | ✅ Good |
| **Peterson AFB** | 0.67 | 2.89 | 2.15 | Random Forest | ✅ Good |
| **Grissom AFB** | 0.66 | 2.94 | 2.19 | Ridge | ✅ Good |
| **Selfridge** | 0.64 | 3.01 | 2.24 | Ridge | ✅ Good |
| **Offutt AFB** | 0.62 | 3.12 | 2.32 | Extra Trees | ✅ Good |
| **JDMT** | 0.58 | 3.28 | 2.44 | Ridge | ⚠️ Moderate |
| **USAFA** | 0.56 | 3.35 | 2.49 | Random Forest | ⚠️ Moderate |
| **Kahului** | 0.44 | 3.79 | 2.82 | Gradient Boosting | ⚠️ Challenging |

</div>

### Key Observations

**Top Performers (R² > 0.70):**
- **Travis AFB** leads with R² = 0.79 and lowest prediction error (2.31 kW RMSE)
- Top four locations cluster in the 0.70-0.79 range, demonstrating strong predictive capability
- These sites benefit from consistent weather patterns and robust datasets

**Solid Performers (0.60 ≤ R² < 0.70):**
- Five locations achieve good performance suitable for operational forecasting
- Prediction errors remain under 3.2 kW, acceptable for grid planning purposes

**Challenging Locations (R² < 0.60):**
- **Kahului** (Hawaii) proves most difficult at R² = 0.44 due to unique island climate, limited data, and weak seasonal patterns
- **USAFA and JDMT** fall slightly below deployment threshold but still provide useful directional guidance
- These models are functional but carry higher uncertainty—predictions should be interpreted cautiously

### Overfitting Control

Train-test performance gaps remain small (0.07-0.18 on average), confirming models generalize well and aren't memorizing training data. Some locations (Grissom, Offutt) even show test performance exceeding training scores, indicating robust generalization.

### Practical Implications

With an average error of ~3 kW on systems generating 0-35 kW, these models provide actionable forecasts for:
- **Grid planning:** Anticipating generation capacity hours ahead
- **Maintenance scheduling:** Identifying low-output periods for service work
- **Energy storage optimization:** Charging batteries when solar output peaks
- **Operational decisions:** Understanding site-specific performance patterns

Nine locations are production-ready for deployment, while the three weaker performers can still inform decision-making with appropriate caution about prediction uncertainty.

## Features

The **Northern Hemisphere Photovoltaic Analysis** web application provides an intuitive interface for exploring solar power data, generating predictions, and understanding model performance. Built with Streamlit, the app is designed for both technical and non-technical stakeholders.

### Dashboard (Main Page)

**What It Does:**
- Presents project overview and motivation
- Displays dataset statistics and geographic distribution of 12 military installations
- Showcases key findings from exploratory data analysis
- Includes visualizations showing:
  - Solar output patterns by time of day and season
  - Environmental factor correlations (humidity, cloud ceiling, temperature)
  - Location-based performance comparisons
  
**Who It's For:** Anyone wanting to understand the project scope, data, and analytical findings without diving into code.

### Predict Page

**What It Does:**
- Interactive prediction tool where users input current weather conditions
- Generates real-time solar power forecasts using trained machine learning models
- Features include:
  - **Location selector:** Choose from 12 military installations
  - **Weather inputs:** Sliders for temperature, humidity, wind speed, visibility, pressure, cloud ceiling (values constrained to realistic ranges)
  - **Time inputs:** Month and hour of day selectors
  - **Instant predictions:** Displays forecasted power output in kilowatts
  - **PDF export:** Download prediction reports for documentation

**Who It's For:** Energy managers, grid operators, and facility planners needing quick solar output forecasts for operational decisions.

**Example Use Case:** *"It's January 15th at 2 PM, temperature is 8°C, humidity 65%, clear skies. What power output should I expect at Travis AFB?"*

### Performance Page

**What It Does:**
- Comprehensive model evaluation metrics for all 12 locations
- Displays accuracy indicators:
  - **R² scores:** How well models explain variance
  - **RMSE (Root Mean Square Error):** Average prediction error in kW
  - **MAE (Mean Absolute Error):** Typical error magnitude
- Performance visualizations:
  - Predictions vs Actuals scatter plots
  - Residual analysis charts
  - Feature importance rankings
  - Performance tier rankings
- Includes helpful explanations of metrics for non-technical users

**Who It's For:** Technical stakeholders evaluating model reliability and data scientists interested in methodology.

### User Experience Features

- **Clean amber/orange theme:** Reflects solar energy domain
- **Help sections:** Plain-language explanations of ML concepts
- **Slider inputs:** Ensures users select valid values within realistic ranges
- **Dynamic data loading:** Performance metrics reflect actual training results (not hardcoded)

## Technical Stack

### **Programming Language**
- **Python 3.9+** - Core language for data science pipeline and web application

### **Data Processing & Analysis**
- **pandas** - Data manipulation and cleaning
- **NumPy** - Numerical operations and array processing
- **SciPy** - Statistical hypothesis testing (ANOVA, Kruskal-Wallis)

### **Machine Learning**
- **scikit-learn** - ML algorithms, model training, evaluation metrics
  - Ridge, Lasso, ElasticNet regression
  - Gradient Boosting, Random Forest, Extra Trees
- **XGBoost** - Optimized gradient boosting implementation
- **joblib** - Model serialization and loading

### **Data Visualization**
- **Matplotlib** - Static plotting and charts
- **Seaborn** - Statistical visualizations
- **Plotly** - Interactive 3D visualizations

### **Web Application**
- **Streamlit** - Web framework for data science applications
- **ReportLab** - PDF report generation

### **Development Tools**
- **Jupyter Notebook** - Interactive analysis and documentation
- **Git** - Version control
- **VS Code** - Code editor

### **Deployment**
- **Streamlit Community Cloud** - Free cloud hosting
- **GitHub** - Code repository 

---

## Installation & Setup

### Prerequisites

Before running the application locally, ensure you have:
- **Python 3.9 or higher** installed ([Download Python](https://www.python.org/downloads/))
- **Git** installed ([Download Git](https://git-scm.com/downloads))
- Basic familiarity with command line/terminal

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/northern-hemisphere-photovoltaic-analysis.git
cd northern-hemisphere-photovoltaic-analysis
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Key dependencies include:**
- streamlit
- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib
- seaborn
- plotly
- reportlab
- scipy

### Step 4: Train Models or Download Pre-trained Models

**Option A - Train models yourself (recommended for learning):**
1. Open and run `jupyter_notebooks/ML.ipynb` sequentially from top to bottom
2. Models will be automatically saved to the `models/` directory
3. Training takes approximately 1-2 minutes (depending on your hardware)

**Option B - Download pre-trained models (quick start):**
1. Download the pre-trained models: [ Download Models (Google Drive)](https://drive.google.com/file/d/1lLHpV9iYEQnUMeiJx-gR65XfCEA2UiKN/view?usp=drive_link)
2. Extract the downloaded file
3. Place all 12 `.pkl` files into the `models/` directory

**Verify models are ready:**
```bash
ls models/*.pkl
# Should show 12 model files (one per location)
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Troubleshooting

**Issue: ModuleNotFoundError**
- Solution: Ensure virtual environment is activated and all dependencies installed

**Issue: FileNotFoundError for models**
- Solution: Verify all 12 `.pkl` model files exist in the `models/` directory

**Issue: Port already in use**
- Solution: Run `streamlit run app.py --server.port 8502` to use a different port

**Issue: Data file not found**
- Solution: Check that `data/clean/photovoltaic_clean.csv` exists with correct path

### Development Mode

To run the app with auto-reload during development:
```bash
streamlit run app.py --server.runOnSave true
```


## Usage Guide

### Getting Started

1. **Launch the application** using the installation steps above, or visit the [deployed version](https://your-app-url.streamlit.app) *(coming soon)*

2. **Navigate the app** using the sidebar menu with three main pages:
   -  Dashboard
   -  Performance
   -  Predict

### Using the Dashboard Page

**Purpose:** Understand the project scope and key findings

1. Read the project overview and motivation
2. Review dataset statistics and location map
3. Explore EDA findings:
   - Scroll through visualizations showing temporal patterns
   - Examine correlation analyses
   - Review hypothesis testing results
4. Note the key insight: **location explains 11.2% of variance**

**No interaction required** - this page is informational only.

### Using the Predict Page

**Purpose:** Generate solar power forecasts for specific conditions

**Step-by-Step:**

1. **Select Location** from dropdown (12 military installations available)

2. **Input Weather Conditions:**
   - **Temperature (°C):** Current ambient temperature (-20 to 40°C)
   - **Humidity (%):** Relative humidity (20 to 100%)
   - **Wind Speed (m/s):** Current wind speed (0 to 20 m/s)
   - **Visibility (km):** Horizontal visibility distance (0 to 20 km)
   - **Pressure (hPa):** Atmospheric pressure (900 to 1050 hPa)
   - **Cloud Ceiling (feet):** Height of lowest cloud layer (0 to 30,000 feet)

3. **Set Time Parameters:**
   - **Month:** Select month (1-12)
   - **Hour:** Select hour of day (0-23, military time)

4. **Click "Generate Prediction"**

5. **Review Results:**
   - Predicted power output displayed in kilowatts (kW)
   - Model confidence indicator
   - Location-specific context

6. **Optional: Export PDF Report**
   - Click "Download PDF Report" button
   - Save detailed prediction with input parameters and model information

**Tips for Best Results:**
- Use realistic weather values for the selected location
- Predictions are only valid for hours 10-15 (peak solar production hours) - the models were trained exclusively on midday data when panels generate meaningful power
- For locations marked "challenging" (Kahului, USAFA, JDMT), interpret results cautiously

**Example Scenario:**
```
Location: Travis AFB
Date: June 15 (Month: 6)
Time: 13:00 (Hour: 13)
Temperature: 28°C
Humidity: 45%
Wind Speed: 3 m/s
Visibility: 15 km
Pressure: 1013 hPa
Cloud Ceiling: 25,000 feet (clear skies)

Expected Output: ~18-22 kW (peak summer performance)
```

### Using the Performance Page

**Purpose:** Evaluate model accuracy and understand limitations

1. **Review Overall Statistics:**
   - Average R² across all locations
   - Average prediction error (RMSE)
   - Deployment readiness summary

2. **Examine Location-Specific Metrics:**
   - Scroll through the performance table
   - Identify top performers (Travis, Camp Murray, Hill Weber, MNANG)
   - Note challenging locations (Kahului, USAFA, JDMT)

3. **Explore Visualizations:**
   - **Predictions vs Actuals:** See how well models match reality
   - **Residual Plots:** Check for systematic biases
   - **Feature Importance:** Understand what drives predictions
   - **Performance Rankings:** Compare locations at a glance

4. **Read Metric Explanations:**
   - Click lightbulb icons (💡) for plain-language definitions
   - Understand what R², RMSE, and MAE mean in practice

**Understanding the Tiers:**
-  **Strong (R² > 0.70):** Highly reliable for operational use
-  **Good (0.60 ≤ R² < 0.70):** Suitable for planning and forecasting
-  **Moderate/Challenging (R² < 0.60):** Use with caution; higher uncertainty

### Sharing Results

- **Screenshots**: Capture visualizations for presentations
- **PDF Reports**: Export predictions with full context (on the Predict page)
- **Deployment URL**: Share app link with stakeholders (no installation required)

## Future Improvements

While the current system demonstrates solid predictive capabilities with an average R² of 0.65, several enhancements could improve accuracy, expand functionality, and increase practical value for energy management stakeholders.

### Enhancing Prediction Accuracy

**Addressing Underperforming Locations**

Three installations (Kahului, USAFA, JDMT) currently achieve lower accuracy scores. Kahului presents particular challenges due to its unique island microclimate and limited training observations. Potential approaches include collecting additional site-specific data, exploring alternative algorithms such as neural networks, or developing specialized feature sets that capture location-specific atmospheric patterns.

**Improving Extreme Condition Predictions**

Analysis reveals that models occasionally underestimate output during optimal weather conditions (clear skies, moderate temperatures, high solar elevation). Developing separate prediction pathways for extreme scenarios or incorporating specialized features for rare high-output conditions would improve forecast reliability across the full operational range.

### Enhancing User Interactivity

**Interactive Geographic Visualization**

Replacing the static location selector with an interactive map interface would provide:
- Direct selection via clickable installation markers
- Real-time performance indicators with color-coded status
- Hover-activated quick statistics (average output, model accuracy tier)
- Pan and zoom controls for regional context

**Multi-Location Comparison Dashboard**

A comparative analysis interface would allow simultaneous evaluation across multiple installations:
- Side-by-side prediction displays with synchronized weather inputs
- Toggle controls to focus on specific location subsets
- Interactive charts showing relative performance under varying conditions
- Exportable comparison reports for stakeholder presentations

**Historical Performance Explorer**

Interactive time-series visualization would provide:
- Actual versus predicted performance tracking
- Seasonal trend analysis with adjustable time ranges
- Animation features demonstrating typical generation patterns
- Data export functionality for external analysis

### Research and Validation Extensions

**Transfer Learning Between Similar Climates**

Investigating whether models trained on one location can generalize to climatically similar sites could reduce data requirements for new installations. For example, testing whether the Travis AFB model performs adequately at nearby March AFB would validate potential efficiency gains in model deployment.

**Prediction Uncertainty Quantification**

Implementing probabilistic forecasting with confidence intervals would enhance decision support. Rather than point predictions, the system would provide ranges (e.g., "17 kW ± 2 kW with 95% confidence"), enabling more sophisticated risk assessment for critical operational decisions. Approaches include quantile regression or bootstrap resampling.

**Long-Term Performance Validation**

Testing model accuracy on recent data (2024-2025) would verify sustained performance and detect potential degradation due to climate shifts or data drift. This validation would confirm whether recalibration or retraining is necessary to maintain operational reliability.

---

## Lessons Learned

**Statistical Significance vs Practical Significance**

The altitude hypothesis provided a crucial lesson: with 20,000+ observations, statistical tests can detect tiny effects that don't matter in practice. Despite a highly significant p-value (< 0.001), altitude explained only 0.5% of variance—essentially negligible. This reinforced the importance of always examining effect sizes alongside p-values, especially with large datasets where even trivial patterns become "statistically significant."

**Location-Specific Modeling Strategy**

Initially, the plan was to build one global model using location as a feature. However, EDA revealed that location alone explains 11.2% of variance with a 2:1 performance ratio between sites. This finding drove the decision to build 12 separate models, allowing each to specialize in its installation's unique climate patterns. The result: significantly better predictions than a generalized approach would have achieved.

**Building My First Streamlit Application**

This was my first experience developing a Streamlit web application, and the learning curve was steep but rewarding. Key lessons included:

- **File organization matters**: Structuring the app with separate pages and utility modules made development much more manageable than cramming everything into one file
- **Dynamic data loading**: Learning to load model performance metrics from CSV files rather than hardcoding values ensures the app always reflects actual training results
- **User experience thinking**: Designing for non-technical stakeholders meant adding help sections, clear explanations, and slider controls instead of free text inputs
- **Deployment considerations**: Understanding the difference between local development and cloud deployment (file paths, dependencies, environment setup)

**Dependency Management for Cloud Deployment**

Initial deployment attempts failed due to overly strict package version requirements. The lesson: local development and cloud deployment have different needs. Changing `requirements.txt` from exact versions (`==`) to minimum versions (`>=`) gave Streamlit Cloud the flexibility to resolve dependencies automatically. Using major.minor versioning (e.g., `pandas>=2.0.0` instead of `pandas==2.0.3`) prevented conflicts while maintaining compatibility. This approach—relaxed but bounded version constraints—is standard practice for production deployments where the hosting environment needs flexibility to install compatible package combinations.

**Feature Engineering Impact**

Starting with 11 base measurements and expanding to 35 engineered features—incorporating solar physics like elevation angles, temperature efficiency factors, and atmospheric attenuation—made a tangible difference in model performance. This validated that domain knowledge combined with machine learning produces better results than algorithms alone.

**When Models Struggle**

Not all locations achieved strong performance, and that's okay. Rather than forcing better metrics through overfitting, accepting that Kahului's unique island climate and limited data yield R² = 0.44 was the honest approach. Documenting these limitations transparently builds trust with stakeholders more than overpromising accuracy.

## Deployment

**Live Application:** [View App](https://solarpower.streamlit.app/)

**Deployment Platform:** Streamlit Community Cloud (free tier)

**Requirements:** All dependencies are specified in `requirements.txt` and will be installed automatically during deployment.

## Acknowledgments

### Dataset

This project uses the **Northern Hemisphere Horizontal Photovoltaic Power Output Dataset** published by Williams, Jada and Wagner, Torrey:

**Citation:**
> Williams, J., & Wagner, T. (2019). Northern Hemisphere Horizontal Photovoltaic Power Output Data for 12 Sites. *Mendeley Data*, V5. https://doi.org/10.17632/hfhwmn8w24.5

**Associated Research Paper:**
> Williams, J., & Wagner, T. (2020). Machine Learning Modeling of Horizontal Photovoltaics Using Weather and Location Data. *Energies*, 13(10), 2570. https://doi.org/10.3390/en13102570

### Resources

**Logo:**
- Solar panel graphics sourced from [PikPNG](https://www.pikpng.com/) (free for personal/educational use)

**Technical Documentation:**
- Streamlit documentation: https://docs.streamlit.io
- scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- XGBoost documentation: https://xgboost.readthedocs.io

### Tools & Frameworks

This project was built using open-source tools including Python, Streamlit, scikit-learn, pandas, matplotlib, seaborn, and plotly. Thank you to the open-source community for making these powerful tools freely available.

## Contact

**Desi Ilieva** | Junior Data Analyst

📧 **Email:** db.ilieva@gmail.com

💼 **LinkedIn:** [Connect with me](www.linkedin.com/in/desislava-ilieva-uk)

---

*This project is part of my data science portfolio demonstrating end-to-end machine learning workflow from data cleaning through model deployment.*
