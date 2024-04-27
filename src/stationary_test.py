import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss


tesla_data = pd.read_csv('dataset/acciones_tesla_normalizados.csv')
toyota_data = pd.read_csv('dataset/acciones_toyota_normalizados.csv')

tesla_data_nasdaq = pd.read_csv('dataset/acciones_nasdaq_tesla_normalizados.csv')
toyota_data_nasdaq = pd.read_csv('dataset/acciones_nasdaq_toyota_normalizados.csv')



def adf_test(timeseries):
    print("Results of Dickey-Fuller Test:")
    dftest = adfuller(timeseries, autolag="AIC")
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
    kpsstest = kpss(timeseries, regression="c", nlags="auto")
    kpss_output = pd.Series(
        kpsstest[0:3], index=["Test Statistic", "p-value", "Lags Used"]
    )
    for key, value in kpsstest[3].items():
        kpss_output["Critical Value (%s)" % key] = value
    print(kpss_output)

    
    
    
    # Aplicar transformación logarítmica
tesla_data_nasdaq_log = np.log(tesla_data_nasdaq["close"])
toyota_data_nasdaq_log = np.log(toyota_data_nasdaq["close"])

# Aplicar diferenciación
tesla_data_nasdaq_diff = tesla_data_nasdaq_log.diff().dropna()
toyota_data_nasdaq_diff = toyota_data_nasdaq_log.diff().dropna()



adf_test(tesla_data_nasdaq_diff)
kpss_test(tesla_data_nasdaq_diff)

adf_test(toyota_data_nasdaq_diff)
kpss_test(toyota_data_nasdaq_diff)
    
    
    