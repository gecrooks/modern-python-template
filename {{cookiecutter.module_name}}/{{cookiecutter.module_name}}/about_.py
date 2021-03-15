# Copyright {{cookiecutter.copywrite}}
#
# This source code is licensed under the {{cookiecutter.license}} License
# found in the LICENSE file in the root directory of this source tree.

"""
About: Print information about this package.
"""
# NB: command line access is located in about.py

import platform
import re
import sys
import typing
from importlib import metadata as importlib_metadata

from .config import __version__

__all__ = ["about"]


def about(file: typing.TextIO = None) -> None:
    f"""Print information about this package.

     ``> python -m {__package__}.about``

    Args:
        file: Output stream (Defaults to stdout)
    """
    metadata = importlib_metadata.metadata(__package__)
    print(f"# {metadata['Name']}", file=file)
    print(f"{metadata['Summary']}", file=file)
    print(f"{metadata['Home-page']}", file=file)

    name_width = 24
    versions = {}
    versions["platform"] = platform.platform(aliased=True)
    versions[__package__] = __version__
    versions["python"] = sys.version[0:5]

    for req in importlib_metadata.requires(__package__):
        name = re.split("[; =><]", req)[0]
        try:
            versions[name] = importlib_metadata.version(name)
        except Exception:  # pragma: no cover
            pass

    print(file=file)
    print("# Configuration", file=file)
    for name, vers in versions.items():
        print(name.ljust(name_width), vers, file=file)
    print(file=file)
