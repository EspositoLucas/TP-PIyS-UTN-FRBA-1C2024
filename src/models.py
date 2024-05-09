# import pandas as pd
# from statsmodels.tsa.arima.model import ARIMA
# from statsmodels.tsa.holtwinters import SimpleExpSmoothing
# from statsmodels.tsa.seasonal import seasonal_decompose

# # ARIMA Seasonal
# def arima_seasonal(train, test, predict):
#     model = ARIMA(train['close'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=len(test) + len(predict))[len(test):]
#     return forecast

# # ARIMA No Seasonal
# def arima_non_seasonal(train, test, predict):
#     model = ARIMA(train['close'], order=(1, 1, 1))
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=len(test) + len(predict))[len(test):]
#     return forecast

# # STL
# def stl_forecast(train, test, predict):
#     stl = seasonal_decompose(train['close'], period=12)
#     trend = stl.trend
#     seasonal = stl.seasonal
#     residual = stl.resid
#     forecast = trend.iloc[-1] + seasonal.iloc[-12:].sum() + residual.mean()
#     return pd.Series([forecast] * len(predict), index=predict.index)


# # Forecasting Lineal
# def linear_forecast(train, predict):
#     model = SimpleExpSmoothing(train['close'])
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=len(predict))
#     return forecast


import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose

# ARIMA Seasonal
def arima_seasonal(train, test, predict):
    model = ARIMA(train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=len(test) + len(predict))[len(test):]
    return forecast

# ARIMA No Seasonal
def arima_non_seasonal(train, test, predict):
    model = ARIMA(train, order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=len(test) + len(predict))[len(test):]
    return forecast

# STL
def stl_forecast(train, test, predict):
    stl = seasonal_decompose(train, period=12)
    trend = stl.trend
    seasonal = stl.seasonal
    residual = stl.resid
    forecast = trend.iloc[-1] + seasonal.iloc[-12:].sum() + residual.mean()
    return pd.Series([forecast] * len(predict), index=predict.index)

# Forecasting Lineal
def linear_forecast(train, predict):
    model = SimpleExpSmoothing(train)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=len(predict))
    return forecast