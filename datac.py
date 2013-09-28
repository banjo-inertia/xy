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
        self.set_name_root(parser.prog)
        self.set_data_dir(args.data_dir)
        self.set_plot_dir(args.plot_dir)

        # I first need to see if any data exists.
        os.path.isfile(self.name_root + ".dat")

        # Next, I should load that data and check it to see if it matches the abscissa data I'm using to calculate the output I want. If it doesn't pass the check, I should throw an error and exit.

    def set_name_root(self, name):
        """
        Sets the `name_root` attribute.
        """
        prog_name = os.path.splitext(name)[0]
        self.name_root = self.strip_prog_name(prog_name)

    def set_data_dir(self, loc):
        """
        Sets the `data_dir` attribute, exception if directory doesn't exist
        """
        if loc:
            self.data_dir = os.path.abspath(loc)
        else:
            self.data_dir = os.getcwd()

        if not os.path.exists(self.data_dir):
            raise OSError(0, "Data directory not found", self.data_dir)

    def set_plot_dir(self, loc):
        """
        Sets the `plot_dir` attribute, exception if directory doesn't exist
        """
        if loc:
            self.plot_dir = os.path.abspath(loc)
        else:
            self.plot_dir = os.getcwd()

        if not os.path.exists(self.plot_dir):
            raise OSError(1, "Plot directory not found", self.plot_dir)


    def strip_prog_name(self, name, prefix="plot", suffix=None):
        """
        Strip off prefix and suffix from the specified name.
        """
        if prefix:
            if name.startswith(prefix):
                name = name.lstrip(prefix)

        if suffix:
            if name.endswith(suffix):
                name = name.rstrip(suffix)

        # Remove any underscores if they are there.
        name = name.lstrip("_")
        name = name.rstrip("_")

        return name

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
