#Packages
import numpy as np
import pandas as pd
from scipy.special import sph_harm, genlaguerre

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


#Functions
def hwave(n, m, l, r, theta, phi):
    """
    Calculate The normalized position wavefunctions
    in spherical coordinates
    Parameters
    ----------
    n : int
        Principle quantum number
    m : int
        Magnetic quantum number
    l : int
        Azimuthal quantum number
    r : float
        Radius
    theta : float
        angle theta in radians
    phi : float
        angle phi in radians
    
    returns
    ----------
    psi(r,theta,phi) : float
    """
    #a0star = (4*pi*epsilon0*hbar**2)/(mu*np.exp(2))
    a0star = 1
    #Define variables
    rho = (2*r)/(n*a0star)
    root = np.sqrt( ( ( (2)/(a0star) )**3 )*( (np.math.factorial(n-l-1))/(2*n*(np.math.factorial(n+l) ) ) ) )
    e = np.exp(-rho/2)
    #General laguare poly
    L = genlaguerre(n-l-1,2*l+1)(rho)
    #Spherical harmonic
    Y = sph_harm(m, l, theta, phi)
    return np.real(root*e*L*Y)

def appendSpherical_np(xyz):
    """
    Append spherical coordinates 
    to numpy array of cartesian coordinates
    By: mtrw
    """
    ptsnew = np.hstack((xyz, np.zeros(xyz.shape)))
    xy = xyz[:,0]**2 + xyz[:,1]**2
    ptsnew[:,3] = np.sqrt(xy + xyz[:,2]**2)
    ptsnew[:,4] = np.arctan2(np.sqrt(xy), xyz[:,2]) # for elevation angle defined from Z-axis down
    #ptsnew[:,4] = np.arctan2(xyz[:,2], np.sqrt(xy)) # for elevation angle defined from XY-plane up
    ptsnew[:,5] = np.arctan2(xyz[:,1], xyz[:,0])
    return ptsnew


