from .setuptools_conda import dist_conda

try:
    from __version__ import __version__
except ImportError:
    __version__ = None