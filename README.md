<table>
  <tr>
    <td>
      <img src="images/solar.png" alt="Logo" width="500" height="100">
    </td>
    <td>
      <h1>Northern Hemisphere Photovoltaic Analysis</h1>

**Northern Hemisphere Photovoltaic Analysis** is a comprehensive machine learning project that predicts solar power generation across 12 military installations in the Northern Hemisphere. By analyzing weather conditions, geographic features, and time-based patterns, this project helps energy managers forecast photovoltaic output and optimize renewable energy operations.

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



## Ethical considerations
* Were there any data privacy, bias or fairness issues with the data?
* How did you overcome any legal or societal issues?

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- Logo downloaded: https://www.pikpng.com/
- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Williams, Jada; Wagner, Torrey (2019), “Northern Hemisphere Horizontal Photovoltaic Power Output Data for 12 Sites”, Mendeley Data, V5, doi: 10.17632/hfhwmn8w24.5
* https://www.mdpi.com/1996-1073/13/10/2570?utm_source=chatgpt.com

