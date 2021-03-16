# Copyright 2021, Some Body and contributors
#
# This source code is licensed under the Apache-2.0 License
# found in the LICENSE file in the root directory of this source tree.

import io
import subprocess

import example_python_project


def test_about() -> None:
    out = io.StringIO()
    example_python_project.about(out)
    print(out)


def test_about_main() -> None:
    rval = subprocess.call(["python", "-m", "example_python_project.about"])
    assert rval == 0
