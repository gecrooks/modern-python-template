# Copyright {{cookiecutter.copywrite}}
#
# This source code is licensed under the {{cookiecutter.license}} License
# found in the LICENSE file in the root directory of this source tree.

"""
Package wide configuration
"""


from importlib import metadata as importlib_metadata

__all__ = ["__version__"]


try:
    __version__ = importlib_metadata.version(__package__)  # type: ignore
except Exception:  # pragma: no cover
    # package is not installed
    __version__ = "0.0.0"
