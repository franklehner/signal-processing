"""
Window functions
"""
import dataclasses
import pandas as pd


@dataclasses.dataclass
class Windows(object):
    """
    Class Windows
    """
    data: pd.DataFrame
    window: int

    def get_window(self, column: str, window_type: str) -> pd.DataFrame:
        """
        return a window for special type
        """
        return self.data[column].rolling(self.window, win_type=window_type).mean()

    def moving_average(self, column: str) -> pd.DataFrame:
        """
        Calculating the moving average
        """
        return self.data[column].rolling(self.window).mean()
