#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:56:50 2026

@author: owner
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv('example_data_1_PHYS_433_533 (2).csv')
print(df)

frequency = df['f_res']
power_dBm = df['max_power_dBm']
plt.title("Power vs. Frequency")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dBm)")
#plt.scatter(frequency, power_dBm)
#plt.show()

power_mW = 10 **(np.array(power_dBm)/ 10)
print(power_mW[:5])

plt.title("Power vs. Frequency")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dBm)")
#plt.scatter(frequency, power_mW)
#plt.show()

mask = frequency > 4000
freq_filtered = frequency[mask]
power_mW_filtered = power_mW[mask]

plt.title("Power vs. Frequency")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dBm)")
#plt.scatter(freq_filtered, power_mW_filtered)
#plt.show()

def linear_fit(x, m, b):
    return m * x + b

popt, pcov = curve_fit(linear_fit, freq_filtered, power_mW_filtered, p0=[-1, 4e-5])
print(popt)
print(pcov)

plt.title("Power vs. Frequency")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dBm)")
plt.scatter(freq_filtered, power_mW_filtered)
plt.plot(freq_filtered, linear_fit(freq_filtered, popt[0], popt[1]), color='red')
plt.show()
#plt.show()