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

        # Initialize attributes of object.
        # --------------------------------
        # Root name for data and plot.
        self.set_name_root(parser.prog)

        # Location of data.
        if args.data_dir:
            self.data_dir = os.path.abspath(args.data_dir)
        else:
            self.data_dir = os.getcwd()

        # Location of figures.
        if args.plot_dir:
            self.plot_dir = os.path.abspath(args.plot_dir)
        else:
            self.plot_dir = os.getcwd()

        # I first need to see if any data exists.
        os.path.isfile(self.name_root + ".dat")

        # Next, I should load that data and check it to see if it matches the abscissa data I'm using to calculate the output I want. If it doesn't pass the check, I should throw an error and exit.

    def set_name_root(self, name):
        """
        Sets the `name_root` attribute of the `main` object.
        """
        prog_name = os.path.splitext(name)[0]
        self.name_root = self.strip_prog_name(prog_name)

    def strip_prog_name(self, name, prefix="plot", suffix=None):
        """
        Strip off prefix and suffix from the specified name.
        """
        strip_name = name.lstrip(prefix)
        strip_name = strip_name.rstrip(suffix)

        # Remove any underscores if they are there.
        strip_name = strip_name.lstrip("_")
        strip_name = strip_name.rstrip("_")

        return strip_name

    def def_abscissae(self):
        """
        Define the abscissae for the calculation.

        This method should be overloaded by the user. At the end of this method, a call to `gen_abscissae` needs to be made.
        """
        pass

    def def_calc(self, params):
        """
        Define the calculation to be performed to generate the ordinates.

        :param dict params: Dictionary to instantiate the object containing the ordinate calculator method.

        This method should be overloaded by the user. At the end of this method, a call to `calc_data` needs to be made. This method is called by the user-subclassed `main` object on each item in its `data` atrribute. Each item is a dict that comes in with the `params` variable.
        """
        pass

    def gen_abscissae(self, key, abscissae, base_params):
        """
        Provisionally set attrib `data` with abscissae generated from args.

        :param str key: Dictionary key of the abscissa data.
        :param float abscissae: Value of abscissa.
        :param dict base_params: Additional params used to instantiate the object containing the ordinate calculator method.
        """
        pass

    def calc_data(self, key, obj):
        """
        Set ordinate key for all dicts in the `data` attribute.

        :params str key: Method to call from the object which calculates the ordinate.
        :params obj: Object containing the ordinate calculator method.


        """
        pass
