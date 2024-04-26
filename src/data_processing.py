import pandas as pd

def load_data():
    tesla_data = pd.read_csv('dataset/acciones_tesla_mensuales.csv')
    toyota_data = pd.read_csv('dataset/acciones_toyota_mensuales.csv')
    return tesla_data, toyota_data

def split_data(data, train_end, test_start, test_end, predict_start):
    train = data[:train_end]
    test = data[test_start:test_end]
    predict = data[predict_start:]
    return train, test, predict