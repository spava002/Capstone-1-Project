import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sb
import csv


#CSV file used for plot
data = pd.read_csv('GOOG.csv')

rows = data.shape

# splitting to train and test data sets
train_data = data.iloc[:int(.99*len(data)), :]
test_data = data.iloc[:int(.99*len(data)):, :]

# Defining the features and target variable
features = ['Open', 'Volume']
target = 'Close'

#XGBBoost model training
model = xgb.XGBRegressor()
model.fit(train_data[features], train_data[target])

predictions = model.predict(test_data[features])
print("Predictions: \n", predictions)

#showing the stocks values
print("Actual values:\n", test_data[target])

# show the models accuracy
accuracy = model.score(test_data[features], test_data[target])
print("Accuracy: \n", accuracy)
plt.plot(data['Close'], label = 'Close Price')
plt.plot(test_data[target].index, predictions, label = "Predictions")
plt.legend()
plt.show()

# Write a stocks value predictions and actual values to a CSV file
filename = 'predictions.csv'
fields = ['Actual','Prediction']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for actual, prediction in zip(test_data[target], predictions):
        writer.writerow({'Actual': actual, 'Prediction': prediction})