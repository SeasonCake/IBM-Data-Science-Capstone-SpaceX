# SpaceX Falcon 9 First Stage Landing Prediction

### IBM Applied Data Science Capstone Project

This repository contains the final capstone project for the IBM Applied Data Science Professional Certificate. The project implements a complete data science pipeline to predict the landing success of a SpaceX Falcon 9 first stage. Predicting the outcome of a first-stage landing is crucial as it directly impacts the cost of a launch, with successful landings enabling rocket reuse.

---

## Project Overview

The objective of this project is to build and evaluate a machine learning model that can accurately predict whether the Falcon 9 first stage will land successfully. This is achieved through a systematic workflow encompassing several key stages of the data science lifecycle:

1.  **Data Collection:** Gathering historical launch data from the SpaceX REST API and scraping a supplemental data table from Wikipedia.
2.  **Data Wrangling:** Cleaning, merging, and transforming the raw data into a usable format. This includes creating the target variable `Class` for our classification models.
3.  **Exploratory Data Analysis (EDA):** Utilizing SQL queries and data visualization with `Matplotlib` and `Seaborn` to uncover initial insights and relationships within the dataset.
4.  **Interactive Visual Analytics:** Building interactive geographical maps with `Folium` and a dynamic dashboard with `Plotly Dash` to explore the data in a more user-friendly way.
5.  **Predictive Modeling:** Training, fine-tuning via `GridSearchCV`, and evaluating several classification models (Logistic Regression, Support Vector Machine, Decision Tree, K-Nearest Neighbors) to find the best predictor of launch success.

---

## Repository Structure

This repository is organized into several key folders:

-   📁 **/Note_books**: Contains the four main Jupyter Notebooks that document the entire project workflow, from data collection to machine learning.
    1.  `1_Data_Collection&Wrangling.ipynb`
    2.  `2_Exploratory_Data_Analysis_With_SQL.ipynb`
    3.  `3_Interactive_Visualizations&Maps.ipynb`
    4.  `4_Predictive_Analysis&Machine_Learning.ipynb`
-   📁 **/Python_dashboard**: Includes the standalone Python script for the interactive dashboard (`dashboard_app.py`).
-   📁 **/Data_outcomes**: Contains the cleaned CSV files generated during the project, which serve as inputs for the analysis notebooks.
-   📁 **/Presentation**: Contains the final project presentation in PDF format.
    -   `SpaceX_Launch_Success_Prediction_Presentation.pdf`

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

**[View Final Presentation](./Presentation/SpaceX_Launch_Success_Prediction_Presentation.pdf)**