# Import required libraries
import pandas as pd
import requests
from io import BytesIO
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# -------------------- Data Loading --------------------
# Download the dataset from the URL
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
try:
    response = requests.get(URL)
    response.raise_for_status()  # Raise an exception for bad status codes
    spacex_df = pd.read_csv(BytesIO(response.content))
    print("SpaceX dataset downloaded and loaded successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error downloading data: {e}")
    # As a fallback, try to load a local copy if it exists
    try:
        spacex_df = pd.read_csv("spacex_launch_dash.csv")
        print("Loaded local copy of the dataset.")
    except FileNotFoundError:
        print("Fallback local file not found. Please check your internet connection.")
        exit()

# Get max and min payload values for the slider
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# -------------------- Dash App Initialization --------------------
app = dash.Dash(__name__)

# Create the layout of the app
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36',
                   'font-size': 40}),
    
    # TASK 1: Add a dropdown list to enable Launch Site selection
    # The default select value is for ALL sites
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'} # Note: This seems to be a duplicate in the original lab
                 ],
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True
                 ),
    html.Br(),

    # TASK 2: Add a pie chart to show the total successful launches count for all sites
    # If a specific launch site was selected, show the Success vs. Failed counts for the site
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # TASK 3: Add a slider to select payload range
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={i: f'{i}' for i in range(0, 10001, 1000)},
                    value=[min_payload, max_payload]),

    # TASK 4: Add a scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# -------------------- Callback Functions --------------------

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # For all sites, show the success rate per site
        fig = px.pie(spacex_df, 
                     values='class', 
                     names='Launch Site', 
                     title='Total Success Launches by Site')
        return fig
    else:
        # For a specific site, show the success vs failure counts
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Group by the 'class' column (0 for failure, 1 for success)
        site_df = filtered_df.groupby(['class'], as_index=False).count()
        site_df.rename(columns={'Launch Site': 'count'}, inplace=True)
        # Manually set names for the pie chart slices
        site_df['Outcome'] = site_df['class'].apply(lambda x: 'Success' if x == 1 else 'Failure')
        
        fig = px.pie(site_df, 
                     values='count', 
                     names='Outcome', 
                     title=f'Total Success vs. Failure for Site {entered_site}',
                     color='Outcome',
                     color_discrete_map={'Success':'green', 'Failure':'red'})
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), 
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_plot(entered_site, payload_range):
    low, high = payload_range
    # Filter by payload range
    df_filtered = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    
    if entered_site == 'ALL':
        # Render scatter plot for all sites
        fig = px.scatter(df_filtered, 
                         x='Payload Mass (kg)', 
                         y='class', 
                         color='Booster Version Category',
                         title=f'Payload vs. Launch Outcome for All Sites (Payload: {low}-{high} kg)')
        return fig
    else:
        # Filter further by the selected site
        df_site_filtered = df_filtered[df_filtered['Launch Site'] == entered_site]
        fig = px.scatter(df_site_filtered, 
                         x='Payload Mass (kg)', 
                         y='class', 
                         color='Booster Version Category',
                         title=f'Payload vs. Launch Outcome for {entered_site} (Payload: {low}-{high} kg)')
        return fig

# -------------------- Main Execution Block --------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)