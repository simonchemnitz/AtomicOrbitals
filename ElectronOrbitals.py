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



########################
#                      #
# n = 4, m = 0, l = 2, #  
#                      #
########################


Ndata = 500000
data = np.random.uniform(low=-10, high=10, size=(Ndata,3))
data = appendSpherical_np(data)
df = pd.DataFrame(data, columns = ["x", "y", "z", "r", "theta", "phi"])
df = df.assign(wav = lambda x: hwave(n = 4, m = 0, l = 2, 
                                     r = x["r"], theta = x["theta"], phi=x["phi"])  )
subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.01]




fig = go.Figure(data=[go.Scatter3d(
    x=subdf["x"],
    y=subdf["y"],
    z=subdf["z"],
    mode='markers',
    marker=dict(
        size=1.5,
        color=subdf["wav"],                # set color to an array/list of desired values
        colorscale='plasma',   # choose a colorscale
        opacity=0.3
    )
)])

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()


########################
#                      #
# n = 4, m = 0, l = 2, #  
#                      #
########################

Ndata = 500000
data = np.random.uniform(low=-30, high=30, size=(Ndata,3))
data = appendSpherical_np(data)
df = pd.DataFrame(data, columns = ["x", "y", "z", "r", "theta", "phi"])
df = df.assign(wav = lambda x: hwave(n = 4, m = 0, l = 1, 
                                     r = x["r"], theta = x["theta"], phi=x["phi"])  )

subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.003]

#Plot data
fig = go.Figure(data=[go.Scatter3d(
    x=subdf["x"],
    y=subdf["y"],
    z=subdf["z"],
    mode='markers',
    marker=dict(
        size=1.5,
        color=subdf["wav"],                # set color to an array/list of desired values
        colorscale='plasma',   # choose a colorscale
        opacity=0.3
    )
)])

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()


########################
#                      #
# n = 4, m = 0, l = 2, #  
#                      #
########################

#Number of data points
Ndata = 500000
#generate data
data = np.random.uniform(low=-15, high=15, size=(Ndata,3))
data = appendSpherical_np(data)
df = pd.DataFrame(data, columns = ["x", "y", "z", "r", "theta", "phi"])
df = df.assign(wav = lambda x: hwave(n = 4, m = 2, l = 3, 
                                     r = x["r"], theta = x["theta"], phi=x["phi"])  )

subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.0001]



#Plot data
fig = go.Figure(data=[go.Scatter3d(
    x=subdf["x"],
    y=subdf["y"],
    z=subdf["z"],
    mode='markers',
    marker=dict(
        size=1.5,
        color=subdf["wav"],                # set color to an array/list of desired values
        colorscale='plasma',   # choose a colorscale
        opacity=0.3
    )
)])

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()


########################
#                      #
# n = 4, m = 0, l = 2, #  
#                      #
########################

#Number of data points
Ndata = 500000
#generate data
data = np.random.uniform(low=-30, high=30, size=(Ndata,3))
data = appendSpherical_np(data)
df = pd.DataFrame(data, columns = ["x", "y", "z", "r", "theta", "phi"])
df = df.assign(wav = lambda x: hwave(n = 4, m = 2, l = 2, 
                                     r = x["r"], theta = x["theta"], phi=x["phi"])  )

subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.0001]


#Plot data
fig = go.Figure(data=[go.Scatter3d(
    x=subdf["x"],
    y=subdf["y"],
    z=subdf["z"],
    mode='markers',
    marker=dict(
        size=1.5,
        color=subdf["wav"],                # set color to an array/list of desired values
        colorscale='plasma',   # choose a colorscale
        opacity=0.3
    )
)])

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()


########################
#                      #
# n = 4, m = 0, l = 2, #  
#                      #
########################

#Number of data points
Ndata = 500000
#generate data
data = np.random.uniform(low=-20, high=20, size=(Ndata,3))
data = appendSpherical_np(data)
df = pd.DataFrame(data, columns = ["x", "y", "z", "r", "theta", "phi"])
df = df.assign(wav = lambda x: hwave(n = 3, m = 0, l = 1, 
                                     r = x["r"], theta = x["theta"], phi=x["phi"])  )

subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.005]


#Plot data
fig = go.Figure(data=[go.Scatter3d(
    x=subdf["x"],
    y=subdf["y"],
    z=subdf["z"],
    mode='markers',
    marker=dict(
        size=1.5,
        color=subdf["wav"],                # set color to an array/list of desired values
        colorscale='BlueRed',   # choose a colorscale
        opacity=0.3
    )
)])

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()
