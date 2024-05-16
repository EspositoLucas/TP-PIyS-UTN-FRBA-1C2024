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
# # def stl_forecast(train, test, predict):
# #     stl = seasonal_decompose(train, period=12)
# #     trend = stl.trend
# #     seasonal = stl.seasonal
# #     residual = stl.resid
# #     forecast = trend.iloc[-1] + seasonal.iloc[-12:].sum() + residual.mean()
# #     return pd.Series([forecast] * len(predict), index=predict.index)


# # Holt Winters


# def holt_winters_forecast(train, test, predict):
#     model = ExponentialSmoothing(train, trend='add', seasonal='add', seasonal_periods=12)
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=len(predict))
#     return forecast


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