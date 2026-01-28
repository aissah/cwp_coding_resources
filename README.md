# Overview

The repo is meant to serve as a template for Center for Wave Phenomena (CWP) codes with coding requirements guidelines and documentation of the various coding resources. Each of the files and directories are described here in the various sections.

## cwp_coding_resources

This directory contains codes relevant to the project itself. It may include separate files or directories for helper functions and the main code. This can be renamed to the name of the project. Currently, it contains a `__init__.py` file which makes the directory a package. This is useful when we want to import functions from the package in other files. It also contains a `project_codes.py` file which is the entry point of the project. This is where the main code is run from and can also be renamed to the name of the project. Finally, it contains a `utils.py` file which contains helper functions that are used in the main code. `utils.py` contains functions that **illustrate how to document functions**.

## docs

Some documentation

## scripts

Scripts that can be used to run specific implementations of the code.

## tests

Carefully written tests to check validity of the code.

## .gitignore

This tells git which files and directories not to track. If we have some huge dataset that we don't want to commit to the remote repo, this would be a good place to specify that.

## LICENSE

This tells others to what extent they are allowed to use our code. The MIT license used here is not particularly restrictive. You may want to talk about this with your group and look at other options that best suit how you want your code to be used.

## pyproject.toml

This is a file that can be used by python to specify details of the project. This comes in handy when we eventaully plan to package our code and make it installable.

## ruff.toml

This is a configuration file for ruff linter and formatter. It specifies the rules that the linter should follow and the formatting style that the formatter should use. [Ruff](https://docs.astral.sh/ruff/) is a linter and formatter that helps maintain a consistent code style across the project.

## .pre-commit-config.yaml

This is a configuration file for pre-commit hooks. Pre-commit hooks are scripts that run before a commit is made. They can be used to check for code style violations, run tests, and perform other checks to ensure that the code being committed is of high quality. [Pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit hooks. The configuration here checks for code formatting using ruff and black, checks for large files, and checks jypter notebooks to strip output cells. Stripping output cells is useful to avoid committing large output files that can bloat the repo size. Hooks can be added or removed as per the project requirements.

## Recommendation

To make life easier in managing your project, I would suggest you [install uv](https://docs.astral.sh/uv/getting-started/installation/). uv makes it easy to initialize the project, create a dedicated environment, manage dependencies, update pyproject.toml, and export dependencies in other file types.
