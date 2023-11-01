#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fourier transformation of the sunspot signals
"""
import click
import pandas as pd
import numpy as np
import scipy.fftpack as sc_fftpack
import matplotlib.pyplot as plt


@click.command()
def cli():
    """Client
    """
    sunspots = get_data()
    x_base = np.linspace(-2 * np.pi, 2 * np.pi, sunspots.size)
    mid = np.ptp(sunspots) / 2
    sine = mid + mid * np.sin(np.sin(x_base))
    sine_fft = fourier_transform(data=sine)
    max_sine = np.argsort(sine_fft)[-5:]
    print(f"Index of max sine FFT {max_sine}")

    transformed = fourier_transform(data=sunspots)
    plot(data=sunspots, show=False, label="Sunspots")
    plot(data=sine, show=True, lw=2, label="Sine")
    plot(data=transformed, show=True, label="Transformed")
    plot(data=sine_fft, show=True, label="Transformed")


def get_data() -> np.ndarray:
    """
    Get Sunspot-data from file
    """
    return pd.read_csv("data/sunspots.csv")["SUNACTIVITY"].values

def fourier_transform(data: np.ndarray) -> np.ndarray:
    """
    Return fourier transformed data
    """
    return np.abs(sc_fftpack.fftshift(sc_fftpack.rfft(data)))

def plot(data: np.ndarray, show: bool = True, **kwargs):
    """
    Plot data
    """
    plt.plot(data, **kwargs)
    if show:
        plt.grid(True)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
