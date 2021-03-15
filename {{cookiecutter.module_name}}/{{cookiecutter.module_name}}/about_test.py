# Copyright {{cookiecutter.copywrite}}
#
# This source code is licensed under the {{cookiecutter.license}} License
# found in the LICENSE file in the root directory of this source tree.

import io
import subprocess
import {{cookiecutter.module_name}}


def test_about() -> None:
    out = io.StringIO()
    {{cookiecutter.module_name}}.about(out)
    print(out)


def test_about_main() -> None:
    rval = subprocess.call(["python", "-m", "{{cookiecutter.module_name}}.about"])
    assert rval == 0
