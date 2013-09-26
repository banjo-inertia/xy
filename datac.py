#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Perform an action on a 2D set of data.
"""

import os
import logging
import argparse


def main():
    """
    Method that always gets executed when program is run.
    """

    parser = argparse.ArgumentParser(description='Perform an action on a 2D set of data.')

    parser.add_argument("-c","--clobber",
                      help="Recalculate then mercilessly overwrite existing data.",
                      action="store_true")

    parser.add_argument("--data-dir",
                      help="Directory in which to look for existing data/write new data (default: current directory).")

    parser.add_argument("-n","--nodisplay",
                      help="Don't display the plot on-screen before writing it.",
                      action="store_true")

    parser.add_argument("--plot-dir",
                      help="Directory in which to write plot image file (default: current directory).")

    parser.add_argument("-t","--plot-type",
                      help="Extension indicating the type of image file to be written (default: eps).",
                      default="eps")

    args = parser.parse_args()


    # I first need to see if any data exists.

    # Next, I should load that data and check it to see if it matches the abscissa data I'm using to calculate the output I want. If it doesn't pass the check, I should throw an error and exit.


def get_program_filename():
    """
    Return the name of the program currently being executed.
    """
    pass

def get_name_root(name, prefix="plot", suffix=None):
    """
    Strip off prefix and suffix from the specified name.
    """
    pass

if __name__ == "__main__":
    main()