#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object
"""
Moving average for sunspots
"""


import matplotlib.pyplot as _plt
import statsmodels.api as _sm

from libs.windows import Windows as _Windows


class Script(object):
    """
    Main class for script
    """
    def __init__(self, window):
        """
        Constructor
        """
        self.window = window
        self.sunspots = self.load_data()

    @classmethod
    def load_data(cls):
        """
        Load the sunspots data from statsmodels
        """
        return _sm.datasets.sunspots.load_pandas().data

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
    Script(11).run()
    Script(22).run()
