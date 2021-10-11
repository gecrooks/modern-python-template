# Copyright 2021, Some Body and contributors
#
# This source code is licensed under the Apache-2.0 License
# found in the LICENSE file in the root directory of this source tree.

"""
Backwards compatibility.
"""


__all__ = ["importlib_metadata"]

try:
    # python >= 3.8
    from importlib import metadata as importlib_metadata  # type: ignore
except ImportError:  # pragma: no cover
    import importlib_metadata  # type: ignore  # noqa: F401
