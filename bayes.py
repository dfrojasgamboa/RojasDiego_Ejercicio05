import numpy as np
import matplotlib.pyplot as plt
import random

chain = 'scccc'

N = 100

chain = 'scccc'

Nc = chain.count('c')
Ns = chain.count('s')

H = np.linspace( 0 , 1 )
PH = np.ones(len(H))

def ver( H , Nc , Ns ):
    return H**Nc * ( 1 - H )**Ns

norm = sum( ver( H , Nc , Ns ) )
posterior = ver( H , Nc , Ns ) / norm

Ho = H[np.argmax( posterior )]
sigma = np.sqrt(Ho * (1-Ho) / len(H) )

def gaussian(x, mu, sigma):
    return np.exp(-np.power(x - mu, 2) / (2 * sigma**2))

norm_gauss = 1 / sum( gaussian(H, Ho, sigma) )


plt.figure()
plt.plot( H , posterior )
plt.plot( H , norm_gauss*gaussian(H, Ho, sigma) )
plt.title( 'H = ' + str(round(Ho,5)) + r'$\pm$' + str(round(sigma,5)) )
plt.savefig('coins.png')