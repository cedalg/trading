import math
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import urllib.request, json
import os
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropoutr

def lstm(x_train, training_data_len, close_dataset, close_data, df, y_train):
    model = Sequential()
   #50 nerons
    model.add(LSTM(50, return_sequences=True, input_shape= (x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
   #25neurons
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=1000, epochs=2)
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_close_data = scaler.fit_transform(close_dataset)
    test_data = scaled_close_data[training_data_len - 60: , :]
    x_test= []
    y_test= close_dataset[training_data_len:, :]
    for i in range (60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])
       #y_test.append()
       #converting data to np array 
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    x_test.shape
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    rmse = np.sqrt(np.mean(predictions - y_test)**2)
    train = close_data[:training_data_len]
    valid = close_data[training_data_len:]
    valid['Predictions'] = predictions
    print(f'rmse : {rmse}, valid : {valid},predictions : {predictions}')
    print(df.Date)
    return valid, predictions, rmse, train, df