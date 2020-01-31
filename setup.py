from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy


ext_modules = [Extension('c_mandel.calc_mandel', ['c_mandel/calc_mandel.pyx'],
                         include_dirs=[numpy.get_include()])]

setup(
    name='c_mandel',
    author='szshi',
    packages=['c_mandel'],
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
