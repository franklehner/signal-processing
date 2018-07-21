#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object
"""
Moving average for sunspots
"""


import argparse as _argparse
import pandas as _pd
import matplotlib.pyplot as _plt

from libs.windows import Windows as _Windows


def get_options():
    """
    Parse options and transfer them to the Script class

    return:
    =======
        options
    """
    parser = _argparse.ArgumentParser(description="Options for sunspots")
    parser.add_argument(
        "-w",
        "--window",
        type=int,
        default=11,
        help="Window size for rolling data"
    )
    return parser.parse_args()


class Script(object):
    """
    Main class for script
    """
    def __init__(self):
        """
        Constructor
        """
        self.options = get_options()
        self.window = self.options.window
        self.sunspots = self.load_data()

    @classmethod
    def load_data(cls):
        """
        Load the sunspots data from statsmodels
        """
        return _pd.read_csv("data/sunspots.csv")

    def run(self):
        """
        Runner method for the script
        """
        year_range = self.sunspots["YEAR"].values
        sunactivity = self.get_moving_average()
        self.plot(year_range, sunactivity)

    def get_moving_average(self, column="SUNACTIVITY"):
        """
        Get the moving average
        """
        window = _Windows(self.sunspots, self.window)
        return window.moving_average(column)

    def plot(self, year_range, sunactivity):
        """
        Plot the moving average
        """
        _plt.plot(
            year_range,
            self.sunspots["SUNACTIVITY"].values,
            label="Original"
        )

        _plt.plot(
            year_range,
            sunactivity.values,
            label="SMA %s" % self.window
        )

        _plt.legend()
        _plt.show()


if __name__ == "__main__":
    Script().run()
