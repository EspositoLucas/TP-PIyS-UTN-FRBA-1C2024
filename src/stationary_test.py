import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss


tesla_data = pd.read_csv('dataset/acciones_tesla_normalizados.csv')
toyota_data = pd.read_csv('dataset/acciones_toyota_normalizados.csv')

tesla_data_nasdaq = pd.read_csv('dataset/acciones_nasdaq_tesla_normalizados.csv')
toyota_data_nasdaq = pd.read_csv('dataset/acciones_nasdaq_toyota_normalizados.csv')
tesla_data_nasdaq = tesla_data_nasdaq.iloc[::-1]
toyota_data_nasdaq = toyota_data_nasdaq.iloc[::-1]
print(tesla_data_nasdaq.head())


def adf_test(timeseries):
    print("Results of Dickey-Fuller Test:")
    dftest = adfuller(timeseries, autolag="AIC", regression="c")
    dfoutput = pd.Series(
        dftest[0:4],
        index=[
            "Test Statistic",
            "p-value",
            "#Lags Used",
            "Number of Observations Used",
        ],
    )
    for key, value in dftest[4].items():
        dfoutput["Critical Value (%s)" % key] = value
    print(dfoutput)

def kpss_test(timeseries):
    print("Results of KPSS Test:")
    kpsstest = kpss(timeseries, regression="ct", nlags="auto")
    kpss_output = pd.Series(
        kpsstest[0:3], index=["Test Statistic", "p-value", "Lags Used"]
    )
    for key, value in kpsstest[3].items():
        kpss_output["Critical Value (%s)" % key] = value
    print(kpss_output)

    
    
    

"""
# Aplicar transformación logarítmica
tesla_data_nasdaq_log = np.log(tesla_data_nasdaq["close"])
toyota_data_nasdaq_log = np.log(toyota_data_nasdaq["close"])
"""
"""
# Graficos de los datos originales
plt.plot(tesla_data_nasdaq["date"], tesla_data_nasdaq["close"], label="Tesla Serie Original")
plt.show()

plt.plot(toyota_data_nasdaq["date"],toyota_data_nasdaq["close"], label="Toyota Serie Original")
plt.show()

# Aplicar diferenciación
tesla_data_nasdaq_diff = tesla_data_nasdaq["close"].diff().dropna()
toyota_data_nasdaq_diff = tesla_data_nasdaq["close"].diff().dropna()

# Graficos de los datos diferenciados
plt.plot(tesla_data_nasdaq["date"],tesla_data_nasdaq_diff, label="Tesla Serie con Diff")
plt.show()

plt.plot(toyota_data_nasdaq["date"],toyota_data_nasdaq_diff, label="Toyota Serie con Diff")
plt.show()

adf_test(tesla_data_nasdaq_diff)
kpss_test(tesla_data_nasdaq_diff)
adf_test(toyota_data_nasdaq_diff)
kpss_test(toyota_data_nasdaq_diff)
"""
"""
TRANSFORMACION 

def remove_trend(timeseries): # le resta la recta de regresión 
    slope, intercept = np.polyfit(range(len(timeseries)), timeseries, 1)
    detrended = timeseries - (slope * np.arange(len(timeseries)) + intercept)
    return detrended

adf_test(remove_trend(tesla_data_nasdaq["close"])) # p-value = 0.151296
kpss_test(remove_trend(tesla_data_nasdaq["close"])) # p-value = 0.01

adf_test(remove_trend(toyota_data_nasdaq["close"])) # p-value = 0.151296
kpss_test(remove_trend(toyota_data_nasdaq["close"])) # p-value = 0.01
"""

"""
# Aplicar diferenciación
tesla_data_nasdaq_diff = tesla_data_nasdaq["close"].diff().dropna()
toyota_data_nasdaq_diff = toyota_data_nasdaq["close"].diff().dropna()

adf_test(tesla_data_nasdaq_diff)
kpss_test(tesla_data_nasdaq_diff)

adf_test(toyota_data_nasdaq_diff)
kpss_test(toyota_data_nasdaq_diff)  
""" 




# from statsmodels.tsa.holtwinters import ExponentialSmoothing

# # Aplicar suavizado exponencial
# tesla_data_2_smooth = ExponentialSmoothing(tesla_data_nasdaq["close"]).fit().fittedvalues
# toyota_data_2_smooth = ExponentialSmoothing(toyota_data_nasdaq["close"]).fit().fittedvalues

# adf_test(tesla_data_2_smooth)
# kpss_test(tesla_data_2_smooth)


# adf_test(toyota_data_2_smooth)
# kpss_test(toyota_data_2_smooth)


"""
# from scipy.stats import boxcox

# # Aplicar la transformación Box-Cox
# tesla_data_2_boxcox = boxcox(tesla_data_nasdaq["close"] + 1)[0]
# toyota_data_2_boxcox = boxcox(toyota_data_nasdaq["close"] + 1)[0]


# adf_test(tesla_data_2_boxcox)
# kpss_test(tesla_data_2_boxcox)


# adf_test(toyota_data_2_boxcox)
# kpss_test(toyota_data_2_boxcox)
"""

# TRANSFORMACION DE RAIZ CUADRADA
import numpy as np

# Aplicar la transformación por raíz cuadrada
tesla_data_2_sqrt = tesla_data_nasdaq["close"] ** (5)
toyota_data_2_sqrt = toyota_data_nasdaq["close"] ** (5)
print(tesla_data_2_sqrt)
print(toyota_data_2_sqrt)


plt.plot(tesla_data_2_sqrt)
plt.show()

plt.plot(toyota_data_2_sqrt)
plt.show()

adf_test(tesla_data_2_sqrt)
kpss_test(tesla_data_2_sqrt)


adf_test(toyota_data_2_sqrt)
kpss_test(toyota_data_2_sqrt)
