# Copyright 2021, Some Body and contributors
#
# This source code is licensed under the Apache-2.0 License
# found in the LICENSE file in the root directory of this source tree.

import glob

import example_python_project


def test_version() -> None:
    assert example_python_project.__version__


def test_copyright() -> None:
    """Check that source code files contain a copyright line"""
    for fname in glob.glob("example_python_project/**/*.py", recursive=True):
        print("Checking " + fname + " for copyright header")

        with open(fname) as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                assert line.startswith("# Copyright")
                break
