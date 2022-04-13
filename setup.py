from setuptools import setup, find_packages

setup(
    name="tic_tac_toe",
    packages=find_packages('src'),
    package_dir={'': 'src'},
)