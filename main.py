import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sb



## function to read past data for the chosen stock.
##based on persons input
def data_presentation():
#CSV file used for plot
    data = pd.read_csv('VTGN.csv')

    rows = data.shape

# print(rows, "\n", data, "\n")

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

    # Showing the data in a graph
    # plt.figure(figsize=(20,10))
    # plt.plot(data['Close'])
    # plt.title('Stock Close price.', fontsize=15)
    # plt.ylabel('Price in dollars.')
    # plt.show()

    #show the actual values
    print("Actual values:\n", test_data[target])

    # show the models accuracy
    accuracy = model.score(test_data[features], test_data[target])
    print("Accuracy: \n", accuracy)

    plt.plot(data['Close'], label = 'Close Price')
    plt.plot(test_data[target].index, predictions, label = "Predictions")
    plt.legend()
    plt.show()

    #calling fucntion data_presentation()
data_presentation()