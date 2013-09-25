# -*- coding: utf-8 -*-
"""
Perform an action on a 2D set of data.
"""

import os
import logging
import optparse


def main():
    """
    Method that always gets executed when program is run.
    """

    usage = "usage: %prog [options] remotes_dir"
    parser = optparse.OptionParser()

    parser.add_option("--clobber",
                      help="Recalculate then mercilessly overwrite existing data.")

    parser.add_option("--data-dir",
                      help="Directory in which to look for existing data/write new data [./].")

    parser.add_option("--nodisplay",
                      help="Don't display the plot onscreen before writing it.")

    parser.add_option("--plot-dir",
                      help="Directory in which to write plot image file [./].")

    parser.add_option("--plot-type",
                      help="Extension indicating the type of image file to be written [eps].")

    (options, args) = parser.parse_args()

    # I first need to see if any data exists.

    # Next, I should load that data and check it to see if it matches the abscissa data I'm using to calculate the output I want. If it doesn't pass the check, I should throw an error and exit.


    # if options.remotes_dir:
    #     remotes = git_remotes_list(args[0])

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
