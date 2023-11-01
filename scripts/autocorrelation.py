#!/usr/bin/env python
"""
Plot autocorrelation
"""
import click
import pandas as pd
import matplotlib.pyplot as plt


@click.command()
@click.option(
    "-f",
    "--filename",
    type=str,
    default="data/sunsports.csv",
    help="Filename with sunspot data",
)
def cli(filename: str):
    """Client
    """
    data = load_data(filename=filename)
    print(f"\nAutocorrelation of sunactivity: {data.SUNACTIVITY.autocorr()}")


def load_data(filename: str) -> pd.DataFrame:
    """
    load data from directory
    """
    return pd.read_csv(filename)

def plot_data(data: pd.DataFrame, column: str):
    """
    Plot the data as Autocorrelation
    """
    pd.plotting.autocorrelation_plot(data[column])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
