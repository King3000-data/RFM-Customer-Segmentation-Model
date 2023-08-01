# RFM-Customer-Segmentation-Model
This repository contains an in-depth customer segmentation analysis of an online retail platform. The analysis uses the Recency, Frequency, Monetary Value (RFM) model and K-Means clustering to identify distinct customer segments. Insights from these segments can be used to inform targeted marketing strategies.

# Description
This project segments customers into different groups based on their shopping patterns. By understanding these patterns, businesses can better cater to their customers' needs and improve their strategies accordingly. The RFM model, a popular method for customer segmentation, is used to identify these groups. The K-Means clustering algorithm is then used to form these groups, providing invaluable insights for targeted marketing and customer relationship strategies.

The RFM model and K-Means clustering are applied to an online retail dataset to identify three distinct customer segments. These insights provide a powerful tool for understanding customer behavior and informing strategic decisions in marketing and customer relationship management.

# Files
data_cleaning_and_parsing.py: Script for initial data cleaning and parsing.
outlier_detection_and_visualization.py: Script for outlier detection and visualization.
outlier_removal.py: Script for outlier removal.
EDA_Bar_Charts.py and EDA_Bar_Charts_Top_4_Countries.py: Scripts for preliminary exploratory data analysis.
rfm_creation.py: Script for creating the RFM table.
data_scaling.py: Script for scaling the RFM data.
cluster_analysis.py: Script for determining the optimal number of clusters.
model_implementation.py: Script for implementing the K-Means clustering algorithm.

# Installation
The use of Python is all you need. I used version 3.11. Ensure dependencies are installed using pip install through CMD. It is recommend you make the package installations global should you have multiple python versions installed.
For example:
Seaborn
MatPlotLib
Numpy

You may view what to install through each script where it imports the necessary packages.

# Usage
Run each script sequentially as they will not run correctly, nor give the desired data results if done out of operating order.
There are additional scripts which may run at any point but are not necessary for the pipeline. They are more for convenience of data viewing and preparation.
