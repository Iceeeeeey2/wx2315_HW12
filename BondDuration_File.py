import numpy as np

def getBondDuration(y, face, couponRate, m, ppy):
    dfs = (1+ y) ** -np.arange(1, m+1)
    discount_coupons = sum(face*couponRate*dfs)
    discount_face = face*dfs[-1]
    bondprice = discount_coupons+discount_face

    t = np.arange(1, m * ppy + 1) 
    weighted_sum = sum(face*couponRate*dfs*t)+discount_face*m  
    bondDuration = weighted_sum / bondprice  
    return(bondDuration)


    
