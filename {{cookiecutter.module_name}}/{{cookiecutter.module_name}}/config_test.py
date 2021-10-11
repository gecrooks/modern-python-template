# Copyright {{cookiecutter.copywrite}}
#
# This source code is licensed under the {{cookiecutter.license}} License
# found in the LICENSE file in the root directory of this source tree.

import glob
import io
import subprocess

import {{cookiecutter.module_name}}


def test_version() -> None:
    assert {{cookiecutter.module_name}}.__version__


def test_copyright() -> None:
    """Check that source code files contain a copyright line"""
    for fname in glob.glob("{{cookiecutter.module_name}}/**/*.py", recursive=True):
        print("Checking " + fname + " for copyright header")

        with open(fname) as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                assert line.startswith("# Copyright")
                break


def test_about() -> None:
    out = io.StringIO()
    {{cookiecutter.module_name}}.about(out)
    print(out)


def test_about_main() -> None:
    rval = subprocess.call(["python", "-m", "{{cookiecutter.module_name}}.about"])
    assert rval == 0
