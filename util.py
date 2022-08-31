import numpy as np
import scipy.special as sp
import pandas as pd
import plotly.graph_objects as go


def wave_function(n, l, m, r, theta, phi):
    """
    Calculate The normalized position wavefunctions
    in spherical coordinates
    Parameters
    ----------
    n : int
        Principle quantum number
    l : int
        Azimuthal quantum number
    m : int
        Magnetic quantum number
    r : float
        Radius
    theta : float
        Angle theta in radians
    phi : float
        Angle phi in radians

    returns
    ----------
    psi(r,theta,phi) : float
    """
    # a0star = (4*pi*epsilon0*hbar**2)/(mu*np.exp(2))
    a0star = 1
    # Define variables
    rho = (2 * r) / (n * a0star)
    root = np.sqrt(
        (((2) / (a0star)) ** 3)
        * ((np.math.factorial(n - l - 1)) / (2 * n * (np.math.factorial(n + l))))
    )
    e = np.exp(-rho / 2) * rho**l
    # General laguare poly
    L = sp.genlaguerre(n - l - 1, 2 * l + 1)(rho)
    # Spherical harmonic
    Y = sp.sph_harm(m, l, theta, phi)
    return np.real(root * e * L * Y)


def generate_evaluation_points(n_points, low, high):
    """
    Generate n_points in the 3 dimensional box defined by [low, high]^3

    Parameters:
    -----------
    n_points : int
        Number of points to evaluate the wave function in
    low : float
        The lowest allowed value for a coordinate (x,y,z)
    high : float
        The highest allowed value for a coordinate (x,y,z)
    """
    data = np.random.uniform(low=low, high=high, size=(n_points, 3))
    spherical_data = append_spherical(data)
    r_theta_phi = spherical_data[:, 3:6]
    x_y_z = spherical_data[:, :3]

    df = pd.DataFrame(spherical_data, columns=["x", "y", "z", "r", "theta", "phi"])
    return df, r_theta_phi, x_y_z


def append_spherical(xyz):
    """
    Append spherical coordinates
    to numpy arry of cartesian coordinates

    Parameters:
    -----------
    xyz : np.array
        Numpy array containing coordinates (x,y,z)
        of the shape (-1,3)
    """
    ptsnew = np.hstack((xyz, np.zeros(xyz.shape)))
    xy = xyz[:, 0] ** 2 + xyz[:, 1] ** 2
    ptsnew[:, 3] = np.sqrt(xy + xyz[:, 2] ** 2)
    ptsnew[:, 4] = np.arctan2(
        np.sqrt(xy), xyz[:, 2]
    )  # for elevation angle defined from Z-axis down
    # ptsnew[:,4] = np.arctan2(xyz[:,2], np.sqrt(xy)) # for elevation angle defined from XY-plane up
    ptsnew[:, 5] = np.arctan2(xyz[:, 1], xyz[:, 0])
    return ptsnew


def vizualise_data(df, markersize=2, opacity=0.5, colorscale="plasma"):
    """
    Create a plotly figure of the data

    Parameters:
    -----------
    df : pandas.DataFrame()
        Dataframe containing x,y,z coordinates and the value of the wave function
    markers : float
        Size of the plotting markers
    opacity : float
        Opacity of plotting markers
    """
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=df["x"],
                y=df["y"],
                z=df["z"],
                mode="markers",
                marker=dict(
                    size=markersize,
                    color=df["wav"],
                    colorscale=colorscale,
                    opacity=opacity,
                ),
            )
        ]
    )

    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()

    return fig
