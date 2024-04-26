import pandas as pd

def load_data():
    tesla_data = pd.read_csv('dataset/acciones_tesla_normalizados.csv')
    toyota_data = pd.read_csv('dataset/acciones_toyota_normalizados.csv')

    tesla_data['date'] = pd.to_datetime(tesla_data['date'], format='%Y-%m-%d')
    toyota_data['date'] = pd.to_datetime(toyota_data['date'], format='%Y-%m-%d')
    
    tesla_data.set_index('date', inplace=True)
    toyota_data.set_index('date', inplace=True)
    
    tesla_data = tesla_data.sort_index()
    toyota_data = toyota_data.sort_index()

    return tesla_data, toyota_data

def split_data(data, train_end, test_start, test_end, predict_start):
    train_end = find_nearest(data, train_end)
    test_start = find_nearest(data, test_start)
    test_end = find_nearest(data, test_end)
    predict_start = find_nearest(data, predict_start)

    train = data[:train_end]
    test = data[test_start:test_end]
    predict = data[predict_start:]
    return train, test, predict

# Encontrar el índice más cercano a la fecha dada
def find_nearest(data, value):
    idx = data.index.get_indexer([value], method='nearest')
    return data.index[idx[0]]