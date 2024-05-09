import matplotlib.pyplot as plt
import pandas as pd

def plot_results(data, train, test, predict, arima_seasonal, arima_non_seasonal, stl, linear, empresa):
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(12, 16), sharex=True)

    # Datos reales
    axes[0].plot(data.index, data['close'], label='Datos reales')
    axes[0].plot(train.index, train, label='Entrenamiento')
    axes[0].plot(test.index, test, label='Prueba')
    axes[0].set_title(f'Predicción de precios de acciones de {empresa}')
    axes[0].legend()

    # ARIMA Seasonal
    axes[1].plot(test.index, test, label='Datos reales')
    axes[1].plot(predict.index, arima_seasonal, label='ARIMA Seasonal')
    axes[1].set_title(f'Predicción con ARIMA Seasonal para {empresa}')
    axes[1].legend()

    # ARIMA No Seasonal
    axes[2].plot(test.index, test, label='Datos reales')
    axes[2].plot(predict.index, arima_non_seasonal, label='ARIMA No Seasonal')
    axes[2].set_title(f'Predicción con ARIMA No Seasonal para {empresa}')
    axes[2].legend()

    # STL
    axes[3].plot(test.index, test, label='Datos reales')
    axes[3].plot(predict.index, stl, label='STL')
    axes[3].set_title(f'Predicción con STL para {empresa}')
    axes[3].legend()

    # Forecasting Lineal
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(test.index, test, label='Datos reales')
    ax.plot(predict.index, linear, label='Forecasting Lineal')
    ax.set_title(f'Predicción con Forecasting Lineal para {empresa}')
    ax.legend()

    plt.tight_layout()
    plt.show()