import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Load stock data (example: Apple - AAPL)
data = yf.download("AAPL", start="2015-01-01", end="2016-12-31")
print(data.head())

# 2. Prepare dataset
data['Prediction'] = data['Close'].shift(-30)  # predict 30 days into future

X = np.array(data[['Close']])[:-30]
y = np.array(data['Prediction'])[:-30]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate
predictions = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, predictions))

# 6. Predict future prices
future_prices = model.predict(data[['Close']][-30:])
print("Next 30 days prediction:\n", future_prices)

# 7. Plot
plt.figure(figsize=(10,6))
plt.plot(y_test[:50], label="Real Price")
plt.plot(predictions[:50], label="Predicted Price")
plt.legend()
plt.show()
