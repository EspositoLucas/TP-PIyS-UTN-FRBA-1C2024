
# # prediccion 2024

# import matplotlib.pyplot as plt
# import pandas as pd

# def plot_results(data, train, test, predict, arima_seasonal_pred, arima_non_seasonal_pred, stl_pred, linear_pred, arima_seasonal, arima_non_seasonal, stl, linear, empresa):
#     media = data['close'].mean()

#     # Datos reales
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.plot(data.index, data['close'], label='Datos reales')
#     ax.plot(train.index, train, label='Entrenamiento')
#     ax.plot(test.index, test, label='Prueba')
#     ax.set_title(f'Predicción de precios de acciones de {empresa}')
#     ax.legend()
#     plt.show()


#     # ARIMA Seasonal + Media
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.plot(predict.index, arima_seasonal, color='blue', label='Predicción')
#     ax.plot(predict.index, data.loc[predict.index, 'close'], color='red', label='Datos reales')
#     ax.set_title(f'Predicción con ARIMA Seasonal para {empresa}')
#     ax.legend()
#     plt.show()


#     # ARIMA No Seasonal + Media
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.plot(predict.index, arima_non_seasonal, color='blue', label='Predicción')
#     ax.plot(predict.index, data.loc[predict.index, 'close'], color='red', label='Datos reales')
#     ax.set_title(f'Predicción con ARIMA No Seasonal para {empresa}')
#     ax.legend()
#     plt.show()


#     # STL + Media
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.plot(predict.index, stl, color='blue', label='Predicción')
#     ax.plot(predict.index, data.loc[predict.index, 'close'], color='red', label='Datos reales')
#     ax.set_title(f'Predicción con STL para {empresa}')
#     ax.legend()
#     plt.show()

#     # Forecasting Lineal
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.plot(predict.index, linear_pred + media, color='blue', label='Predicción')
#     ax.plot(predict.index, data.loc[predict.index, 'close'], color='red', label='Datos reales')
#     ax.set_title(f'Predicción con Forecasting Lineal para {empresa}')
#     ax.legend()
#     plt.show()
    
    
    

# prediccion 2025

import matplotlib.pyplot as plt
import pandas as pd

def plot_results(data, train, test, predict, arima_seasonal, linear, empresa, tesla_data,toyota_data, toyota_arima_seasonal, toyota_linear):
    # ARIMA Seasonal
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(predict.index[predict.index.year == 2025], arima_seasonal[predict.index.year == 2025], color='blue', label=f'{empresa} ARIMA Seasonal 2025')
    ax.plot(predict.index[predict.index.year == 2024], data.loc[predict.index[predict.index.year == 2024], 'close'], color='red', label='Datos reales 2024')
    ax.set_title(f'Predicción con ARIMA Seasonal para {empresa} (2025)')
    ax.legend()
    plt.show()

    # Forecasting Lineal
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(predict.index[predict.index.year == 2025], linear[predict.index.year == 2025], color='blue', label=f'{empresa} Forecasting Lineal 2025')
    ax.plot(predict.index[predict.index.year == 2024], data.loc[predict.index[predict.index.year == 2024], 'close'], color='red', label='Datos reales 2024')
    ax.set_title(f'Predicción con Forecasting Lineal para {empresa} (2025)')
    ax.legend()
    plt.show()

    # Gráfico comparativo ARIMA Seasonal
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(predict.index[predict.index.year == 2025], arima_seasonal[predict.index.year == 2025], label=f'{empresa} ARIMA Seasonal 2025')
    if empresa == 'Tesla':
        ax.plot(predict.index[predict.index.year == 2025], toyota_arima_seasonal[predict.index.year == 2025], label='Toyota ARIMA Seasonal 2025')
        ax.plot(predict.index[predict.index.year == 2024], tesla_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Tesla Datos reales 2024')
        ax.plot(predict.index[predict.index.year == 2024], toyota_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Toyota Datos reales 2024')
    else:
        ax.plot(predict.index[predict.index.year == 2025], tesla_arima_seasonal[predict.index.year == 2025], label='Tesla ARIMA Seasonal 2025')
        ax.plot(predict.index[predict.index.year == 2024], toyota_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Toyota Datos reales 2024')
        ax.plot(predict.index[predict.index.year == 2024], tesla_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Tesla Datos reales 2024')
    ax.set_title('Comparación de predicciones ARIMA Seasonal 2025')
    ax.legend()
    plt.show()

    # Gráfico comparativo Forecasting Lineal
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(predict.index[predict.index.year == 2025], linear[predict.index.year == 2025], label=f'{empresa} Forecasting Lineal 2025')
    if empresa == 'Tesla':
        ax.plot(predict.index[predict.index.year == 2025], toyota_linear[predict.index.year == 2025], label='Toyota Forecasting Lineal 2025')
        ax.plot(predict.index[predict.index.year == 2024], tesla_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Tesla Datos reales 2024')
        ax.plot(predict.index[predict.index.year == 2024], toyota_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Toyota Datos reales 2024')
    else:
        ax.plot(predict.index[predict.index.year == 2025], tesla_linear[predict.index.year == 2025], label='Tesla Forecasting Lineal 2025')
        ax.plot(predict.index[predict.index.year == 2024], toyota_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Toyota Datos reales 2024')
        ax.plot(predict.index[predict.index.year == 2024], tesla_data.loc[predict.index[predict.index.year == 2024], 'close'], label='Tesla Datos reales 2024')
    ax.set_title('Comparación de predicciones Forecasting Lineal 2025')
    ax.legend()
    plt.show()