import numpy as np

def getBondPrice(y, face, couponRate, m, ppy):
    dfs = (1+ y) ** -np.arange(1, m+1)
    discount_coupons = sum(face*couponRate*dfs)
    discount_face = face*dfs[-1]

    return(discount_coupons+discount_face)

