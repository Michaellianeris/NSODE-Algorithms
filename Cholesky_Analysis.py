import scipy.linalg as spla
import numpy as np
import matplotlib.pyplot as plt 



def Cholesky(A) :
    
                      
    L=np.linalg.cholesky(A)
    
    return L



def my_back_solve(U,y) :
    n=len(U)
    x=np.zeros(n)
    x[n-1] = y[n-1] / U[n-1, n-1]
    for k in range(n-2, -1, -1):
        sums = y[k]
        for j in range(k+1, n):
            sums = sums - (U[k,j] * x[j])
        x[k] = sums / U[k,k]
    return x



def my_fwd_solve(L,b) :
    n=len(L)
    y=np.zeros(n)
    y[0] = b[0] / L[0, 0]
    for k in range(1,n):
        sums = b[k]
        for j in range(0, n):
            sums = sums - (L[k,j] * y[j])
        y[k] = sums / L[k,k]
    return y

#----------------Main Programme ----------------------------------#

A=np.array([[4.,6.,10.],[6.,25.,19.],[10.,19.,62.]])
b=np.array([66,39,474])


L=Cholesky(A)

y=my_fwd_solve(L,b)
x=my_back_solve(L.T,y)


print(x)







