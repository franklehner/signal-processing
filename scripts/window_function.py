#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object
"""
Show different window functions
"""


import argparse as _argparse
import matplotlib.pyplot as _plt
import statsmodels.api as _sm

from libs.windows import Windows as _Window


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

    parser.add_argument(
        "-t",
        "--type",
        type=str,
        default="boxcar",
        help="""
        Define window type:
            - boxcar
            - triang
            - blackman
            - hanning
            - bartlett
        """
    )

    options = parser.parse_args()

    window_types = [
        "boxcar",
        "triang",
        "blackman",
        "hanning",
        "bartlett",
    ]

    if options.type not in window_types:
        raise ValueError("Wrong window type: Please use --help")

    return options


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
        self.win_type = self.options.type

    def run(self):
        """
        Runner method
        """
        sunspots = self.load_data()
        sunspots.set_index("YEAR", inplace=True)
        sunspots = sunspots.tail(150)
        sunspots_plot = sunspots.plot()
        window_data = self.get_window(sunspots, column=sunspots.columns[0])
        self.plot_window(sunspots, window_data, sunspots_plot)

    @classmethod
    def load_data(cls):
        """
        Load sunspots data
        """
        return _sm.datasets.sunspots.load_pandas().data

    def get_window(self, data, column):
        """
        Get the window data
        """
        window = _Window(data, self.window)
        return window.get_window(column, self.win_type)

    def plot_window(self, sunspots, window_data, sunspots_plot):
        """
        Plot window
        """
        sunspots.columns = [self.win_type]
        sunspots[self.win_type] = window_data.values
        sunspots.plot(ax=sunspots_plot)
        _plt.show()


if __name__ == "__main__":
    Script().run()
