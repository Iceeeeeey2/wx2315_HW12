import numpy as np

def getBondPrice(y, face, couponRate, m, ppy):
    t = np.arange(1, m * ppy + 1)  
    pv = (1 + y/ppy) ** (-t) 
    cf = couponRate / ppy * face 
    pvcf = pv * cf  
    pvcfsum = np.sum(pvcf)  
    bondprice = pvcfsum + (1 + y/ppy) ** (-m*ppy) * face  
    return (bondprice)


