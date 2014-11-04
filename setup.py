from setuptools import setup, find_packages

setup(
    name = "GreenAnalysis",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greennessGraph'],
    install_requires = ['argparse']
)
