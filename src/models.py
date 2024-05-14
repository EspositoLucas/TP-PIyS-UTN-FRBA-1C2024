# prediccion 2024

# import pandas as pd
# from statsmodels.tsa.arima.model import ARIMA
# from statsmodels.tsa.holtwinters import ExponentialSmoothing
# from statsmodels.tsa.seasonal import seasonal_decompose
# from pmdarima import auto_arima

# # ARIMA Seasonal
# def arima_seasonal(train, test, predict):
#     model = auto_arima(train, seasonal=True, m=12, start_p=0, start_q=0, max_p=1, max_q=1, start_P=0, start_Q=0, max_P=1, max_Q=1, trace=True)
#     forecast = model.predict(n_periods=len(test) + len(predict))[len(test):]
#     return forecast

# # ARIMA No Seasonal
# def arima_non_seasonal(train, test, predict):
#     model = auto_arima(train, seasonal=False, start_p=1, start_q=1, max_p=1, max_q=1, trace=True)
#     forecast = model.predict(n_periods=len(test) + len(predict))[len(test):]
#     return forecast

# # STL
# def stl_forecast(train, test, predict):
#     stl = seasonal_decompose(train, period=12)
#     trend = stl.trend
#     seasonal = stl.seasonal
#     residual = stl.resid
#     forecast = trend.iloc[-1] + seasonal.iloc[-12:].sum() + residual.mean()
#     return pd.Series([forecast] * len(predict), index=predict.index)

# # def stl_forecast(train, test, predict):
# #     stl = seasonal_decompose(train, period=12)
# #     trend = stl.trend
# #     seasonal = stl.seasonal
# #     residual = stl.resid

# #     # Crear un nuevo DataFrame con el índice de fechas completo
# #     start_date = predict.index.min()
# #     end_date = predict.index.max()
# #     forecast_dates = pd.date_range(start=start_date, end=end_date, freq='D')
# #     forecast_df = pd.DataFrame(index=forecast_dates)

# #     # Llenar los valores faltantes con NaN
# #     forecast_df['values'] = pd.Series(forecast_df.index).map(predict).fillna(predict.mean())

# #     # Calcular la tendencia y la estacionalidad para el período de predicción
# #     forecast_trend = pd.Series(trend.iloc[-1], index=forecast_dates)  # Última tendencia replicada
# #     forecast_seasonal = seasonal.iloc[-12:].reset_index(drop=True)  # Últimos 12 meses de estacionalidad

# #     # Calcular la predicción
# #     forecast = forecast_trend.reindex(forecast_dates, method='ffill')
# #     forecast = forecast.add(forecast_seasonal.reindex(forecast_dates, method='ffill'), fill_value=0)
# #     forecast = forecast.add(residual.mean(), fill_value=0)

# #     # Filtrar la predicción para los índices solicitados
# #     forecast = forecast.reindex(predict.index)

# #     return forecast


# # Forecasting Lineal
# def linear_forecast(train, predict):
#     model = ExponentialSmoothing(train, trend='add', seasonal='add', seasonal_periods=12)
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=len(predict))
#     return forecast



# prediccion 2025


import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from pmdarima import auto_arima

# ARIMA Seasonal
def arima_seasonal(train, test, predict):
    model = auto_arima(train, seasonal=True, m=12, start_p=0, start_q=0, max_p=1, max_q=1, start_P=0, start_Q=0, max_P=1, max_Q=1, trace=True)
    forecast = model.predict(n_periods=len(test) + len(predict))[len(test):]
    return forecast

# Forecasting Lineal
def linear_forecast(train, predict):
    model = ExponentialSmoothing(train, trend='add', seasonal='add', seasonal_periods=12)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=len(predict))
    return forecast