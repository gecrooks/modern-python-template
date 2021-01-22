# Copyright 2021, Some Body and contributors
#
# This source code is licensed under the Apache-2.0 License
# found in the LICENSE file in the root directory of this source tree.

# Command line interface for the about() function
# > python -m example_python_project.about
#
# NB: This module should not be imported by any other code in the package
# (else we will get multiple import warnings)

if __name__ == "__main__":
    import example_python_project

    example_python_project.about()
