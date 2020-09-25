import matplotlib.pyplot as plt

def plot_pred(valid, predictions, rmse, train, df):
    plt.figure(figsize=(16,8))
    plt.title('Model')
    plt.xticks(range(0,df.shape[0],200),df['Date'].loc[::200],rotation=45)
    print(df.shape[0])
    print('up')
    plt.xlabel('Date')
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(train['Close'])
    plt.plot(valid[['Close', 'Predictions']])
    plt.legend(['Train', 'Validation', 'Predictions'], loc='lower right')
