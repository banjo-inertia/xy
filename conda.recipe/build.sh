#!/usr/bin/env bash

# Define version from `datac/version.py`
VERSION=`python -c 'execfile("datac/version.py")
print(__version__)'`

echo $VERSION > __conda_version__.txt

# Install package
$PYTHON setup.py install
