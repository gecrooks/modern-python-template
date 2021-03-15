# Copyright {{cookiecutter.copywrite}}
#
# This source code is licensed under the {{cookiecutter.license}} License
# found in the LICENSE file in the root directory of this source tree.

# Command line interface for the about() function
# > python -m {{cookiecutter.module_name}}.about
#
# NB: This module should not be imported by any other code in the package
# (else we will get multiple import warnings)
# Implementation is located in about_.py

if __name__ == "__main__":
    import {{cookiecutter.module_name}}

    {{cookiecutter.module_name}}.about()
