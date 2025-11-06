<table>
  <tr>
    <td>
      <img src="images/solar.png" alt="Logo" width="500" height="100">
    </td>
    <td>
      <h1>Northern Hemisphere Photovoltaic Analysis</h1>

**Northern Hemisphere Photovoltaic Analysis** is a data-driven project designed to explore, analyze, and predict solar power generation across multiple locations. Using weather, geographic, and temporal data, this project builds predictive models for photovoltaic energy output, identifies key environmental factors affecting efficiency, and provides actionable insights for energy management, grid planning, and renewable energy optimization.  

The project combines **ETL, exploratory data analysis (EDA), and machine learning modeling** to help stakeholders understand patterns, forecast solar production, and make informed operational decisions.
    </td>
  </tr>
</table>

## Dataset Content & Description

This dataset accompanies the paper *"Machine Learning Modeling of Horizontal Photovoltaics Using Weather and Location Data"* submitted to the *Journal of Renewable Energy*. It contains **power output measurements from horizontal photovoltaic panels** located at 12 Northern Hemisphere sites over a period of 14 months.

Each row represents a recorded observation at a specific date, time, and location. The dataset includes the following **independent variables**:

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
      <td>The name or ID of the observation site or station.</td>
    </tr>
    <tr>
      <td>Date</td>
      <td>int64</td>
      <td>The date when the data was recorded (YYYYMMDD format).</td>
    </tr>
    <tr>
      <td>Time</td>
      <td>int64</td>
      <td>The time of observation in 24-hour format (HHMM).</td>
    </tr>
    <tr>
      <td>Latitude</td>
      <td>float64</td>
      <td>Geographic coordinate showing how far north or south the location is.</td>
    </tr>
    <tr>
      <td>Longitude</td>
      <td>float64</td>
      <td>Geographic coordinate showing how far east or west the location is.</td>
    </tr>
    <tr>
      <td>Altitude</td>
      <td>int64</td>
      <td>Elevation of the observation site above sea level (meters).</td>
    </tr>
    <tr>
      <td>YRMODAHRMI</td>
      <td>float64</td>
      <td>Combined timestamp code (Year, Month, Day, Hour, Minute).</td>
    </tr>
    <tr>
      <td>Month</td>
      <td>int64</td>
      <td>Month number extracted from the date (1–12).</td>
    </tr>
    <tr>
      <td>Hour</td>
      <td>int64</td>
      <td>Hour of the day extracted from the time (0–23).</td>
    </tr>
    <tr>
      <td>Season</td>
      <td>object</td>
      <td>Derived season (Winter, Spring, Summer, Autumn) based on the date.</td>
    </tr>
    <tr>
      <td>Humidity</td>
      <td>float64</td>
      <td>Relative humidity (%) at the time of measurement.</td>
    </tr>
    <tr>
      <td>AmbientTemp</td>
      <td>float64</td>
      <td>Ambient air temperature (°C).</td>
    </tr>
    <tr>
      <td>PolyPwr</td>
      <td>float64</td>
      <td>Measured photovoltaic (solar) power output (Watts).</td>
    </tr>
    <tr>
      <td>Wind.Speed</td>
      <td>int64</td>
      <td>Wind speed at the location (m/s).</td>
    </tr>
    <tr>
      <td>Visibility</td>
      <td>float64</td>
      <td>Horizontal visibility distance (km).</td>
    </tr>
    <tr>
      <td>Pressure</td>
      <td>float64</td>
      <td>Atmospheric pressure (hPa).</td>
    </tr>
    <tr>
      <td>Cloud.Ceiling</td>
      <td>int64</td>
      <td>The height of the lowest cloud layer (feet or meters).</td>
    </tr>
  </tbody>
</table>

</div>


This dataset enables exploration of **environmental and temporal factors affecting solar panel performance** and supports **predictive modeling of photovoltaic power output** for energy planning and optimization.

## Business Requirements
The Northern Hemisphere Photovoltaic Analysis project aims to provide actionable insights and predictive capabilities for solar energy management. The key business requirements are:

## Business Requirements

The Northern Hemisphere Photovoltaic Analysis project aims to provide actionable insights and predictive capabilities for solar energy management. A single predictive model will be trained on data from all sites, leveraging location as a feature to forecast output for any site in the dataset.

| # | Business Requirement | Description |
|---|--------------------|-------------|
| 1 | Forecast Solar Power Output | Predict photovoltaic power output using weather, temporal, and location data. Support energy managers with grid planning, energy storage optimization, and operational scheduling. |
| 2 | Identify Key Environmental Factors | Determine which weather conditions and environmental variables most influence solar power output. Provide insights into how temperature, humidity, cloud cover, wind, and geographic location affect efficiency. |
| 3 | Support Site Planning and Maintenance | Highlight high- and low-performing locations across all sites. Identify periods of expected low output to assist with maintenance scheduling or operational planning. |
| 4 | Visualize Performance Trends | Present solar power trends by hour, month, and season. Show geographic differences in energy output to support data-driven decision making. |
| 5 | Enable Data-Driven Decisions | Provide interpretable predictions and insights for stakeholders interested in optimizing renewable energy generation. Generate visualizations, dashboards, or reports that communicate predictive results effectively. |


*Note: A single predictive model will be trained on data from all sites, leveraging location as a feature, so it can forecast output for any site in the dataset.*


## Hypotheses and Validation

This section outlines key hypotheses for the Northern Hemisphere Photovoltaic Analysis project and how each will be validated through analysis or modeling.

| # | Hypothesis | Validation Approach |
|---|------------|-------------------|
| 1 | Higher humidity reduces solar power output. | Analyze correlation between `Humidity` and `PolyPwr`; visualize with scatter plots and regression analysis. |
| 2 | Cloud ceiling negatively correlates with photovoltaic power output. | Scatter plots of `Cloud.Ceiling` vs `PolyPwr`; compute correlation coefficients; test with regression models. |
| 3 | Solar power output is higher in summer and at midday. | Plot `PolyPwr` by `Month` and `Hour`; use boxplots and line charts to highlight seasonal and daily patterns. |
| 4 | Altitude affects efficiency. | Compare `PolyPwr` across sites with different `Altitude`
| 5 | Location matters — some sites consistently produce more energy. | Aggregate `PolyPwr` by `Location`; visualize using bar charts or maps to compare average performance across sites. |


## Project Plan
* Outline the high-level steps taken for the analysis.
* How was the data managed throughout the collection, processing, analysis and interpretation steps?
* Why did you choose the research methodologies you used?

## The rationale to map the business requirements to the Data Visualisations
* List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used
* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques. Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

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
* https://news.tuoitre.vn/southern-vietnam-records-lowest-temperature-in-over-40-years-10358779.htm
https://rajibshaw.org/wpRS/wp-content/uploads/2018/09/Vietnam-CC-and-Drought-Mekong.pdf