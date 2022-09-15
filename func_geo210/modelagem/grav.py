import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gravity_anomaly_sphere(x0,y0,z0,a,rho,x,y,z):
    
    """
    Calcula a anomalia gravimétrica causada por uma esfera
    
    x0,y0,z0 - coordenadas do centro da esfera (km)
    a - raio da esfera (km)
    rho - densidade (kg.m^-3)
    x,y,z - coordenadas onde a medida é tomada
    
    Output
    gx,gy,gz - componentes do campo em unidades de mGal
    """
    
    gamma = 6.67*(10**(-11))
    si2mg = 10**5
    km2m = 10**3
    rx, ry, rz = x-x0, y-y0, z-z0
    r = np.sqrt(rx**2+ry**2+rz**2)
    
    if 0 in r:
        return 'parâmetro invalido'
    else:
        mass = 4*np.pi*rho*(a**3)/3
        return (-gamma*si2mg*km2m)*mass*np.asarray((rx,ry,rz))/(r**3)