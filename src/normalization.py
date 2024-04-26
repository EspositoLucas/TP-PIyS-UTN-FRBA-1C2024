import pandas as pd

def normalize_data(input_file, output_file):
    data = pd.read_csv(input_file, parse_dates=['date'])
    
    data['date'] = pd.to_datetime(data['date'], format='%d/%m/%y')
    data['close'] = (data['close'] - data['close'].min()) / (data['close'].max() - data['close'].min())

    data = data[['date', 'close']]

    data.to_csv(output_file, index=False)

normalize_data('dataset/MacroTrends_Data_Download_TM.csv', 'dataset/acciones_toyota_normalizados.csv')
normalize_data('dataset/MacroTrends_Data_Download_TSLA.csv', 'dataset/acciones_tesla_normalizados.csv')