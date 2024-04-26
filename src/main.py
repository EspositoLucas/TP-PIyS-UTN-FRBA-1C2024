import pandas as pd
from data_processing import load_data, split_data
from models import arima_seasonal, arima_non_seasonal, stl_forecast, linear_forecast
from visualization import plot_results

def main():
    # Cargar y preprocesar los datos
    tesla_data, toyota_data = load_data()

    # Dividir los datos en conjuntos de entrenamiento y prueba
    train_end = pd.Timestamp('2021-12-31')
    test_start = pd.Timestamp('2022-01-01')
    test_end = pd.Timestamp('2023-12-31')
    predict_start = pd.Timestamp('2024-01-01')

    tesla_train, tesla_test, tesla_predict = split_data(tesla_data, train_end, test_start, test_end, predict_start)
    toyota_train, toyota_test, toyota_predict = split_data(toyota_data, train_end, test_start, test_end, predict_start)

    # Modelado
    tesla_arima_seasonal = arima_seasonal(tesla_train, tesla_test, tesla_predict)
    toyota_arima_seasonal = arima_seasonal(toyota_train, toyota_test, toyota_predict)

    tesla_arima_non_seasonal = arima_non_seasonal(tesla_train, tesla_test, tesla_predict)
    toyota_arima_non_seasonal = arima_non_seasonal(toyota_train, toyota_test, toyota_predict)

    tesla_stl = stl_forecast(tesla_train, tesla_test, tesla_predict)
    toyota_stl = stl_forecast(toyota_train, toyota_test, toyota_predict)

    tesla_linear = linear_forecast(tesla_train, tesla_predict)
    toyota_linear = linear_forecast(toyota_train, toyota_predict)

    # Visualización
    plot_results(tesla_data, tesla_train, tesla_test, tesla_predict, tesla_arima_seasonal, tesla_arima_non_seasonal, tesla_stl, tesla_linear, "Tesla")
    plot_results(toyota_data, toyota_train, toyota_test, toyota_predict, toyota_arima_seasonal, toyota_arima_non_seasonal, toyota_stl, toyota_linear, "Toyota")


if __name__ == "__main__":
    main()