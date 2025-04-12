import pandas as pd
import numpy as np

def calculate_dcf(fcf,wacc,terminal_growth):
    terminal_value = (fcf[-1] * (1+terminal_growth))/(wacc-terminal_growth)
    present_value = [fcf[i] /(1+wacc) ** (i + 1) for i in range(len(fcf))]


    return total_pv

#load data from blob storage

df = spark.read.format("json").load("wasbs://financial-data@<dataStoreAccount>.blob.core.windows.net/AAPL_cashflow.json")
fcf = df.select("FreeCashFlow").rdd.flatMap(lambda x: x).collect()
intrinsic_value = calculate_dcf(fcf,0.10,0.03)