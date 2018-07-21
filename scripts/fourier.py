#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fourier transformation of the sunspot signals
"""


import pandas as _pd
import numpy as _np
import scipy.fftpack as _sc_fftpack
import matplotlib.pyplot as _plt


class Script(object):
    """
    Main class for this Script
    """

    def __init__(self):
        """
        Constructor
        """
        self.sunspots = self.get_data()

    def run(self):
        """
        Runner method for this script
        """
        x_base = _np.linspace(-2 * _np.pi, 2 * _np.pi, self.sunspots.size)
        mid = _np.ptp(self.sunspots) / 2
        sine = mid + mid * _np.sin(_np.sin(x_base))
        sine_fft = self.fourier_transform(sine)
        print "Index of max sine FFT", _np.argsort(sine_fft)[-5:]

        transformed = self.fourier_transform(self.sunspots)
        print "Indices of max sunspots FFT", _np.argsort(transformed)[-5:]

        self.plot(self.sunspots, show=False, label="Sunspots")
        self.plot(sine, show=True, lw=2, label="Sine")

        self.plot(transformed, show=True, label="Transformed Sunspot")

        self.plot(sine_fft, show=True, label="Transformed Sine", lw=2)

    @classmethod
    def get_data(cls):
        """
        Get Sunspot-data from file
        """
        return _pd.read_csv("data/sunspots.csv")["SUNACTIVITY"].values

    @classmethod
    def fourier_transform(cls, data):
        """
        Return fourier transformed data

        Params:
            data
        """
        return _np.abs(_sc_fftpack.fftshift(_sc_fftpack.rfft(data)))

    @classmethod
    def plot(cls, data, show=True, **kwargs):
        """
        Plot data
        """
        _plt.plot(data, **kwargs)
        if show:
            _plt.grid(True)
            _plt.legend()
            _plt.show()


    def __call__(self):
        """
        Start run method
        """
        self.run()


if __name__ == "__main__":
    FOURIER_TRANSFORMATION = Script()
    FOURIER_TRANSFORMATION()
