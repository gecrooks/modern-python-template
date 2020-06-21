# Copyright 2019-, Gavin E. Crooks and contributors
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Package wide configuration
"""

import sys
import typing
import re
import platform

try:  # pragma: no cover
    # python >= 3.8
    from importlib.metadata import PackageNotFoundError  # type: ignore
    from importlib.metadata import requires  # type: ignore
    from importlib.metadata import version  # type: ignore
except ImportError:  # pragma: no cover   # type: ignore
    # python == 3.7
    from importlib_metadata import PackageNotFoundError  # type: ignore
    from importlib_metadata import requires  # type: ignore
    from importlib_metadata import version  # type: ignore


__all__ = ["__version__", "about"]


package_name = "python_mvp"

try:
    __version__ = version(package_name)
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = "?.?.?"


def about(file: typing.TextIO = None) -> None:
    """Print information about the configuration

     ``> python -m python_mvp.about``

    Args:
        file: Output stream (Defaults to stdout)
    """
    name_width = 24
    versions = {}
    versions["platform"] = platform.platform(aliased=True)
    versions[package_name] = __version__
    versions["python"] = sys.version[0:5]

    for req in requires(package_name):
        name = re.split("[; =><]", req)[0]
        try:
            versions[name] = version(name)
        except PackageNotFoundError:  # pragma: no cover
            pass

    print(file=file)
    print("# Configuration (> python -m python_mvp.about)", file=file)
    for name, vers in versions.items():
        print(name.ljust(name_width), vers, file=file)
    print(file=file)
