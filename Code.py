import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('house_data.csv')
X = data[['SquareFootage', 'Bedrooms', 'Bathrooms']]
y = data['Price']

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
new_data = np.array([[1700, 3, 2], [1600, 2, 1]])
predicted_prices = model.predict(new_data)
print(predicted_prices)

