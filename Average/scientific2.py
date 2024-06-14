import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from data import data

a = [item for sublist in data[8:40] for item in sublist]

# Example of your own list of 4-digit integers (replace this with your dataset)
your_lottery_data = a#[5431, 1234, 1892, 2205, 3056, 5078, 1843, 2289, 3652, 4219, 1835, 2297, 3661, 1854, 4268]

# Create a DataFrame from your dataset
lottery_data = pd.DataFrame({'Draw': range(1, len(your_lottery_data) + 1), 'Number': your_lottery_data})

# Extract features (draw number) and target (lottery number)
X = lottery_data[['Draw']].values
y = lottery_data['Number'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Example of predicting the next lottery number
next_draw_number = model.predict([[lottery_data['Draw'].max() + 1]])
print("Predicted next lottery number:", next_draw_number[0])
