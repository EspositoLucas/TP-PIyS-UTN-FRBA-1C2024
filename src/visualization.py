import matplotlib.pyplot as plt

def plot_results(data, train, test, predict, arima_seasonal, arima_non_seasonal, stl, linear, empresa):
    fig, ax = plt.subplots(2, 2, figsize=(16, 10))

    ax[0, 0].plot(data, label='Datos reales')
    ax[0, 0].plot(train.index, train['close'], label='Entrenamiento')
    ax[0, 0].plot(test.index, test['close'], label='Prueba')
    ax[0, 0].plot(predict.index, arima_seasonal, label='ARIMA Seasonal')
    ax[0, 0].plot(predict.index, arima_non_seasonal, label='ARIMA No Seasonal')
    ax[0, 0].plot(predict.index, stl, label='STL')
    ax[0, 0].plot(predict.index, linear, label='Forecasting Lineal')
    ax[0, 0].set_title(f'Predicción de precios de acciones de {empresa}')
    ax[0, 0].legend()

    ax[1, 0].plot(test.index, test['close'], label='Datos reales')
    ax[1, 0].plot(test.index, arima_seasonal[:len(test)], label='ARIMA Seasonal')
    ax[1, 0].plot(test.index, arima_non_seasonal[:len(test)], label='ARIMA No Seasonal')
    ax[1, 0].plot(test.index, stl[:len(test)], label='STL')
    ax[1, 0].plot(test.index, linear[:len(test)], label='Forecasting Lineal')
    ax[1, 0].set_title(f'Comparación de predicciones para {empresa} (2022-2023)')
    ax[1, 0].legend()

    plt.tight_layout()
    plt.show()