import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
import matplotlib.pyplot as plt

# Cargar los datasets
tesla_data_2 = pd.read_csv('dataset/acciones_nasdaq_tesla_normalizados.csv')
toyota_data_2 = pd.read_csv('dataset/acciones_nasdaq_toyota_normalizados.csv')

def adf_test(timeseries):
    print("Results of Dickey-Fuller Test:")
    dftest = adfuller(timeseries.dropna(), autolag="AIC")
    dfoutput = pd.Series(dftest[0:4], index=["Test Statistic", "p-value", "#Lags Used", "Number of Observations Used"])
    for key, value in dftest[4].items():
        dfoutput["Critical Value (%s)" % key] = value
    print(dfoutput)

def kpss_test(timeseries):
    print("Results of KPSS Test:")
    kpsstest = kpss(timeseries.dropna(), regression="c", nlags="auto")
    kpss_output = pd.Series(kpsstest[0:3], index=["Test Statistic", "p-value", "Lags Used"])
    for key, value in kpsstest[3].items():
        kpss_output["Critical Value (%s)" % key] = value
    print(kpss_output)

# Aplicar filtro de media móvil con ventana de tamaño 10
window_size = 10
tesla_data_2_rolling_mean = tesla_data_2["close"].rolling(window=window_size).mean()
toyota_data_2_rolling_mean = toyota_data_2["close"].rolling(window=window_size).mean()

tesla_data_2_detrended = tesla_data_2["close"].dropna() - tesla_data_2_rolling_mean
toyota_data_2_detrended = toyota_data_2["close"].dropna() - toyota_data_2_rolling_mean

print(f"\nResultados con ventana de tamaño {window_size}:")
adf_test(tesla_data_2_detrended)
kpss_test(tesla_data_2_detrended)
adf_test(toyota_data_2_detrended)
kpss_test(toyota_data_2_detrended)

# Graficar la señal original y la señal estacionaria
plt.figure(figsize=(12, 6))
plt.plot(tesla_data_2["close"].dropna(), label='Señal original')
plt.plot(tesla_data_2_detrended, label='Señal estacionaria')
plt.title('Señal original y estacionaria de acciones Tesla')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()

# # Mostrar las columnas de fecha y precio de cierre
# print("\nColumnas de fecha y precio de cierre para Tesla:")
# print(tesla_data_2[['date','close']].head())

# print("\nColumnas de fecha y precio de cierre para Toyota:")
# print(toyota_data_2[['date','close']].head())


# Crear DataFrames con fechas y precios de cierre para la serie estacionaria
tesla_data_2_detrended_df = tesla_data_2[['date', 'close']].dropna().iloc[window_size//2:-window_size//2]
tesla_data_2_detrended_df['close_detrended'] = tesla_data_2_detrended

toyota_data_2_detrended_df = toyota_data_2[['date', 'close']].dropna().iloc[window_size//2:-window_size//2]
toyota_data_2_detrended_df['close_detrended'] = toyota_data_2_detrended

print("\nColumnas de fecha y precio de cierre para la serie estacionaria de Tesla:")
print(tesla_data_2_detrended_df.head())

print("\nColumnas de fecha y precio de cierre para la serie estacionaria de Toyota:")
print(toyota_data_2_detrended_df.head())

plt.show()
