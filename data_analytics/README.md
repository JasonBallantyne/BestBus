# Cleaning Notebook
Sets up the workspace, cleans the leavetimes dataset, cleans the trips dataset, cleans the vehicles dataset and cleans the weather dataset.
Each cleaned dataframe has it's own data quality plan to explain the rational behind the decisions made.
Each dataframe has been exported to it's own cleaned csv.

# Building & Testing Models
Functions to easily clean the dataframes once we split them.
Merging leavetimes and weather dataframes for analysis.
Adding new features to trips dataframe.
Setting up dataframe for models based off of route 68, direction 1, merged with weather data.
Building and Testing models on this dataframe. (Decision Tree, Random Forest Regressor, K-Nearest Neighbour, Linear Regression).
Testing the accuracy of these models using statistical measurements (R2 Score, Mean absolute error and Root Mean Square Error).
Discussing our results and choosing a predictive model to carry out on the rest of our dataset.
