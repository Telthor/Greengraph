from setuptools import setup, find_packages

setup(
        name = "Greengraph",
        version = "0.1",
        packages = find_packages(),
        scripts = ['scripts/greengraph','scripts/greengraph_long.py'],
        install_requires = ['argparse', 'matplotlib', 'geopy', 'numpy', 'requests' ]
)

