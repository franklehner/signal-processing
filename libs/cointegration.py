"""
Cointegration test
==================
"""
import dataclasses
import statsmodels
import statsmodels.tsa.stattools as ts
import numpy as np


@dataclasses.dataclass
class Cointegration:
    """
    Class Cointegration
    """
    vector1: np.ndarray
    vector2: np.ndarray

    def get_least_squares(self) -> statsmodels.regression.linear_model.RegressionResultsWrapper:
        """
        OLS
        """
        return ts.OLS(self.vector1, self.vector2).fit()

    @classmethod
    def calc_adf(cls, resid):
        """
        Calculate Dickey-Fuller test
        """
        return ts.adfuller(resid)
