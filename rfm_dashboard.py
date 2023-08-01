# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Load the data
rfm_data = pd.read_csv("rfm_data.csv")

# Create a Dash application
app = dash.Dash(__name__)

# Define the application layout
app.layout = html.Div([
    # Create a dropdown for page selection
    dcc.Dropdown(
        id='page-dropdown',
        options=[
            {'label': '3D Scatter Plot', 'value': 'scatter'},
            {'label': 'Bar Plot', 'value': 'bar'},
            {'label': 'Pie Chart', 'value': 'pie'}
        ],
        value='scatter'
    ),
    html.Div(id='page-content')
])

# Update page content based on the selected page
@app.callback(
    Output('page-content', 'children'),
    Input('page-dropdown', 'value'))
def update_page(value):
    if value == 'scatter':
        # Create a 3D scatter plot
        fig = px.scatter_3d(rfm_data, x='Recency', y='Frequency', z='MonetaryValue', color='Cluster', hover_data=['Cluster'])
        return dcc.Graph(figure=fig)
    elif value == 'bar':
        # Create a bar plot for average RFM values across clusters
        avg_rfm = rfm_data.groupby('Cluster').mean().reset_index()
        fig = px.bar(avg_rfm, x='Cluster', y=['Recency', 'Frequency', 'MonetaryValue'], barmode='group', title='Average RFM Values Across Clusters')
        return dcc.Graph(figure=fig)
    elif value == 'pie':
        # Create a pie chart for the distribution of customers across clusters
        cluster_counts = rfm_data['Cluster'].value_counts().reset_index()
        cluster_counts.columns = ['Cluster', 'Count']
        fig = px.pie(cluster_counts, values='Count', names='Cluster', title='Customer Distribution Across Clusters')
        return dcc.Graph(figure=fig)

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
