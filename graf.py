# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:59:56 2024

@author: Juan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
from scipy import stats as st

x=np.array([10,20,30,40,50,60,70,80,90])#Corriente I micro A
y=np.array([0.98,1.98,2.98,3.97,4.95,5.95,6.93,7.93,8.91])#voltaje V mili V

dy=0.01*np.zeros(len(y))


lin_reg = st.linregress(x,y)
f= lambda x: lin_reg.slope*x+lin_reg.intercept

x_p=np.linspace(min(x),max(x),500)

fig, ax= plt.subplots(2,1, figsize=(6,8))

ax[0].set_title("Gráfica de votlaje contra corriente")
ax[0].set_xlabel("I ($\mu$A)")
ax[0].set_ylabel("V (mV)")
ax[0].grid()
ax[0].scatter(x,y, c="tomato")
ax[0].plot(x_p,f(x_p),c="k",linestyle="--",label="y = ("+str(round(lin_reg.slope,5))+"$\pm$ "
         +str(round(lin_reg.stderr,5))+")x + ("+str(round(lin_reg.intercept,3))+"$\pm$"+
         str(round(lin_reg.intercept_stderr,3)) +")")
ax[0].legend(loc="upper left")
ax[0].errorbar(x, y, yerr= dy, ecolor="k",capsize=2,linestyle="")

print(lin_reg.slope)
print("Error m de H vs I:",lin_reg.stderr)
print(lin_reg.intercept)
print("Error b de H vs I:",lin_reg.intercept_stderr)

res=(y-f(x))

aCu=np.sqrt(1/(len(y)-2)*np.sum((y-lin_reg.slope*x-lin_reg.intercept)**2))
D=len(y)*np.sum(x**2)-(np.sum(x))**2
print(aCu)
print(aCu*np.sqrt(len(y)/D))

ax[1].scatter(x,res,c="red")
ax[1].grid()
ax[1].set_xlabel("I ($\mu$A)")
ax[1].set_ylabel("Residuales $R_i$ ")
ax[1].set_title("Gráfica de residuales")
ax[1].legend()
plt.tight_layout()

plt.show()
print(np.average(res))

