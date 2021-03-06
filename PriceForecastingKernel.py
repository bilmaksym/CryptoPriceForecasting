import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import mean_squared_error
from math import sqrt
from random import randint
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import GRU
from keras.callbacks import EarlyStopping
from keras import initializers
from datetime import datetime
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import plotly.offline as py
import plotly.graph_objs as go
from DataLoader import DataLoader


# py.init_notebook_mode(connected=True)
# get_ipython().run_line_magic('matplotlib', 'inline')


def create_lookback(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back):
        X.append([dataset[i, 0]])
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)


# This function prepares random train/test split,
# scales data with MinMaxScaler, create time series labels (Y)
def get_split(working_data, n_train, n_test, look_back=1):
    # get a point from which we start to take train dataset and after it - test dataset
    start_point = len(working_data) - n_test - n_train
    df_train = working_data[start_point:start_point + n_train]
    df_test = working_data[start_point + n_train:start_point + n_train + n_test]

    training_set = df_train.values
    training_set = np.reshape(training_set, (len(training_set), 1))
    test_set = df_test.values
    test_set = np.reshape(test_set, (len(test_set), 1))

    # scale datasets
    scaler_cv = MinMaxScaler()
    training_set = scaler_cv.fit_transform(training_set)
    test_set = scaler_cv.transform(test_set)

    # create datasets which are suitable for time series forecasting
    X_train, Y_train = create_lookback(training_set, look_back)
    X_test, Y_test = create_lookback(test_set, look_back)

    # reshape datasets so that they will be ok for the requirements of the models in Keras
    X_train = np.reshape(X_train, (len(X_train), 1, X_train.shape[1]))
    X_test = np.reshape(X_test, (len(X_test), 1, X_test.shape[1]))

    return X_train, Y_train, X_test, Y_test, scaler_cv, start_point


# This function takes datasets from the get_split function as input and train model using these datasets,,,,,,,,,,,
def train_model_GRU(X_train, Y_train, X_test, Y_test):
    # initialize sequential model, add bidirectional LSTM layer and densely connected output neuron
    model = Sequential()
    model.add(GRU(256, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dense(1))

    # compile and fit the model
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X_train, Y_train, epochs=100, batch_size=16, shuffle=False,
              validation_data=(X_test, Y_test), verbose=0,
              callbacks=[EarlyStopping(monitor='val_loss', min_delta=5e-5, patience=20, verbose=0)])
    return model


# This function takes datasets from the get_split function as input and train model using these datasets
def train_model_LSTM(X_train, Y_train, X_test, Y_test):
    # initialize sequential model, add 2 stacked LSTM layers and densely connected output neuron
    model = Sequential()
    model.add(LSTM(256, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(LSTM(256))
    model.add(Dense(1))

    # compile and fit the model
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X_train, Y_train, epochs=100, batch_size=16, shuffle=False,
              validation_data=(X_test, Y_test), verbose=0,
              callbacks=[EarlyStopping(monitor='val_loss', min_delta=5e-5, patience=20, verbose=0)])
    return model


# This function uses trained model and test dataset to calculate RMSE
def get_rmse(model, X_test, Y_test, scaler, start_point, working_data, n_train):
    # add one additional data point to align shapes of the predictions and true labels
    X_test = np.append(X_test,
                       scaler.transform(working_data.iloc[start_point + n_train + len(X_test)][0].reshape(1, -1)))
    X_test = np.reshape(X_test, (len(X_test), 1, 1))

    # get predictions and then make some transformations to be able to calculate RMSE properly in USD
    prediction = model.predict(X_test)
    prediction_inverse = scaler.inverse_transform(prediction.reshape(-1, 1))
    Y_test_inverse = scaler.inverse_transform(Y_test.reshape(-1, 1))
    prediction2_inverse = np.array(prediction_inverse[:, 0][1:])
    Y_test2_inverse = np.array(Y_test_inverse[:, 0])

    # calculate RMSE
    RMSE = sqrt(mean_squared_error(Y_test2_inverse, prediction2_inverse))
    return RMSE, prediction2_inverse, Y_test2_inverse


# The function uses all previous functions to build workflow of calculations and return RMSE and predictions of the model.
def workflow(working_data, get_split, train_model, get_rmse, n_train=250, n_test=50, look_back=1):
    X_train, Y_train, X_test, Y_test, scaler, start_point = get_split(working_data, n_train, n_test)
    model = train_model(X_train, Y_train, X_test, Y_test)
    RMSE, predictions, y_inverse = get_rmse(model, X_test, Y_test, scaler, start_point, working_data, n_train)
    return RMSE, predictions, y_inverse


# This function is used to repeat the workflow ten times and to calculate average RMSE
def cross_validate(working_data, get_split, train_model, get_rmse, workflow, n_train=250, n_test=50, look_back=1):
    rmse_list = []
    for i in range(10):
        print('Iteration:', i + 1)
        RMSE, _ = workflow(working_data, get_split, train_model, get_rmse, n_train, n_test, look_back)
        rmse_list.append(RMSE)
        print('Test RMSE: %.3f' % RMSE)
    mean_rmse = np.mean(rmse_list)
    return mean_rmse, rmse_list


def data_preparation(dataframe):
    """
            Some manipulations with date before proceeding data ahead
            :param dataframe: data loaded from exchange
            :return: dataframe with date as index and close price as value
            """
    working_data = dataframe
    group = working_data.groupby('timestamp')
    working_data = group['close'].mean()
    working_data = working_data.reset_index()
    working_data.timestamp = pd.to_datetime(working_data.timestamp)
    working_data = working_data.set_index('timestamp')
    return working_data


def plot_graph(working_data, n_test, prediction2_inverse, Y_test2_inverse):
    Test_Dates = working_data[len(working_data) - n_test:].index

    trace1 = go.Scatter(x=Test_Dates, y=Y_test2_inverse, name='Actual Price',
                        line=dict(color='rgb(66, 244, 155)', width=2))
    trace2 = go.Scatter(x=Test_Dates, y=prediction2_inverse, name='Predicted Price',
                        line=dict(color='rgb(244, 146, 65)', width=2))
    data = [trace1, trace2]
    layout = dict(title='Comparison of true prices (on the test dataset) with prices our model predicted, by dates',
                  xaxis=dict(title='Date'), yaxis=dict(title='Price, USDT'))
    fig = go.Figure(data=data, layout=layout)
    fig.show()

# Constants
API_SECRET = "iCnm9Pqr0X8pVDgKr661q8Vvs3WrCQ8WVgKljFvkln4V9hegqbZKe7VI4I8Xl0ES"
API_KEY = "rnJ0EQ9RLAt1HPeQ3uQ4wpk1IkDLe99lzvMjwmzlgZz6EraKeYFU6Ou40lMjTZhr"
if __name__ == "__main__":
    loader = DataLoader(API_KEY, API_SECRET)
    working_data = data_preparation(loader.load_data("BTCUSDT", "1h", 660))
    n_test = 60

    RMSE, predictions, y_inverse = workflow(working_data, get_split, train_model_LSTM, get_rmse, n_train=600, n_test=n_test)
    print('Test GRU model RMSE: %.3f' % RMSE)

    plot_graph(working_data, n_test, predictions, y_inverse)