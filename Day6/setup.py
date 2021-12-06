from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Day6Part2',
    ext_modules=cythonize("day6p2Cython.py"),
    zip_safe=False,
)