"""
setup.py
"""


from setuptools import setup, find_packages


setup(
    name="signal-processing",
    version="0.0.1",
    author="Frank Lehner",
    author_email="frank.lehner@unity-mail.de",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "statsmodels",
        "matplotlib",
    ]
)
