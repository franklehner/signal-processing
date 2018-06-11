"""
Window functions
"""


class Windows(object):
    """
    Class Windows
    """
    def __init__(self, data, window):
        """
        Constructor
        """
        self.data = data
        self.window = window

    def get_window(self, column, window_type):
        """
        return a window for special type
        """
        return self.data[column].rolling(self.window, win_type=window_type).mean()

    def moving_average(self, column):
        """
        Calculating the moving average
        """
        return self.data[column].rolling(self.window).mean()
