# SpaceX Falcon 9 First Stage Landing Prediction

### IBM Applied Data Science Capstone Project

This repository contains the final capstone project for the IBM Applied Data Science Professional Certificate. The project implements a complete data science pipeline to predict the landing success of a SpaceX Falcon 9 first stage. Predicting the outcome of a first-stage landing is crucial as it directly impacts the cost of a launch, with successful landings enabling rocket reuse.

---

## Project Overview

The objective of this project is to build and evaluate a machine learning model that can accurately predict whether the Falcon 9 first stage will land successfully. This is achieved through a systematic workflow encompassing several key stages of the data science lifecycle:

1.  **Data Collection:** Gathering historical launch data from the SpaceX REST API and scraping a supplemental data table from Wikipedia.
2.  **Data Wrangling:** Cleaning, merging, and transforming the raw data into a usable format and engineering the final target variable for classification.
3.  **Exploratory Data Analysis (EDA):** Utilizing SQL queries and data visualization with `Matplotlib` and `Seaborn` to uncover initial insights.
4.  **Interactive Visual Analytics:** Building interactive geographical maps with `Folium` and a dynamic dashboard with `Plotly Dash`.
5.  **Predictive Modeling:** Training and tuning several machine learning models to find the best predictor of launch success.

---

## Key Findings & Results

This analysis yielded several key insights into the factors driving Falcon 9 landing success and resulted in a high-performing predictive model.

*   **Key Success Factors:** Exploratory Data Analysis confirmed that **Launch Site**, **Payload Mass**, **Orbit Type**, and **Booster Version** are all significant predictors of the landing outcome.

*   **Top Performers:** The **KSC LC-39A** launch site and the modern **Falcon 9 B5 booster version** demonstrated the highest success rates, highlighting them as the most reliable assets in the program.

*   **Predictive Model Performance:** A **Decision Tree classifier** was identified as the best-performing model, achieving a **90.3% cross-validation accuracy** during tuning and a final **83.3% accuracy** on the unseen test data.

*   **Final Conclusion:** The project successfully demonstrates that Falcon 9 landing outcomes can be predicted with a high degree of confidence. The resulting model serves as a valuable proof-of-concept for a decision-support tool to aid in mission planning and risk assessment.

---

## Repository Structure

This repository is organized into the following folders:

-   **/Note_books**: Contains the four main Jupyter Notebooks that document the entire project workflow.
    1.  `1_Data_Collection&Wrangling.ipynb`
    2.  `2_Exploratory_Data_Analysis_With_SQL&Matplotlib.ipynb`
    3.  `3_Interactive_Visualizations&Maps.ipynb`
    4.  `4_Predictive_Analysis&Machine_Learning.ipynb`
-   **/Python_dashboard**: Includes the standalone Python script for the interactive dashboard (`dashboard_app.py`).
-   **/Data_outcomes**: Contains the cleaned CSV files generated during the project.
-   **/Presentation**: Contains the final project presentation in PDF format.
    -   `Data_Science_Project_An_Analysis_and_Prediction_of_SpaceX_Launch_Success.pdf`

---

## Tools and Libraries Used

-   **Data Collection:** `requests`, `BeautifulSoup`
-   **Data Manipulation & Analysis:** `pandas`, `numpy`, `SQLAlchemy`, `SQLite`
-   **Data Visualization:** `matplotlib`, `seaborn`, `folium`
-   **Interactive Dashboard:** `plotly`, `dash`
-   **Machine Learning:** `scikit-learn`

---

## How to Run the Interactive Dashboard

To launch the interactive dashboard on your local machine, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/SeasonCake/IBM-Data-Science-Capstone-SpaceX.git
    cd IBM-Data-Science-Capstone-SpaceX
    ```
2.  **Install Dependencies:**
    ```bash
    pip install pandas dash plotly requests
    ```
3.  **Run the Application:**
    ```bash
    python Python_dashboard/dashboard_app.py
    ```
4.  **View in Browser:**
    Open your web browser and navigate to `http://127.0.0.1:8050/`.

---

## Final Presentation

A comprehensive summary of the project's methodology, key findings, and final model recommendations is available in the final presentation PDF.

**[View Final Presentation](https://github.com/SeasonCake/IBM-Data-Science-Capstone-SpaceX/blob/main/Presentation/Data_Science_Project_An_Analysis_and_Prediction_of_SpaceX_Launch_Success.pdf)**
