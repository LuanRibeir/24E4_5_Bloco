from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("sum_parallel.pyx"),
    include_dirs=[numpy.get_include()]
)

