# -*- coding: utf-8 -*-
"""
Perform an action on a 2D set of data.
"""

import os
import logging
import argparse
import copy


class main():
    """
    Class that always gets instantiated when program is run.

    Attributes
    ----------
    name_root: Name of the calling script stripped of the filename extension and 'plot' or 'plot_' prefix. E.g., if the name of the script is 'plot_fig01.py', name_root is 'fig01'.
    data_dir: Directory in which data is located/to be written.
    plot_dir: Directory in which the plot image file is to be written.
    data: List of dicts containing the abscissae, ordinates, and fixed terms used calculate the ordinates.
    abscissa_key: Key in each dict of self.data corresponding to the abscissa.
    ordinate_key: Key in each dict of self.data corresponding to the ordinate.
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

        # Generate or load the data and set self.data
        # -------------------------------------------
        data_filename = os.path.join(self.data_dir, 
            self.name_root + ".dat")
        my_abscissae = self.gen_abscissae()

        if os.path.isfile(data_filename):
            # Load data from data_filename.
            file_data = self.read_data(data_filename)
            # Compare abscissae in data_filename to my_abscissae.
            # Throw exception and exit if the abscissae don't match.
            self.compare_abscissae(my_abscissae, file_data)
            if args.clobber:
                # Execute calculator method using my_abscissae.
                my_data = self.calc_data(my_abscissae)
                # Set self.data using the data just calculated.
                self.set_data(my_data)
            else:
                # Set self.data using the data loaded from the file.
                self.set_data(file_data)
        else:
            # Execute calculator method using my_abscissae.
            my_data = self.calc_data(my_abscissae)
            # Set self.data using the data just calculated.
            self.set_data(my_data)

        # Record the names of the abscissa and ordinate.
        self.set_abscissa_key()
        self.set_ordinate_key()

        # Write data to file (if it wasn't just read from a file)
        # -------------------------------------------------------
        if args.clobber:
            self.write_data(self.data, data_filename)
        elif not os.path.isfile(data_filename):
            self.write_data(self.data, data_filename)

        # Generate the plot and display it on screen
        # ------------------------------------------
        if not args.nodisplay:
            self.plot_data(self.data)

        # Write the plot image to a file
        # ------------------------------
        self.write_plot(self.plot_dir, self.data, args.plot_type)


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

    def set_data(data):
        """
        Sets `data` attribute.
        """
        self.data = data


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

        The user overloads this method to define the abscissae for the calculation. The user must overload this method to return a tuple with three items (abscissae, base_params, key) in order for the class to generate the list of dictionaries. 
        * abscissae: An iteratable object, such as a numpy array, that contains the abscissae.
        * base_params: A dictionary that, along with an item from the iteratable object above, can be used to instantiate an object of the class that contains the desired ordinate calculator method.
        * key: A string defining a key in the dictionary above, which corresponds to the abscissa data.
        """
        pass

    def def_calc(self, params):
        """
        Define the calculation to be performed to generate the ordinates.

        :param dict params: Dictionary to instantiate the object containing the ordinate calculator method.

        The user overloads this method to define the calculation to be performed on each item of the object's list of dictionaries. The user must overload this method to return a tuple with two items (calculator_obj, calculator_method).
        * calculator_obj: An object with the desired ordinate calculator method.
        * calculator_method: A string with the name of the desired calculator method of the object defined above. This string will also be used as a key in the dict storing the data.
        """
        pass

    def gen_abscissae(self, abscissae, base_params, key):
        """
        Return a list of dicts representing abscissae.

        :param float abscissae: Value of abscissa.
        :param dict base_params: Additional params used to instantiate the object containing the ordinate calculator method.
        :param str key: Dictionary key of the abscissa data.
        """
        # Probably should be using a list comprehension here.
        data = []
        for abscissa in abscissae:
            abscissa_dict = copy.copy(base_params)
            abscissa_dict[key] = abscissa
            data.append(abscissa_dict)

        return data

    def calc_data(self):
        """
        Return a list of dicts including both abscissae and ordinates.
        """
        # Probably should use list comprehensions here, too.
        data = []
        for params in self.data:
            ordinate_dict = copy.copy(params)
            obj, calc_method = self.def_calc(ordinate_dict)
            ordinate_dict[calc_method] = getattr(obj, calc_method)()
            data.append(ordinate_dict)

        return data

    def read_data(self, data_filename):
        """
        Returns data read from a file.

        :param str data_filename: Full path to the data file.
        """
        data_file = open(data_filename, "r")
        data = json.load(data_file)
        data_file.close()

        # Is data a list of dicts?

        return data

    def write_data(self, data, data_filename):
        """
        Write data to a file.

        :param np.ndarray data: Data to write to the file.
        :param str data_filename: Full path to the data file.
        """
        data_file = open(data_filename, "w")
        json.dump(data, data_file)
        data_file.close()

    def compare_abscissae(self, abscissae, full_data):
        """
        Return True if each item in abscissae is a subdict of full_data

        :param dict abscissae: List of dicts containing only abscissa and terms (no ordinates) used to instantiate the object with the desired calculator method.
        :param dict full_data: List of dicts containing abscissa, terms, and ordinates.
        """
        # At this point, I'm assuming full_data is a legitimate data set: its a list of dicts.

        if len(abscissae) != len(full_data):
            # The following exception should be more specific, i.e. I shouldn't just be using some generic parent class exception.
            raise Exception("Data from file isn't the same length list as the specified abscissae.")

        # I also assume that all the dicts in both list have the same keys. Therefore, if the keys of abscissae aren't a subset of the keys of full_data, an exception should be raised and the program should exit.

        if set(abscissa[0].keys()) <= set(full_data[0].keys()):
            # Again, I need a real exception.
            raise Exception("Data from file doesn't have the same abscissa/terms as the specified abscissae.")

        for abscissa, full_datum in zip(abscissae, full_data):
            for key in abscissa.keys():
                if abscissa[key] != full_datum[key]:
                    # Again, use a real exception.
                    raise Exception("Abscissa or terms from file is not equal to the abscissa or terms from the specified abscissae.")
