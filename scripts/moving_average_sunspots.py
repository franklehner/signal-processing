#!/usr/bin/env python
"""
Moving average for sunspots
"""
import click
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from libs.windows import Windows


@click.command()
@click.option(
    "-w",
    "--window",
    type=int,
    default=11,
    help="Window size for rolling data",
)
def cli(window: int):
    """Client
    """
    sunspots = load_data()
    year_range = sunspots["Year"].values
    sun_activity = get_moving_average(sunspots=sunspots, wd=window)
    plot(
        sunspots=sunspots,
        window=window,
        year_range=year_range,
        sunactivity=sun_activity,
    )


def load_data() -> pd.DataFrame:
    """
    Load the sunspots data from statsmodels
    """
    return pd.read_csv("data/sunspots.csv")

def get_moving_average(sunspots: pd.DataFrame, wd: int, column: str = "SUNACTIVITY") -> pd.Series:
    """
    Get the moving average
    """
    window = Windows(sunspots, wd)

    return window.moving_average(column=column)

def plot(sunspots: pd.DataFrame, window: int, year_range: np.ndarray, sunactivity):
    """
    Plot the moving average
    """
    plt.plot(
        year_range,
        sunspots["SUNACTIVITY"].values,
        label="Original"
    )

    plt.plot(
        year_range,
        sunactivity.values,
        label=f"SMA {window}",
    )
    plt.legend()
    plt.show()


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
