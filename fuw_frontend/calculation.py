from math import exp
import numpy as np
import logging
from scipy.optimize import curve_fit
from .Model import Parameter, Metering, Result

class SpectrCalculation:
    def __init__(self) -> None:
        self.c = 0
        self.iter =0
        self.fullModulation = 0.32
        self.narrowModulation = 0.08
        self.fullCoefficients = np.array([2,0,6,0.7,0.3,0]) # Coefficients in full by default
        self.narrowCoefficients = np.array([1.5, 0.3, 1, 0.5,0.3,0.6,0]) # Coefficients in narrow by default
        pass 
        
    def __func1(self, x, a, b, c1, d, q, k):
        return a*(exp(-2*(x-b+self.fullModulation)**2/c1**2)-exp(-2*(x-b-self.fullModulation)**2/c1**2)) + d*q**2*(1/(q**2 + (x-b+self.fullModulation)**2) - 1/(q**2+(x-b-self.fullModulation)**2)) - k

    def __func2(self, x, a, b, d, q, w, v, k):
        logging.info(f"c = {self.c}")
        logging.info(f"interation =  {self.iter}")
        self.iter+=1
        return a*(exp(-2*(x-b+self.narrowCoefficients)**2/self.c**2)-exp(-2*(x-b-self.narrowCoefficients)**2/self.c**2)) + d*(q**2)*(1/(q**2 + (x-b+self.narrowCoefficients)**2) - 1/(q**2+(x-b-self.narrowCoefficients)**2)) \
            +w*v*(1/(v**2 + (x-b+self.narrowCoefficients)**2) - 1/(v**2+(x-b-self.narrowCoefficients)**2))- k

    def culculate(self, parameter:Parameter, metering:Metering)->Metering:
        self.fullModulation = parameter.fullModulation
        self.narrowModulation = parameter.narrowModulation
        x = metering.full[:,0]
        y = metering.full[:,1]
        popt, pcov = curve_fit(self.__func1, x, y, self.fullCoefficients)
        self.c = popt[2]
        a_min = 0.9*popt[0]
        min = 0.5*popt[3]
        x1 = metering.narrow[:,0]
        y1 = metering.narrow[:,1]
        popt1, pcov1 = curve_fit(self.__func2, x1, y1, self.narrowCoefficients, bounds=((a_min, -np.inf, min, -np.inf, min, -np.inf, -np.inf),(np.inf, np.inf, np.inf, 2, np.inf, 2, np.inf)))
        result = Result(full_a = popt[0],full_b = popt[1],full_c = popt[2], full_d = popt[3],full_q = popt[4],full_k = popt[5],narrow_a = popt1[0],
                       narrow_b = popt1[1],narrow_d = popt1[2],narrow_q = popt1[3],narrow_w = popt1[4],narrow_v = popt1[5],narrow_k = popt1[6])
        metering.result = result
        return metering
 