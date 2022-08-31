from re import template
import numpy as np
#import scipy.special as sp
import pandas as pd
import plotly.graph_objects as go

import util as util


class Hydrogen_Wave:
    def __init__(self) -> None:
        pass

    def vizualise_wave(self, threshold, plot_kwargs):
        self.evaluate_points()
        self.apply_threshold(threshold=threshold)
        self.get_plot_kwargs(plot_kwargs)
        self.create_dataframe()
        self.create_plot()

    def set_quantum_number(self, n, l, m):
        """
        Initialize the quantum numbers
        Parameters:
        -----------
        n : int
            Principle number, in [0,1,2,...]
        l : int
            Azimuthal number,  in [0,n-1]
        m : int
            Magnetic number, in [-l,l]
        """
        self.n = n
        self.l = l
        self.m = m

        self.initialize_wave_function()

    def initialize_wave_function(self):
        self.wave_function = lambda x: (
            util.wave_function(
                n=self.n, l=self.l, m=self.m, r=x[:, 0], theta=x[:, 1], phi=x[:, 2]
            )
        )

    def generate_data(self, n_points, low, high):
        data, r_theta_phi, x_y_z = util.generate_evaluation_points(n_points, low, high)
        self.r_theta_phi = r_theta_phi
        self.x_y_z = x_y_z
        self.data = data

    def evaluate_points(self):
        self.wav = self.wave_function(self.r_theta_phi)

    def apply_threshold(self, threshold):
        indices = np.where(np.abs(self.wav) > threshold)

        self.wav = self.wav[indices].reshape(-1, 1)
        self.x_y_z = self.x_y_z[indices]

    def create_dataframe(self):
        data = np.append(self.x_y_z, self.wav, axis=1)
        data = pd.DataFrame(data, columns=["x", "y", "z", "wav"])
        self.data = data

    def get_plot_kwargs(self, plot_kwargs):
        self.opacity = plot_kwargs["opacity"]
        self.marker_size = plot_kwargs["marker_size"]
        self.colorscale = plot_kwargs["colorscale"]
        self.theme = plot_kwargs["theme"]

    def create_plot(self):
        fig = go.Figure(
            data=[
                go.Scatter3d(
                    x=self.data["x"],
                    y=self.data["y"],
                    z=self.data["z"],
                    mode="markers",
                    marker=dict(
                        size=self.marker_size,
                        color=self.data["wav"],
                        colorscale=self.colorscale,
                        opacity=self.opacity,
                    ),
                )
            ]
        )
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        fig.update_layout(template=self.theme)
        fig.show()


if __name__ == "__main__":
    print()
    print()
    print()
    themes = [
        "plotly",
        "plotly_white",
        "plotly_dark",
        "ggplot2",
        "seaborn",
        "simple_white",
        "none",
    ]
    plot_kwargs = {
        "opacity": 1,
        "colorscale": "plasma",
        "marker_size": 2,
        "theme": "plotly_dark",
    }

    wave = Hydrogen_Wave()

    # n=4, l=2, m=0)
    wave.set_quantum_number(n=4, l=2, m=0)
    wave.generate_data(n_points=200000, low=-35, high=35)
    wave.vizualise_wave(threshold=0.01, plot_kwargs=plot_kwargs)

    # n=4, l=1, m=0
    wave.set_quantum_number(n=4, l=1, m=0)
    wave.generate_data(n_points=600000, low=-50, high=50)
    wave.vizualise_wave(threshold=0.02, plot_kwargs=plot_kwargs)

    # n=4, l=3, m=2)
    wave.set_quantum_number(n=4, l=3, m=2)
    wave.generate_data(n_points=600000, low=-30, high=30)
    wave.vizualise_wave(threshold=0.01, plot_kwargs=plot_kwargs)

    # n=4, l=2, m=2
    wave.set_quantum_number(n=4, l=2, m=2)
    wave.generate_data(n_points=600000, low=-35, high=35)
    wave.vizualise_wave(threshold=0.01, plot_kwargs=plot_kwargs)

    # n=4, l=2, m=2
    wave.set_quantum_number(n=4, l=2, m=2)
    wave.generate_data(n_points=600000, low=-35, high=35)
    wave.vizualise_wave(threshold=0.01, plot_kwargs=plot_kwargs)

    # n=5, l=3, m=1
    wave.set_quantum_number(n=5, l=3, m=1)
    wave.generate_data(n_points=600000, low=-50, high=50)
    wave.vizualise_wave(threshold=0.008, plot_kwargs=plot_kwargs)
