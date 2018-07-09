"""
Test for cointegration lib
"""
# pylint: disable=invalid-name
# pylint: disable=no-member


import numpy as _np
import libs.cointegration as _cointegration


def create_sine_vector(vector):
    """
    Create a sine_vector
    """
    return _np.sin(_np.sin(vector))


def create_cosine_vector(vector):
    """
    Create a cosine vector
    """
    return 100 * _np.cos(vector) + 10


def create_vector(numbers):
    """
    Create a base vector from -2pi to 2pi
    """
    return _np.linspace(-2 * _np.pi, 2 * _np.pi, numbers)


def create_noise(numbers):
    """
    Create a vector with noise
    """
    return _np.random.normal(0, 0.1, numbers)  # pylint: disable=no-member


def test_get_least_squares_same_function():
    """
    test the least square method
    """
    vector = create_vector(309)
    sine = create_sine_vector(vector)
    least_squares = _cointegration.Cointegration(sine, sine).get_least_squares()
    assert least_squares.resid.sum() == 0.0


def test_get_least_squares_other_function():
    """
    test the least square method for two different functions
    """
    vector = create_vector(309)
    sine = create_sine_vector(vector)
    cosine = create_cosine_vector(vector)
    least_squares = _cointegration.Cointegration(sine, cosine).get_least_squares()
    assert least_squares.resid.sum() == 0.0
