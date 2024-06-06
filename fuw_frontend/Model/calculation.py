from math import exp
import numpy as np

from pylab import * 
import logging
from scipy.optimize import curve_fit
from scipy import integrate
from . import Parameter, Metering, Result, Square

class SpectrCalculation():
    def __init__(self) -> None:
        self.c = 0
        self.iter =0
        self.fullModulation = 0.32
        self.narrowModulation = 0.08
        self.fullCoefficients = np.array([2,0,6,0.7,0.3,0]) # Coefficients in full by default
        self.narrowCoefficients = np.array([1.5, 0.3, 1, 0.5,0.3,0.6,0]) # Coefficients in narrow by default
        pass 
        
    def fullFunc(self, x, a, b, c1, d, q, k):
        return a*(exp(-2*(x-b+self.fullModulation)**2/c1**2)-exp(-2*(x-b-self.fullModulation)**2/c1**2)) \
            + d*q**2*(1/(q**2 + (x-b+self.fullModulation)**2) - 1/(q**2+(x-b-self.fullModulation)**2)) - k
    
    def __fullFunc(self, x, a, c1,d,q):
        return a*(exp(-2*(x)**2/c1**2))+d*q**2/(x**2 +q**2)

    def __fullFuncPart1(self, x, a, c1):
        return a*(exp(-2*(x**2/c1**2)))
    
    def __fullFuncPart2(self, x, d, q):
        return d*q**2/(x**2 +q**2)

    def narrowFunc(self, x, a, b, d, q, w, v, k):
        logging.debug(f"c = {self.c} a = {a}, b = {b}, d = {d}, q = {q}, w = {w}, v = {v}, k = {k}")
        logging.debug(f"interation =  {self.iter}")
        self.iter+=1
        return a*(exp(-2*(x-b+self.narrowModulation)**2/self.c**2)-exp(-2*(x-b-self.narrowModulation)**2/self.c**2)) \
            + d*(exp(-2*(x-b+self.narrowModulation)**2/q**2)-exp(-2*(x-b-self.narrowModulation)**2/q**2)) \
                +w*v*(1/(v**2 + (x-b+self.narrowModulation)**2) - 1/(v**2+(x-b-self.narrowModulation)**2))- k
    
    def __narrowFunc(self,x, a, d, q, w, v):
        return a*exp(-2*(x**2/self.c**2))+ d*(q**2/(x**2+q**2)) +w*(v**2/(x**2+v**2))

    def __narrowFuncPart1(self, x, a):
        return a*exp(-2*(x**2/self.c**2))
    
    def __narrowFuncPart2(self, x,   d, q):
        return d*(q**2/(x**2+q**2)) 
    
    def __narrowFuncPart3(self, x, w, v):
        return w*(v**2/(x**2+v**2))
        
        # y1 = a*(exp(-2*(x-b+self.narrowModulation)**2/self.c**2)-exp(-2*(x-b-self.narrowModulation)**2/self.c**2))
        # + d*(q**2)*(1/(q**2 + (x-b+self.narrowModulation)**2) - 1/(q**2+(x-b-self.narrowModulation)**2))
        # +w*v*(1/(v**2 + (x-b+self.narrowModulation)**2) - 1/(v**2+(x-b-self.narrowModulation)**2))- k
    

    def culculate(self, parameter:Parameter, metering:Metering)->Metering:
        logging.info(f"Start calulation {metering.description}")
        self.fullModulation = parameter.fullModulation
        self.narrowModulation = parameter.narrowModulation
        
        popt = self.__calculateFull(metering.full)
        logging.info(popt)
        self.c = popt[2]
        a_min = 0.9*popt[0]
        min = 0.5*popt[3]
        logging.info(f" c = {self.c} a_min = {a_min} min = {min}")
        popt1 = self.__calculateNarrow(metering.narrow,a_min,min)

        result = Result(full_a = popt[0],full_b = popt[1],full_c = popt[2], full_d = popt[3],full_q = popt[4],full_k = popt[5],narrow_a = popt1[0],
                       narrow_b = popt1[1],narrow_d = popt1[2],narrow_q = popt1[3],narrow_w = popt1[4],narrow_v = popt1[5],narrow_k = popt1[6])

        fs = self.__squareFull(metering.full, result)
        fs1 = self.__squareFullPart1(metering.full, result)
        fs2 = self.__squareFullPart2(metering.full, result)
        fd = self.__squareFullDef(metering.full)
        ns = self.__squareNarrow(metering.narrow, result)
        ns1 = self.__squareNarrowPart1(metering.narrow, result)
        ns2 = self.__squareNarrowPart2(metering.narrow, result)
        ns3 = self.__squareNarrowPart3(metering.narrow, result)
        nd = self.__squareNarrowDef(metering.narrow)
        # logging.info(f"s - {ns[0]}  s1+s2+s3 - {ns1[0]+ns2[0]+ns3[0]}")
        result.squarFull = Square(s=fs, s1=fs1, s2=fs2, default=fd)
        result.squarNarrow = Square(s=ns, s1=ns1, s2=ns2, s3=ns3, default=nd)
        metering.result = result
        return metering
    
    def __calculateFull(self, full)->tuple:
        x = full[:,0]
        y = full[:,1]
        popt, pcov = curve_fit(self.fullFunc, x, y, self.fullCoefficients)
        return popt
    
    def __calculateNarrow(self , narrow, a_min, min)->tuple:
        logging.info("Start calculation Narrow")
        if len(narrow) == 0:
            return (None,None,None,None,None,None,None)
        x = narrow[:,0]
        y = narrow[:,1]
        self.narrowCoefficients[0] = a_min
        self.narrowCoefficients[2] = min
        logging.info(self.narrowCoefficients)
        popt, pcov = curve_fit(self.narrowFunc, x, y, self.narrowCoefficients, bounds=((a_min, 0, 0, -np.inf, 0, -np.inf, -np.inf),
                                                                                        (np.inf, np.inf, np.inf, 2, np.inf, 2, np.inf)))
        return popt

    def __squareFullPart1(self, full, parameters:Result):
        X = full[:,0]
        x_min = np.min(X)
        x_max = np.max(X)
        s = integrate.quad(self.__fullFuncPart1,x_min,x_max,args=(parameters.full_a, parameters.full_c))
        logging.info(f"full part1 {s}")
        return s

    def __squareFullPart2(self, full, parameters:Result):
        X = full[:,0]
        x_min = np.min(X)
        x_max = np.max(X)
        s = integrate.quad(self.__fullFuncPart2,x_min,x_max,args=(parameters.full_d, parameters.full_q))
        logging.info(f"full part2 {s}")
        return s


    def __squareFull(self, full, parameters:Result):
        X = full[:,0]
        x_min = np.min(X)
        x_max = np.max(X)
        s = integrate.quad(self.__fullFunc,x_min,x_max,args=(parameters.full_a, parameters.full_c, parameters.full_d, parameters.full_q))
        logging.info(f"full {s}")
        return s
    
    def __squareFullDef(self,full):
        X = full[:,0]
        y= full[:,1]
        s1= np.trapz(y,x=X)
        logging.info(f"full def {s1}")
        return s1
    
    def __squareNarrowPart1(self, narrow, parameters:Result):
        if len(narrow) == 0:
            return None
        X = narrow[:,0]
        x_min = np.min(X)
        x_max = np.max(X)
        s = integrate.quad(self.__narrowFuncPart1,x_min,x_max,args=(parameters.narrow_a))
        logging.info(f"narrow part1 {s}")
        return s
    
    def __squareNarrowPart2(self, narrow, parameters:Result):
        if len(narrow) == 0:
            return None
        X = narrow[:,0]
        x_min = np.min(X)
        x_max = np.max(X)
        s = integrate.quad(self.__narrowFuncPart2, x_min, x_max, args=(parameters.narrow_d, parameters.narrow_q))
        logging.info(f"narrow part2 {s}")
        return s

    def __squareNarrowPart3(self, narrow, parameters:Result):
        if len(narrow) == 0:
            return None
        X = narrow[:,0]
        x_min = np.min(X)
        x_max = np.max(X)
        s = integrate.quad(self.__narrowFuncPart3, x_min, x_max, args=(parameters.narrow_w, parameters.narrow_v))
        logging.info(f"narrow part3 {s}")
        return s
    
    def __squareNarrow(self, narrow, parameters:Result):
        if len(narrow) == 0:
            return None
        X = narrow[:,0]
        x_min = np.min(X)
        x_max = np.max(X)
        self.c = 6.025
        s = integrate.quad(self.__narrowFunc, x_min, x_max, args=(parameters.narrow_a, parameters.narrow_d, parameters.narrow_q, parameters.narrow_w, parameters.narrow_v))
        logging.info(f"narrow {s}")
        return s
    
    def __squareNarrowDef(self, narrow):
        if len(narrow) == 0:
            return None
        X = narrow[:,0]
        y= narrow[:,1]
        s= np.trapz(y,x=X)
        logging.info(f"narrow def {s}")
        return s