# -*- coding: utf-8 -*-
"""
Perform an action on a 2D set of data.
"""

import os
import logging
import argparse


class main():
    """
    Class that always gets instantiated when program is run.
    """

    def __init__(self):

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

        # Set up some data I'll need
        self.name_root = get_name_root(os.path.splitext(parser.prog)[0])

        # I first need to see if any data exists.
        


        # Next, I should load that data and check it to see if it matches the abscissa data I'm using to calculate the output I want. If it doesn't pass the check, I should throw an error and exit.

    def get_name_root(name, prefix="plot", suffix=None):
        """
        Strip off prefix and suffix from the specified name.
        """
        strip_name = name.lstrip(prefix)
        strip_name = strip_name.rstrip(suffix)

        # Remove any underscores if they are there.
        strip_name = strip_name.lstrip("_")
        strip_name = strip_name.rstrip("_")

        return strip_name

    def gen_abscissae(self):
        """
        Return the list of dicts used to instantiate objects.

        This method should be overloaded by the user to generate the abscissae.
        """
        pass
