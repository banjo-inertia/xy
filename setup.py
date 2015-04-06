# -*- coding: utf-8 -*-
from setuptools import setup
execfile("datac/version.py")

setup(name="datac",
    version=__version__,
    author="Joshua Ryan Smith",
    author_email="joshua.r.smith@gmail.com",
    packages=["datac"],
    url="https://github.com/jrsmith3/datac",
    description="Utility for managing 2D data",
    classifiers=["Programming Language :: Python",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Development Status :: 3 - Alpha",
                 "Intended Audience :: Science/Research",
                 "Topic :: Utilities",
                 "Natural Language :: English", ],
    install_requires=[], )
