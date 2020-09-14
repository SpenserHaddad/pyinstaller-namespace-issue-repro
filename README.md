# pyinstaller-namespace-issue-repro
Demonstrate issue using namespace packages in PyInstaller

PyInstaller 4.0 has an issue where namespace packages are not distinguished
from regular packages, so using them to dynamically add packages ([as described
in the guide on PyPA](https://packaging.python.org/guides/packaging-namespace-packages/))
fails. The namespace packages are not visible when dynamically querying them.

This repo provides a minimal example showing the issue. It provides two
sub-packages under a single namespace, and a third module that loads the two in
and prints a common function between them. Running `run.py` as a Python script
will print both module's output. However, creating an .exe using PyInstaller
and running that will give no output, as the program will not be able to find
the namespaces.

# Setup
```bash
# Install dependencies, modules and submodules
$ pip install -r requirements.txt
$ pip install .
$ pip install submod_a/
$ pip install submod_b/

# Run as Python script (w/ found output)
$ python run.py

# Print namespace package...
# <module 'subpackages' (namespace)>
# Print submodule data...
# Hello from submodule A!!!
# Hello from submodule B!!!
# Print submod_b output...
# Hello from submodule B!!!

# Create and run PyInstaller executable (w/ found output)
$ pyinstaller --clean --onedir --noupx --noconfirm -n pyi_ns_issue run.py
$ dist/pyi_ns_issue 

# Print namespace package...
# <module 'subpackages' from '/home/spenser/pyinstaller-namespace-issue-repro/dist/pyi_ns_issue/subpackages/__init__.pyc'>
# Print submodule data...
# Print submod_b output...
# Hello from submodule B!!!
