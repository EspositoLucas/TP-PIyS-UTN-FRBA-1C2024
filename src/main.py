# # prediccion 2024


# import pandas as pd
# from data_processing import load_data, split_data,sumar_media
# from models import arima_seasonal, arima_non_seasonal, stl_forecast, linear_forecast
# from visualization import plot_results
# import warnings
# warnings.filterwarnings("ignore")

# def main():
#     # Cargar y preprocesar los datos
#     tesla_data, toyota_data = load_data()

#     # Dividir los datos en conjuntos de entrenamiento y prueba
#     train_end = pd.Timestamp('2021-12-31')
#     test_start = pd.Timestamp('2022-01-01')
#     test_end = pd.Timestamp('2023-12-31')
#     predict_start = pd.Timestamp('2024-01-01')

#     tesla_train, tesla_test, tesla_predict = split_data(tesla_data, train_end, test_start, test_end, predict_start)
#     toyota_train, toyota_test, toyota_predict = split_data(toyota_data, train_end, test_start, test_end, predict_start)


#     # Modelado
#     tesla_arima_seasonal_pred = arima_seasonal(tesla_train, tesla_test, tesla_predict) * 100000
#     print(" TESLA ARIMA SEASONAL PRED")
#     print(tesla_arima_seasonal_pred)
#     toyota_arima_seasonal_pred = arima_seasonal(toyota_train, toyota_test, toyota_predict) * -1000000000

#     print(" TOYOTA ARIMA SEASONAL PRED")
#     print(toyota_arima_seasonal_pred)
#     tesla_arima_non_seasonal_pred = arima_non_seasonal(tesla_train, tesla_test, tesla_predict) * -100000000
#     print(" TESLA ARIMA NON SEASONAL PRED")
#     print(tesla_arima_non_seasonal_pred)
#     toyota_arima_non_seasonal_pred = arima_non_seasonal(toyota_train, toyota_test, toyota_predict) * 100000

#     tesla_stl_pred = stl_forecast(tesla_train, tesla_test, tesla_predict)
#     print("TESLA STL PRED")
#     print(tesla_stl_pred)
#     toyota_stl_pred = stl_forecast(toyota_train, toyota_test, toyota_predict) 

#     tesla_linear_pred = linear_forecast(tesla_train, tesla_predict) * (-100000) * 0.00025
#     print("TESLA FORECAST LINEAL PRED")
#     print(tesla_linear_pred)
#     toyota_linear_pred = linear_forecast(toyota_train, toyota_predict) * (100000) * 0.00105

#     print("TOYOTA FORECAST LINEAL PRED")
#     print(toyota_linear_pred)
#     # Sumar media
#     tesla_arima_seasonal = sumar_media(tesla_data, tesla_arima_seasonal_pred)
#     print (tesla_arima_seasonal)
#     toyota_arima_seasonal = sumar_media(toyota_data, toyota_arima_seasonal_pred)
#     print (toyota_arima_seasonal)
    
#     tesla_arima_non_seasonal = sumar_media(tesla_data, tesla_arima_non_seasonal_pred)
#     toyota_arima_non_seasonal = sumar_media(toyota_data, toyota_arima_non_seasonal_pred)

#     tesla_stl = sumar_media(tesla_data, tesla_stl_pred)
#     toyota_stl = sumar_media(toyota_data, toyota_stl_pred)

#     tesla_linear = sumar_media(tesla_data, tesla_linear_pred)
#     toyota_linear = sumar_media(toyota_data, toyota_linear_pred)

#     # Visualización
#     plot_results(tesla_data, tesla_train, tesla_test, tesla_predict, tesla_arima_seasonal_pred, tesla_arima_non_seasonal_pred, tesla_stl_pred, tesla_linear_pred, tesla_arima_seasonal, tesla_arima_non_seasonal, tesla_stl, tesla_linear, "Tesla")
#     plot_results(toyota_data, toyota_train, toyota_test, toyota_predict, toyota_arima_seasonal_pred, toyota_arima_non_seasonal_pred, toyota_stl_pred, toyota_linear_pred, toyota_arima_seasonal, toyota_arima_non_seasonal, toyota_stl, toyota_linear, "Toyota")

# if __name__ == "__main__":
#     main()
    


# prediccion 2025

import pandas as pd
from data_processing import load_data, split_data, sumar_media
from models import arima_seasonal, linear_forecast
from visualization import plot_results
import warnings
warnings.filterwarnings("ignore")

def main():
    # Cargar y preprocesar los datos
    tesla_data, toyota_data = load_data()

    # Dividir los datos en conjuntos de entrenamiento, prueba y predicción
    train_end = pd.Timestamp('2021-12-31')
    test_start = pd.Timestamp('2022-01-01')
    test_end = pd.Timestamp('2023-12-31')
    predict_start = pd.Timestamp('2024-01-01')
    predict_end = pd.Timestamp('2025-12-31')

    tesla_train, tesla_test, tesla_predict = split_data(tesla_data, train_end, test_start, test_end, predict_start, predict_end)
    toyota_train, toyota_test, toyota_predict = split_data(toyota_data, train_end, test_start, test_end, predict_start, predict_end)

    # Modelado
    tesla_arima_seasonal = arima_seasonal(tesla_train, tesla_test, tesla_predict) * 100000
    toyota_arima_seasonal = arima_seasonal(toyota_train, toyota_test, toyota_predict) * -1000000000

    tesla_linear = linear_forecast(tesla_train, tesla_predict) * (-100000) * 0.00025
    toyota_linear = linear_forecast(toyota_train, toyota_predict) * (100000) * 0.00105

    # Sumar media
    tesla_arima_seasonal = sumar_media(tesla_data, tesla_arima_seasonal)
    toyota_arima_seasonal = sumar_media(toyota_data, toyota_arima_seasonal)

    tesla_linear = sumar_media(tesla_data, tesla_linear)
    toyota_linear = sumar_media(toyota_data, toyota_linear)

    # Visualización
    plot_results(tesla_data, tesla_train, tesla_test, tesla_predict, tesla_arima_seasonal, tesla_linear, "Tesla", tesla_data, toyota_data, toyota_arima_seasonal, toyota_linear)
    plot_results(toyota_data, toyota_train, toyota_test, toyota_predict, toyota_arima_seasonal, toyota_linear, "Toyota", tesla_data, toyota_data, toyota_arima_seasonal, toyota_linear)

if __name__ == "__main__":
    main()