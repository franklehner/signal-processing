#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-member
"""
Plot autocorrelation
"""


import os as _os
import argparse as _argparse
import pandas as _pd
import matplotlib.pyplot as _plt


def get_options():
    """
    Parse options and transfer them to the Script class

    return:
    =======
        options
    """
    parser = _argparse.ArgumentParser(description="Options for sunspots")

    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default="data/sunspots.csv",
        help="Filename with sunspot data"
    )

    options = parser.parse_args()

    if not _os.path.isfile(options.file):
        raise RuntimeError("Die Datei %s existiert nicht" % options.file)

    return options


class Script(object):
    """
    Main class for this script
    """
    def __init__(self):
        """
        Constructor
        """
        self.options = get_options()

    def run(self):
        """
        Runner method
        """
        data = self.load_data()
        print "\nAutocorrelation of sunactivity: ", data.SUNACTIVITY.autocorr()
        print
        self.plot_data(data, "SUNACTIVITY")

    def load_data(self):
        """
        load data from directory
        """
        return _pd.read_csv(self.options.file)

    @classmethod
    def plot_data(cls, data, column):
        """
        Plot the data as Autocorrelation
        """
        _pd.plotting.autocorrelation_plot(data[column])
        _plt.tight_layout()
        _plt.show()


if __name__ == "__main__":
    Script().run()
