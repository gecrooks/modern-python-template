# Copyright 2019-, Gavin E. Crooks and contributors
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import glob
import io
import subprocess

import python_mvp


def test_version() -> None:
    assert python_mvp.__version__


def test_about() -> None:
    out = io.StringIO()
    python_mvp.about(out)
    print(out)


def test_about_main() -> None:
    rval = subprocess.call(["python", "-m", "python_mvp.about"])
    assert rval == 0


def test_copyright() -> None:
    """Check that source code files contain a copyright line"""
    exclude = set(["python_mvp/version.py"])
    for fname in glob.glob("python_mvp/**/*.py", recursive=True):
        if fname in exclude:
            continue
        print("Checking " + fname + " for copyright header")

        with open(fname) as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                assert line.startswith("# Copyright")
                break
