import math
from sklearn.preprocessing import MinMaxScaler

def prepro(df):
    close_data = df.filter(['Close'])
    close_dataset = close_data.values
    training_data_len = math.ceil(len(close_dataset) * .8) #pour entrainer sur 80% de notre data
    print(f"longueur du training_data {training_data_len}")
    print("---------------------------------------------------------------------------------")
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_close_data = scaler.fit_transform(close_dataset)
    print(scaled_close_data)
    return scaled_close_data, training_data_len, close_dataset, close_data, df





