"""
Collection of test ad data processing scripts
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Poisson import PoiFit as pf


def pe_getdata(file: str):
    """
    load and format test data
    :return:
    """

    Weather = pd.read_excel(file,'Weather',header=0,dtype=np.double)
    Natural = pd.read_excel(file,'Natural',header=0,dtype=np.double)

    a = list(Natural['Datum'])
    b = list(Weather['Datum'])

    df = Weather.copy()
    df['Events'] = [a.count(i) for i in b]

    start = '2000.01.01'
    n = len(df)
    days = pd.date_range(start=start,periods=n,freq='D')
    df['Datum'] = days
    df = df.set_index('Datum')

    return df


def pe_analyze():

    file = "/home/lovas/Documents/Kutatás/SOTE4/2016/TKlara_PE/szamitasok/adatok.xls"
    df = pe_getdata(file)

    # fit Poisson process intensity
    tool = pf.PoiFit(df['Events'])
    l = tool.fit()

    plt.figure()
    l1 = 1-np.exp(-l)
    l1.plot()
    df['Tavg'].plot(secondary_y=True, style='r')
    print(df.head(n=5))

    #  plt.figure()
    #  df['P'].plot()
    plt.show()


def main():
    pe_analyze()





if __name__ == '__main__':
    main()