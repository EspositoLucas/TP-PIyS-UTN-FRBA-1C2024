import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datasets
tesla_data_2 = pd.read_csv('dataset/acciones_nasdaq_tesla_normalizados.csv')
toyota_data_2 = pd.read_csv('dataset/acciones_nasdaq_toyota_normalizados.csv')

# Aplicar filtro de media móvil con ventana de tamaño 10
window_size = 10
tesla_data_2_rolling_mean = tesla_data_2["close"].rolling(window=window_size, center=True, min_periods=1).mean()
toyota_data_2_rolling_mean = toyota_data_2["close"].rolling(window=window_size, center=True, min_periods=1).mean()

tesla_data_2_detrended = tesla_data_2["close"] - tesla_data_2_rolling_mean
toyota_data_2_detrended = toyota_data_2["close"] - toyota_data_2_rolling_mean

# Graficar la señal original y la señal estacionaria
plt.figure(figsize=(12, 6))
plt.plot(tesla_data_2["close"], label='Señal original')
plt.plot(tesla_data_2_detrended, label='Señal estacionaria')
plt.title('Señal original y estacionaria de acciones Tesla')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()

# Crear DataFrames con fechas y precios de cierre para la serie estacionaria
tesla_data_2_detrended_df = tesla_data_2[['date', 'close']].copy()
tesla_data_2_detrended_df['close_detrended'] = tesla_data_2_detrended

toyota_data_2_detrended_df = toyota_data_2[['date', 'close']].copy()
toyota_data_2_detrended_df['close_detrended'] = toyota_data_2_detrended

print("\nColumnas de fecha y precio de cierre para la serie estacionaria de Tesla:")
print(tesla_data_2_detrended_df.head())

print("\nColumnas de fecha y precio de cierre para la serie estacionaria de Toyota:")
print(toyota_data_2_detrended_df.head())

plt.show()
