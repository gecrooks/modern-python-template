# modern-python-template: How to setup an open source, github hosted, python package


![Build Status](https://github.com/gecrooks/modern-python-template/workflows/Build/badge.svg) 

[Source](https://github.com/gecrooks/modern-python-template)

## Quickstart

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) python template for a minimal python package. 
Install and run cookiecutter, answer the configuration questions, and you should be good to go.

    pip install -U cookiecutter
    cookiecutter https://github.com/gecrooks/modern-python-template.git

To complete github setup, create a new empty repo on github with the same name, add origin to our
project, and push to github.

    cd example_python_project
    git remote add origin https://github.com/somebody/example_python_project.git
    git push -u origin master
    git push origin v0.0.0

On github, you'll want to complete the About section (project description, website, and topics), add your PyPi user name and password as Secrets (if you're planning to upload to PyPi), and protect the [master branch](https://amachreeowanate.medium.com/how-to-protect-the-master-branch-on-github-ab85e9b6b03).

## About: On the creation and crafting of a python project

This is a discussion of the steps needed to setup an open source, github hosted, python package ready for further development.
The minimal project we're building is located in the [example_python_project](example_python_project) subdirectory. The rest of the files in the repo are for a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to create the example python project.

## Naming

The first decision to make is the name of the project. And for python packages the most important criteria is that the name isn't already taken on [pypi](https://pypi.org/), the repository from which we install python packages with `pip`. So we should do a quick Internet search: This name is available on pypi, there are no other repos of that name on github, and a google search doesn't pull up anything relevant. So we're good to go. 

Note that github repo and pypi packages are generally named using dashes (`-`), but that the corresponding python modules are named with underscores (`_`). (The reason for this dichotomy appears to be that underscores don't work well in URLs, but dashes are frowned upon in filenames.)

## License

The next decision is which of the plethora of [Open Source](https://opensource.org/licenses) licenses to use. We'll use the [Apache License](https://opensource.org/licenses/Apache-2.0), a perfectly reasonable, and increasingly popular choice. 


## Create repo

Next we need to initialize a git repo. It's easiest to create the repo on github and clone to our local machine (This way we don't have to mess around setting the origin and such like). Github will helpfully add a `README.md`, the license, and a python `.gitignore` for us. On Github, add a description, website url (typically pointing at readthedocs), project tags, and review the rest of github's settings. 
 

Note that MacOS likes to scatter `.DS_Store` folders around (they store the finder icon display options). We don't want to accidentally add these to our repo. But this is a machine/developer issue, not a project issue. So if you're on a mac you should configure git to ignore `.DS_Store` globally.

```
    # specify a global exclusion list
    git config --global core.excludesfile ~/.gitignore
    # adding .DS_Store to that list
    echo .DS_Store >> ~/.gitignore
```

## Clone repo 

On our local machine the first thing we do is create a new conda environment. (You have conda installed, right?) This way if we balls up the installation of some dependency (which happens distressingly often) we can nuke the environment and start again. 
```
    $ conda create --name GPT
    $ source activate GPT
    (GPT) $ python --version
    Python 3.11.0
```

Now we clone the repo locally.

```
    (GPT) $ git clone https://github.com/gecrooks/modern-python-template.git
    Cloning into 'modern-python-template'...
    remote: Enumerating objects: 4, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (4/4), done.
    (GPT) $ cd modern-python-template
```

Lets tag this initial commit for posterities sake (And so I can [link](https://github.com/gecrooks/modern-python-template/releases/tag/v0.0.0) to the code at this instance).
```
  (GPT) $ git tag v0.0.0
  (GPT) $ git push origin v0.0.0
```
For reasons that are unclear to me the regular `git push` doesn't push tags. We have push the tags explicitly by name. Note we need to specify a full MAJOR.MINOR.PATCH version number, and not just e.g. '0.1', for technical reasons that have to do with how we're going to manage package versions.


## Branch
It's always best to craft code in a branch, and then merge that code into the master branch.
```
$ git branch gec001-init
$ git checkout gec001-init
Switched to branch 'gec001-init'
```
I tend to name branches with my initials (so I know it's my branch on multi-developer projects), a serial number (so I can keep track of the chronological order of branches), and a keyword (if I know ahead of time what the branch is for).


## Packaging

Let's complete the minimum viable python project. We need the actual python module, signaled by a (currently) blank `__init__.py` file. 
```
    (GPT) $ mkdir example_python_project
    (GPT) $ touch example_python_project/__init__.py
```

Python standards for packaging and distribution seems to be in flux (again...). So, following what I think the current standard is, we need 3 files, `setup.py`, `pyproject.toml`, and `setup.cfg`. 

The modern `setup.py` is just a husk:

```
#!/usr/bin/env python

import setuptools

if __name__ == "__main__":
    setuptools.setup(use_scm_version=True)
```
Our only addition is `use_scm_version=True`, which activates versioning with git tags. More on that anon. Don't forget to set executable permissions on the setup.py script.
```
 $ chmod a+x setup.py
```
The [pyproject.toml](https://snarky.ca/what-the-heck-is-pyproject-toml/) file (written in [toml](https://github.com/toml-lang/toml) format) is a recent addition to the canon. It specifies the tools used to build the project.
```
# pyproject.toml
[build-system]
requires = ["setuptools>=42", "wheel", "setuptools_scm[toml]>=3.4"]
build-backend = "setuptools.build_meta"


# pyproject.toml
[tool.setuptools_scm]

```
Again, the parts with `setuptools_scm` are additions. 


All of the rest of the metadata goes in `setup.cfg` (in INI format).
```
# Setup Configuration File
# setup.cfg is the configuration file for setuptools. It tells setuptools about your package
# (such as the name and version) as well as which code files to include. Eventually much of
# this configuration may be able to move to pyproject.toml.
#
# https://packaging.python.org/tutorials/packaging-projects/
# https://docs.python.org/3/distutils/configfile.html
# [INI](https://docs.python.org/3/install/index.html#inst-config-syntax) file format.
#
# Project cut from gecrooks_python_template cookiecutter template
# https://github.com/gecrooks/modern-python-template


[metadata]
# https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html
# SPDX license short-form identifier, https://spdx.org/licenses/
# https://pypi.org/classifiers/
# setuptools v53.1.0+ expects lower cased keys, e.g. "Name" must be "name".

name = {{cookiecutter.module_name}}
summary = {{cookiecutter.short_description}}
long_description = file:README.md
long_description_content_type = text/markdown
keywords = python
url = https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.module_name}}/
author = {{cookiecutter.author_name}}
author_email = {{cookiecutter.author_email}}
license = {{cookiecutter.license}}
license_file = LICENSE
classifiers=
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    Intended Audience :: Science/Research
    Programming Language :: Python
    Natural Language :: English
    Operating System :: OS Independent
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: 3.10
    Programming Language :: Python :: 3.11
    Topic :: Scientific/Engineering
    Topic :: Software Development
    Topic :: Software Development :: Libraries
    Topic :: Software Development :: Libraries :: Python Modules
    Typing :: Typed


[options]
zip_safe = True
python_requires = >= 3.9
packages = find:

install_requires =
    numpy

setup_requires =
    setuptools_scm


[options.extras_require]
dev =
    numpy >= 1.20               # v1.20 introduces typechecking for numpy
    setuptools_scm
    pytest >= 4.6
    pytest-cov
    flake8
    mypy
    black
    isort
    sphinx
```
Confusingly there are two different standards for metadata. At present the metadata
lives in `setup.cfg` and should follow the setuptools 
[specification](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html). 
But the intention seems to be
that in the long run the metadata moves to `pyproject.toml` and follows a different 
[specification](https://packaging.python.org/specifications/core-metadata/).


It's good practice to support at least two consecutive versions of python. Starting with 3.9, python is moving to an annual [release schedule](https://www.python.org/dev/peps/pep-0602/). The initial 3.x.0 release will be in early October and the first bug patch 3.x.1 in early December, second in February, and so on.  Since it takes many important packages some time to upgrade (e.g. numpy and tensorflow are often bottlenecks), one should probably plan to upgrade python support around the beginning of each year. Upgrading involves changing the python version numbers in the workflow tests and `config.cfg`, and then cleaning up any `__future__` or conditional imports, or other hacks added to maintain compatibility with older python releases. If you protected the master branch on github, and added required status checks, you'll need to update those too. Supporting older python versions is often a good idea, if you don't need the newest wizz-bang python features. 


We can now install our package (as editable -e, so that the code in our repo is live).
```
   $ pip install -e .[dev] 
``` 
The optional `[dev]` will install all of the extra packages we need for test and development, listed under `[options.extras_require]` above.



## Versioning
Our project needs a version number (e.g. '3.1.4'). We'll try and follow the [semantic versioning](https://semver.org/) conventions. But as long as the major version number is '0' we're allowed to break things.

There should be a 
[single source of truth](https://packaging.python.org/guides/single-sourcing-package-version/) for this number.
My favored approach is use git tags as the source of truth (Option 7 in the above linked list). We're going to tag releases anyways, so if we also hard code the version number into the python code we'd violate the single source of truth principle. We use the [setuptools_scm](https://github.com/pypa/setuptools_scm) package to automatically construct a version number from the latest git tag during installation.

The convention is that the version number of a python packages should be available as `packagename.__version__`. 
So we add the following code to `example_python_project/config.py` to extract the version number metadata.
```

__all__ = ["__version__", "importlib_metadata", "about"]


# Backwards compatibility imports
try:
    # python >= 3.9
    from importlib import metadata as importlib_metadata  # type: ignore
except ImportError:  # pragma: no cover
    import importlib_metadata  # type: ignore  # noqa: F401


try:
    __version__ = importlib_metadata.version(__package__)  # type: ignore
except Exception:  # pragma: no cover
    # package is not installed
    __version__ = "0.0.0"

```
and then in `example_python_project/__init__.py`, we import this version number.
```
from .config import __version__ as __version__                      # noqa: F401
```
We put the code to extract the version number in `config.py` and not `__init__.py`, because we don't want to pollute our top level package namespace. 

The various pragmas in the code above ("pragma: no cover" and "type: ignore") are there because the conditional imports confuse both our type checker and code coverage tools.



## about

One of my tricks is to add a function to print the versions of the core upstream dependencies. This can be extremely helpful when debugging configuration or system dependent bugs, particularly when running continuous integration tests.

```
# Configuration (> python -m example_python_project.about)
platform                 macOS-10.16-x86_64-i386-64bit
example_python_project   0.0.0
python                   3.10.3
numpy                    1.20.1
setuptools_scm           5.0.2
pytest                   6.2.2
pytest-cov               2.11.1
flake8                   6.0.0
mypy                     0.812
black                    20.8b1
isort                    5.7.0
sphinx                   3.5.1
pre-commit               2.20.0
```
The `about()` function to print this information is placed in `about_.py`. The file `about.py` contains the standard python command line interface (CLI), 
```
if __name__ == '__main__':
    import example_python_project
    example_python_project.about()
```
It's important that `about.py` isn't imported by any other code in the package, else we'll get multiple import warnings when we try to run the CLI. 

If you don't want the `about` functionality remove the file `about.py`, `about()` function in config.py, and relevant tests in `config_test.py`, and edit the Makefile.

## Unit tests

Way back when I worked as a commercial programmer, the two most important things that I learned were source control and unit tests. Both were largely unknown in the academic world at the time.

(I was once talking to a chap who was developing a new experimental platform. The plan was to build several dozens of these gadgets, and sell them to other research groups so they didn't have to build their own. A couple of grad students wandered in. They were working with one of the prototypes, and they'd found some minor bug. Oh yes, says the chap, who goes over to his computer, pulls up the relevant file, edits the code, and gives the students a new version of that file. He didn't run any tests, because there were no tests. And there was no source control, so there was no record of the change he'd just made. That was it. The horror.)

Currently, the two main options for python unit tests appear to be `unittest` from the standard library and `pytest`. To me `unittest` feels very javonic. There's a lot of boiler plate code and I believe it's a direct descendant of an early java unit testing framework. Pytest, on the other hand, feels pythonic. In the basic case all we have to do is to write functions (whose names are prefixed with 'test_'), within which we test code with `asserts`. Easy.

There's two common ways to organize tests. Either we place tests in a separate directory, or they live in the main package along with the rest of the code. In the past I've used the former approach. It keeps the test organized and separate from the production code. But I'm going to try the second approach for this project. The advantage is that the unit tests for a piece of code live right next to the code being tested.

Let's test that we can access the version number (There is no piece of code too trivial that it shouldn't have a unit test.) In `example_python_project/config_test.py` we add

```
import example_python_project

def test_version():
    assert example_python_project.__version__
```
and run our test. (The 'python -m' prefix isn't strictly necessary, but it helps ensure that pytest is running under the correct copy of python.)
```

(GTP) $ python -m pytest
========================================================================================== test session starts ===========================================================================================
platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/work/Work/Projects/example_python_project
collected 1 item                                                                                                                                                                                         

example_python_project/config_test.py .                                                                                                                                                                            [100%]

=========================================================================================== 1 passed in 0.02s ============================================================================================
```

Note that in the main code we'll access the package with relative imports, e.g.
```
from . import __version__
```
But in the test code we use absolute imports. 
```
from example_python_project import __version__
```
In tests we want to access our code in the same way we would access it from the outside as an end user.


## Test coverage

At a bare minimum the unit tests should run (almost) every line of code. If a line of code never runs, then how do you know it works at all? (High code coverage does not mean you have a [good test suite](https://preslav.me/2020/12/03/the-myth-of-code-coverage/). But a good set of unit tests will have high code coverage.)

So we want to monitor the test coverage. The [pytest-cov](https://pypi.org/project/pytest-cov/) plugin to pytest will do this for us. Configuration is placed in the setup.cfg file (Config can also be placed in a separate `.coveragerc`, but I think it's better to avoid a proliferation of configuration files.)
```
# pytest configuration
[tool:pytest]
testpaths =
    example_python_project


# Configuration for test coverage
#
# https://coverage.readthedocs.io/en/latest/config.html
#
# python -m pytest --cov

[coverage:paths]
source =
    example_python_project

[coverage:run]
omit =
    *_test.py

[coverage:report]
# Use ``# pragma: no cover`` to exclude specific lines
exclude_lines =
    pragma: no cover
    except ImportError
    assert False
    raise NotImplementedError()
    pass
```

We have to explicitly omit the unit tests since we have placed the test files in the same directories as the code to test.

The [pragma](https://en.wikipedia.org/wiki/Directive_(programming)) `pragma: no cover` is used to mark untestable lines. This often happens with conditional imports used for backwards compatibility between python versions. The other excluded lines are common patterns of code that don't need test coverage.


## Linting

We need to lint our code before pushing any commits. I like [flake8](https://flake8.pycqa.org/en/latest/). It's faster than pylint, and (I think) better error messages. I will hereby declare:

    The depth of the indentation shall be 4 spaces. 
    And 4 spaces shall be the depth of the indentation. 
    Two spaces thou shall not use. 
    And tabs are right out. 

Four spaces is standard. [Tabs are evil](https://www.emacswiki.org/emacs/TabsAreEvil). I've worked on a project with 2-space indents, and I see the appeal, but I found it really weird. 

Most of flake8's defaults are perfectly reasonable and in line with [PEP8](https://www.python.org/dev/peps/pep-0008/) guidance. But even [Linus](https://lkml.org/lkml/2020/5/29/1038) agrees that the old standard of 80 columns of text is too restrictive. (Allegedly, 2-space indents were [Google's](https://www.youtube.com/watch?v=wf-BqAjZb8M&feature=youtu.be&t=260) solution to the problem that 80 character lines are too short. Just make the indents smaller!) Raymond Hettinger suggests 90ish (without a hard cutoff), and [black](https://black.readthedocs.io/en/stable/the_black_code_style.html) uses 88. So let's try 88.


The configuration also lives in `setup.cfg`.
```
# flake8 linter configuration
[flake8]
max-line-length = 88
ignore = E203, W503
```
We need to override the linter on occasion. We add pragmas such as `# noqa: F401` to assert that no, really, in this case we do know what we're doing.


Two other python code format tools to consider using are [isort](https://pypi.org/project/isort/) and [black, The uncompromising code formatter](https://black.readthedocs.io/en/stable/). Isort sorts your import statements into a canonical order. And Black is the Model-T Ford of code formatting -- any format you want, so long as it's Black. I could quibble about some of Black's code style, but in the end it's just easier to blacken your code and accept black's choices, and thereby gain a consistent coding style across developers. 

The command `make delint` will run `isort` and `black` on your code, with the right magic incantations so that they are compatible. (`isort --profile black` which appears to be equivalent to `isort -m 3 --tc --line-length 88`. We set this configuration project wide in `setup.cfg`)


## Copyright
It's common practice to add a copyright and license notice to the top of every source file -- something like this:
```

# Copyright 2019-, Gavin E. Crooks and contributors
#
# This source code is licensed under the Apache License, Version 2.0
# found in the LICENSE file in the root directory of this source tree.

```

I tend to forget to add these lines. So let's add a unit test `example_python_project/config_test.py::test_copyright` to make sure we don't.
```
def test_copyright():
    """Check that source code files contain a copyright line"""
    exclude = set(['example_python_project/version.py'])
    for fname in glob.glob('example_python_project/**/*.py', recursive=True):
        if fname in exclude:
            continue
        print("Checking " + fname + " for copyright header")

        with open(fname) as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                assert line.startswith('# Copyright')
                break
```


## API Documentation
[Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html) is the standard 
tool used to generate API documentation from the python source. Use the handy quick start tools. 
```
$ mkdir docsrc
$ cd docsrc
$ sphinx-quickstart
```
The defaults are reasonable. Enter the project name and author when prompted. 

Edit the conf.py, and add the following collection of extensions.
```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
```
[Autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) automatically extracts documentation from docstrings, and [napolean](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) enables [Google style](http://google.github.io/styleguide/pyguide.html) python docstrings.

We also add a newline at the end of `conf.py`, since the lack of a blank line at the end upsets our linter.

Go ahead and give it a whirl. This won't do anything interesting yet, but it's a start.
```
$ make html
```

One problem is that sphinx creates three (initially) empty directories, `_build`, `_static`, and `_templates`. But we can't add empty directories to git, since git only tracks files. The workaround is to add an empty `.gitignore` file to each of the `_static` and `_templates` directories. (An alternative convention is to add a `.gitkeep` file.) If we never want the files in these directories to be under source control, we can add a `*` to the `.gitignore` file.  Sphinx will create the `_build` directory when it's needed.

```
$ touch _templates/.gitignore _build/.gitignore _static/.gitignore
$ git add -f _templates/.gitignore _build/.gitignore _static/.gitignore
$ git add Makefile *.*
# cd ..
```


Note that we have placed the sphinx documentation tools in `docsrc` rather than the more traditional `docs`. This is to keep the `docs` directory available to serve documentation using `githubs-pages`. (We also have to update the root `.gitignore` file.)


## Makefile
I like to add a Makefile with targets for all of the common development tools I need to run. This is partially for convenience, and partially as documentation, i.e. here are all the commands you need to run to test, lint, typecheck, and build the code (and so on.) I use a [clever hack](https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html) so that the makefile self documents.

```
(GTP) $ make
about        Report versions of dependent packages
status       git status --short --branch
init         Install package ready for development
all          Run all tests
test         Run unittests
coverage     Report test coverage
lint         Lint check python source
delint       Run isort and black to delint project
typecheck    Static typechecking 
docs         Build documentation
docs-open    Build documentation and open in webbrowser
docs-clean   Clean documentation build
docs-github-pages Install html in docs directory ready for github pages
pragmas      Report all pragmas in code
build        Setuptools build
requirements Make requirements.txt
```

The pragmas target searches the code and lists all of the pragmas that occur. Common uses of [pragmas](https://en.wikipedia.org/wiki/Directive_(programming)) are to override the linter, tester, or typechecker. 


## Readthedocs
We'll host our API documentation on [Read the Docs](readthedocs.org). We'll need a basic configuration file, `.readthedocs.yml`.
```
version: 2
formats: []
sphinx:
  configuration: docs/conf.py
python:
  version: 3.9
```
I've already got a readthedocs account, so setting up a new project takes but a few minutes. 


## README.md

We add some basic information and installation instructions to `README.mb`. Github displays this file on your project home page (but under the file list, so if you have a lot of files at the top level of your project, people might not notice your README.)

A handy trick is to add Build Status and Documentation Status badges for Github actions tests and readthedocs. These will proudly declare that your tests are passing (hopefully). (See top of this file)


## Continuous Integration

Another brilliant advance to software engineering practice is continuous integration (CI). The basic idea is that all code gets thoroughly tested before it's added to the master branch.

Github now makes this very easy to setup with Github actions. They even provide basic templates. This testing workflow lives in `.github/workflows/python-build.yml`, and is a modification of Github's  `python-package.yml` workflow.
```
# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python package

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
  schedule:
    - cron: "0 13 * * *"  # Every day at 1pm UTC (6am PST)    

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11']

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        python -m pip install -e .[dev]  # install package + test dependencies
    - name: About
      run: |
        python -m $(python -Wi setup.py --name).about
    - name: Lint with flake8
      run: |
        flake8 .
    - name: Test with pytest
      run: |
        python -m pytest --cov-fail-under 100
    - name: Typecheck with mypy
      run: |
        mypy
    - name: Build documentation with sphinx
      run: |
        sphinx-build -M html docsrc docsrc/_build

```
Note that these tests are picky. Not only must the unit tests pass, but test coverage must be 100%, the code must be delinted, blackened, isorted, and properly typed, and the docs have to build without error.

It's a good idea to set a cron job to run the test suite against the main branch on a regular basis (the `schedule` block above). This will alert you of problems caused by your dependencies updating. (For instance, one of my other projects just broke, apparently because flake8 updated its rules.)

Let's add, commit, and push our changes. 
```
$ git status
On branch gec001-init
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   .readthedocs.yml
    new file:   .github/workflows/python-package.yml
    new file:   Makefile
    modified:   README.md
    new file:   docs/Makefile
    new file:   docs/_build/.gitignore
    new file:   docs/_static/.gitignore
    new file:   docs/_templates/.gitignore
    new file:   docs/conf.py
    new file:   docs/index.rst
    new file:   pyproject.toml
    new file:   example_python_project/__init__.py
    new file:   example_python_project/about.py      
    new file:   example_python_project/config.py
    new file:   example_python_project/config_test.py  
    new file:   setup.cfg
    new file:   setup.py
    
$ git commit -m "Minimum viable package"
...
$ git push --set-upstream origin gec001-init
...
```
If all goes well Github will see our push, and build and test the code in the branch. Probably all the tests won't pass on the first try. It's easy to forget something (which is why we have automatic tests). So tweak the code, and push another commit until the tests pass.

## Git pre-commit

Another handy trick is to add a (pre-commit](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/) hook to git, so that some tests are run before code can be committed.
A basic example hook to run black before commit is located in `.pre-commit-config.yaml`. The make command `init` 
will install the pre-commit hook.
 
## Editorconfig

[EditorConfig](https://editorconfig.org/) is a handy way of specifying code formatting conventions, such as indent levels and line endings. The .editorconfig lives in the root of the repository, and is understood by many popular IDEs and ext editors.


## PyPi

We should now be ready to do a test submission to PyPI, The Python Package Index (PyPI).
Follow the directions laid out in the [python packaging](https://packaging.python.org/tutorials/packaging-projects/) documentation.

```
$ pip install -q build twine
...
$ git tag v0.1.0rc1
$ python -m build 
...
```
We tag our release candidate so that we get a clean version number (pypi will object to the development version numbers setuptools_scm generates if the tag or git repo isn't up to date).

First we push to the pypi's test repository.
```
(GTP) $ python -m twine upload --repository testpypi dist/*
```
You'll need to create a pypi account if you don't already have one. 

Let's make sure it worked by installing from pypi into a fresh conda environment.
```
(GTP) $ conda deactivate
$ conda create --name tmp
$ conda activate tmp
(tmp) $ pip install --index-url https://test.pypi.org/simple/ --no-deps modern-python-template
(tmp) $ python -m example_python_project.about
(tmp) $ conda activate GTP
```


## Merge and Tag

Over on github we create a pull request, wait for the github action checks to give us the green light once all the tests have passed, and then squash and merge. 

The full developer sequence goes something like this

1.) Sync the master branch. 
```
$ git checkout master
$ git pull origin master
```
(If we're working on somebody else's project, this step is a little more complicated. We fork the project on github, clone our fork to the local machine, and then set git's 'upstream' to be the original repo. We then sync our local master branch with the upstream master branch
```
$ git checkout master
$ git fetch upstream
$ git merge upstream/master
```
This should go smoothly as long as you never commit directly to your local master branch.)


2.) Create a working branch.
```
$ git branch BRANCH
$ git checkout BRANCH
```

3.) Do a bunch of development on the branch, committing incremental changes as we go along.

4.) Sync the master branch with github (since other development may be ongoing.) (i.e. repeat step 1)

5.) Rebase our branch to master. 
```
$ git checkout BRANCH
$ git rebase master
```
If there are conflicts, resolve them, and then go back to step 4.

6.) Sync our branch to github

```
$ git push
```

7.) Over on github, create a pull request to merge into the master branch

8.) Wait for the integration tests to pass. If they don't, fix them, and then go back to step 4.

9.) Squash and merge into the master branch on github. Squashing merges all of our commits on the branch into a single commit to merge into the master branch. We generally don't want to pollute the master repo history with lots of micro commits. (On multi-developer projects, code should be reviewed. Somebody other than the branch author approves the changes before the final merge into master.)

10.) Goto step 1. Back on our local machine, we resync master, create a new branch, and continue developing. 


## Tag and release

Assuming everything went well, you can now upload a release to pypi proper. We can add a [github workflow](.github/workflows/python-publish.yml) to automatically upload new releases tagged on github. The only additional configuration is to upload `PYPI_USERNAME` and `PYPI_PASSWORD` to github as secrets (under your repo settings). 

## Extras: requirements.txt
The `setup.cfg` file specifies the minimum versions of dependencies.  But for testing and deployment it can be useful to pin exact versions.

    > pip freeze > requirements.txt

And to install these exact versions:
    
    > pip install -r requirements.txt

If a `requirements.txt` exists then those versions are installed by the github workflows and the `make init` command.


## Extras: MANIFEST.in
You don't need a [`MANIFEST.in` file](https://www.remarkablyrestrained.com/python-setuptools-manifest-in/).

Historically, this file was used to specify which additional files, (typically data files) should be included in a packaged distribution. 
But `setuptools_scm` takes care of that for us (in most cases), by default including all files under source control.


## Cookiecutter

Having shorted out our basic module configuration and layout, the next trick is to turn the package into a 
[cookiecutter](https://cookiecutter.readthedocs.io/) project template. That way we can create a new project in
just a few moments.

    pip install -U cookiecutter
    cookiecutter https://github.com/gecrooks/modern-python-template.git
  
Answer the questions, create a new empty repo on github with the same name, push, and you should be good to go.

    cd example_python_project
    git remote add origin https://github.com/somebody/example_python_project.git
    git push -u origin master


The basic idea is to replace customizable text with  template strings, e.g. `{{cookiecutter.author_email}}`. 
Defaults for these templates are stored in `cookiecutter.json`. In particular example_python_package is moved to a directory called 
`{{cookiecutter.module_name}}`, and the module code is moved to 
`{{cookiecutter.module_name}}/{{cookiecutter.module_name}}`. 
I'm more or less following [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)

One tricky bit is that some of the github configuration files already contain similar template strings. So we have to
wrap those strings in special raw tags.

    {% raw %} some stuff with {templates} {% endraw %}

I also added some pre- and post- templating hooks (in the `hooks` subdirectory). These initialize and tag a git repo in the created module, and pip install the package.


## Conclusion

By my count our minimal project has 13 configuration files (In python, toml, yaml, INI, gitignore, Makefile, and plain text formats), 2 documentation files, one file of unit tests, and 3 files of code (containing 31 lines of code). 

We're now ready to create a new git branch and start coding in earnest.


## Further reading

* [Boring Python: dependency management, by James Bennett](https://www.b-list.org/weblog/2022/may/13/boring-python-dependencies/)
* [Boring Python: code quality, by James Bennett](https://www.b-list.org/weblog/2022/dec/19/boring-python-code-quality/)
