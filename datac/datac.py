# -*- coding: utf-8 -*-
import copy


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
        self.calc_method = calc_method

        self.generate_ordinates()
        

    def generate_ordinates(self):
        """
        Calculate and add list of ordinates to object
        """
        ordinates = []

        for abscissa in self.abscissae:
            # Create dict of params and abscissa to instantiate object which features ordinate calculator method.
            params = copy.copy(self.params)
            params[self.abscissa_name] = abscissa

            # Initialize object, call calculator method.
            ob = self.calc_method.im_class(params)
            ordinate = getattr(ob, self.calc_method.__name__)()

            ordinates.append(ordinate)

        self.ordinates = ordinates
