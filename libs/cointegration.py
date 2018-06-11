"""
Cointegration test
==================
"""


import statsmodels.tsa.stattools as _ts


class Cointegration(object):
    """
    Class Cointegration
    """
    def __init__(self, vector1, vector2):
        """
        Constructor
        """
        self.vector1 = vector1
        self.vector2 = vector2

    def get_least_squares(self):
        """
        OLS
        """
        return _ts.OLS(self.vector1, self.vector2).fit()

    @classmethod
    def calc_adf(cls, resid):
        """
        Calculate Dickey-Fuller test
        """
        return _ts.adfuller(resid)
