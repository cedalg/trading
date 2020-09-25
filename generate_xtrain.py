import numpy as np

def generate_x_train(scaled_close_data, training_data_len, close_dataset, close_data, df):
    train_close_data = scaled_close_data[0:training_data_len, :]
    x_train = []
    y_train = []
    for i in range(60, len(train_close_data)):
        x_train.append(train_close_data[i-60:i, 0])
        y_train.append(train_close_data[i,0]) #60 values from index 0 to 59
    print(x_train)
    x_train, y_train = np.array(x_train), np.array(y_train)
    print(f'dimension de x_train : {x_train.shape}')
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1)) #x_train.shape == 60
    print(f'dimension de x_train : {x_train.shape}')
    return x_train, y_train, df