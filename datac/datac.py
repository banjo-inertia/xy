# -*- coding: utf-8 -*-

class Datac(object):
    """
    Model of 2D data with static parameters

    A `Datac` object is instantiated with the following parameters:

    :param dict params: Static parameters required to initialize the object featuring the ordinate calculator method.
    :param list abscissae: Independent variable also required to initialize object featuring the ordinate calculator method.
    :param str abscissa_name: Dictionary key for the abscissa name.
    :param instancemethod calc_method: Instance method of a class which implements the calculator method used to determine the ordinates of the data.
    """

    def __init__(self, params, abscissae, abscissa_name, calc_method):
        self.params = params
        self.abscissae = abscissae
        self.abscissa_name = abscissa_name
