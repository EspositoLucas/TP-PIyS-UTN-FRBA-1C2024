# # prediccion 2024

# import pandas as pd

# def load_data():
#     tesla_data = pd.read_csv('dataset/acciones_tesla_estacionaria.csv')
#     toyota_data = pd.read_csv('dataset/acciones_toyota_estacionaria.csv')

#     tesla_data['date'] = pd.to_datetime(tesla_data['date'], format='%d/%m/%y')
#     toyota_data['date'] = pd.to_datetime(toyota_data['date'], format='%d/%m/%y')
    
#     tesla_data.set_index('date', inplace=True)
#     toyota_data.set_index('date', inplace=True)
    
#     tesla_data = tesla_data.sort_index()
#     toyota_data = toyota_data.sort_index()

#     return tesla_data, toyota_data

# def split_data(data, train_end, test_start, test_end, predict_start):
#     train_end = find_nearest(data, train_end)
#     test_start = find_nearest(data, test_start)
#     test_end = find_nearest(data, test_end)
#     predict_start = find_nearest(data, predict_start)

#     train = data.loc[:train_end, 'close_detrended']
#     test = data.loc[test_start:test_end, 'close_detrended']
#     predict = data.loc[predict_start:, 'close_detrended']
#     return train, test, predict

# # Encontrar el índice más cercano a la fecha dada
# def find_nearest(data, value):
#     idx = data.index.get_indexer([value], method='nearest')
#     return data.index[idx[0]] 

# def sumar_media(data_original, resultados_predict):
#     media = data_original['close'].mean()
#     resultados_predict = resultados_predict + media
#     return resultados_predict



# prediccion 2025

import pandas as pd

def load_data():
    tesla_data = pd.read_csv('dataset/2025/acciones_tesla_estacionaria_2025.csv')
    toyota_data = pd.read_csv('dataset/2025/acciones_toyota_estacionaria_2025.csv')

    tesla_data['date'] = pd.to_datetime(tesla_data['date'], format='%d/%m/%y')
    toyota_data['date'] = pd.to_datetime(toyota_data['date'], format='%d/%m/%y')
    
    tesla_data.set_index('date', inplace=True)
    toyota_data.set_index('date', inplace=True)
    
    tesla_data = tesla_data.sort_index()
    toyota_data = toyota_data.sort_index()

    return tesla_data, toyota_data

def split_data(data, train_end, test_start, test_end, predict_start, predict_end):
    train_end = find_nearest(data, train_end)
    test_start = find_nearest(data, test_start)
    test_end = find_nearest(data, test_end)
    predict_start = find_nearest(data, predict_start)
    predict_end = find_nearest(data, predict_end)

    train = data.loc[:train_end, 'close_detrended']
    test = data.loc[test_start:test_end, 'close_detrended']
    predict = data.loc[predict_start:predict_end, 'close_detrended']
    return train, test, predict

# Encontrar el índice más cercano a la fecha dada
def find_nearest(data, value):
    idx = data.index.get_indexer([value], method='nearest')
    return data.index[idx[0]]


def sumar_media(data_original, resultados_predict):
    media = data_original['close'].mean()
    resultados_predict = resultados_predict + media
    return resultados_predict
