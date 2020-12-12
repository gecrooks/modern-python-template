# Copyright 2019-2021, Gavin E. Crooks and contributors
#
# This source code is licensed under the Apache License 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import glob
import io
import subprocess

import gecrooks_python_template


def test_version() -> None:
    assert gecrooks_python_template.__version__


def test_about() -> None:
    out = io.StringIO()
    gecrooks_python_template.about(out)
    print(out)


def test_about_main() -> None:
    rval = subprocess.call(["python", "-m", "gecrooks_python_template.about"])
    assert rval == 0


def test_copyright() -> None:
    """Check that source code files contain a copyright line"""
    exclude = set(["gecrooks_python_template/version.py"])
    for fname in glob.glob("gecrooks_python_template/**/*.py", recursive=True):
        if fname in exclude:
            continue
        print("Checking " + fname + " for copyright header")

        with open(fname) as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                assert line.startswith("# Copyright")
                break
