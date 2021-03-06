#Packages
import numpy as np
import pandas as pd
from scipy.special import sph_harm, genlaguerre

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
    e = np.exp(-rho/2)*rho**l
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
    ptsnew=np.hstack((xyz, np.zeros(xyz.shape)))
    xy=xyz[:,0]**2 + xyz[:,1]**2
    ptsnew[:,3]=np.sqrt(xy + xyz[:,2]**2)
    ptsnew[:,4]=np.arctan2(np.sqrt(xy), xyz[:,2]) # for elevation angle defined from Z-axis down
    #ptsnew[:,4] = np.arctan2(xyz[:,2], np.sqrt(xy)) # for elevation angle defined from XY-plane up
    ptsnew[:,5]=np.arctan2(xyz[:,1], xyz[:,0])
    return ptsnew

def vizData(df, markersize=2, opacity=0.5):
    fig=go.Figure(data=[go.Scatter3d(
    x=df["x"],
    y=df["y"],
    z=df["z"],
    mode='markers',
    marker=dict(
        size=markersize,
        color=df["wav"],                # set color to an array/list of desired values
        colorscale='plasma',   # choose a colorscale
        opacity=opacity
    )
    )])

    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()

def generateData(nData, low, high):
    #Generate data
    data = np.random.uniform(low=low, high=high, size=(nData,3))
    #Add spherical coordinates
    data = appendSpherical_np(data)
    #Convert to Pandas DataFrame
    df = pd.DataFrame(data, columns= ["x", "y", "z", "r", "theta", "phi"])
    return df




#Examples



########################
#                      #
# n = 4, m = 0, l = 2, #  
#                      #
########################

#Variables
# Number of datapoints
Ndata = 200000
# Range of datapoints
low = -35
high = 35
# Quantum values
n = 4
m = 0
l = 2
#Generate data
df = generateData(nData = Ndata, low = low, high = high)

#Calculate Electron density
df = df.assign(wav = lambda x: hwave(n = n, m = m, l = l, 
                                     r = x["r"], 
                                     theta = x["theta"], 
                                     phi= x["phi"])  )
#Subset data
subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.01]

#Plot data
vizData(subdf)

########################
#                      #
# n = 4, m = 0, l = 1, #  
#                      #
########################

#Variables
# Number of datapoints
Ndata = 550000
# Range of datapoints
low = -50
high = 50
# Quantum values
n = 4
m = 0
l = 1
#Generate data
df = generateData(nData = Ndata, low = -50, high = 50)

#Calculate Electron density
df = df.assign(wav = lambda x: hwave(n = 4, m = 0, l = 1, 
                                     r = x["r"], 
                                     theta = x["theta"], 
                                     phi = x["phi"])  )
#Subset data
subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.02]

#Plot data
vizData(subdf)

########################
#                      #
# n = 4, m = 2, l = 3, #  
#                      #
########################

#Variables
# Number of datapoints
Ndata = 500000
# Range of datapoints
low = -30
high = 30
# Quantum values
n = 4
m = 2
l = 3
#Generate data
df = generateData(nData = Ndata, low = low, high = high)


#Calculate Electron density
df = df.assign(wav = lambda x: hwave(n = 4, m = 2, l = 3, 
                                     r = x["r"], 
                                     theta = x["theta"], 
                                     phi = x["phi"])  )
#Subset data
subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.01]

#Plot data
vizData(subdf)

########################
#                      #
# n = 4, m = 2, l = 2, #  
#                      #
########################

#Variables
# Number of datapoints
Ndata = 500000
# Range of datapoints
low = -35
high = 35
# Quantum values
n = 4
m = 2
l = 2
#Generate data
df = generateData(nData = Ndata, low = low, high = high)


#Calculate Electron density
df = df.assign(wav = lambda x: hwave(n = 4, m = 2, l = 2, 
                                     r = x["r"], 
                                     theta = x["theta"], 
                                     phi = x["phi"])  )
#Subset data
subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.01]

#Plot data
vizData(subdf)

########################
#                      #
# n = 3, m = 0, l = 1, #  
#                      #
########################

#Variables
# Number of datapoints
Ndata = 550000
# Range of datapoints
low = -50
high = 50
# Quantum values
n = 5
m = 1
l = 3

#Generate data
df = generateData(nData = Ndata, low = low, high = high)

#Calculate Electron density
df = df.assign(wav = lambda x: hwave(n = 5, m = 1, l = 3, 
                                     r = x["r"], 
                                     theta = x["theta"], 
                                     phi = x["phi"])  )
#Subset data
subdf = df.copy()
subdf = subdf.loc[subdf["wav"].abs()>0.008]

#Plot data
vizData(subdf)