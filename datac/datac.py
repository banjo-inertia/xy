# -*- coding: utf-8 -*-
import copy
import json
import matplotlib.pyplot as plt
from astropy import units
from numbers import Number


class Datac(object):
    """
    Model of 2D data with static parameters

    A `Datac` object is instantiated with the following parameters:

    :param dict params: Static parameters required to initialize the object featuring the ordinate calculator method.
    :param list abscissae: Independent variable also required to initialize object featuring the ordinate calculator method.
    :param str abscissa_name: Dictionary key for the abscissa name.
    :param instancemethod calc_method: Instance method of a class which implements the calculator method used to determine the ordinates of the data.
    """
    # Many of the object's attributes should be read-only.
    @property
    def params(self):
        return self._params


    @property
    def abscissa_name(self):
        return self._abscissa_name

    @abscissa_name.setter
    def abscissa_name(self, value):
        if self._abscissa_name:
            raise AttributeError("abscissa_name is read-only")
        else:
            if type(abscissa_name) is not str:
                raise TypeError("abscissa_name must be a string")
            self._abscissa_name = value


    @property
    def abscissae(self):
        return self._abscissae

    @abscissae.setter
    def abscissae(self, value):
        if self._abscissae:
            raise AttributeError("abscissae is read-only")
        else:
            try:
                iterator = iter(abscissae)
            except TypeError:
                raise TypeError("abscissae must be iterable")
            self._abscissae = value


    @property
    def calc_method(self):
        return self._calc_method

    @calc_method.setter
    def calc_method(self, value):
        if self._calc_method:
            raise AttributeError("calc_method is read-only")
        else:
            self._calc_method = value


    @property
    def ordinates(self):
        return self._ordinates


    def __init__(self, calc_method, abscissa_name, abscissae, **kwargs):

        self._params = kwargs
        self.abscissae = abscissae
        self.abscissa_name = abscissa_name
        self.calc_method = calc_method

        self._ordinates = self.calc_ordinates()


    def _to_dict(self):
        """
        Map object's data unambiguously to dict

        Data from the object is represented in the dictionary returned by this method according to the following rules.

        * Key/value pairs of the `params` dict SHALL map to key/value pairs in the returned dict.
        * The list stored in the `abscissae` attribute SHALL be stored in the returned dict with key "abscissae".
        * If they exist, the list stored in the `ordinates` attribute SHALL be stored in the returned dict with key "ordinates". Otherwise this field will not appear in the returned dict.
        * The `abscissa_name` attribute SHALL be stored in the returned dict with key "abscissa_name".
        * If the value stored in the object's `calc_method` attribute is not `None`, it SHALL be converted to a string, and that string stored in the returned dict with key "ordinate_name". Otherwise this field will not appear in the returned dict.
        """
        obj_dict = copy.copy(self.params)
        obj_dict["abscissae"] = self.abscissae
        try:
            obj_dict["ordinates"] = self.ordinates
        except:
            pass
        obj_dict["abscissa_name"] = self.abscissa_name
        if self.calc_method:
            obj_dict["ordinate_name"] = str(self.calc_method)

        return obj_dict


    def __iter__(self):
        obj_dict = self._to_dict()
        return obj_dict.iteritems()


    def __repr__(self):
        """
        String representation of object's dictionary representation
        """
        obj_dict = self._to_dict()
        return str(obj_dict)


    def calc_ordinates(self):
        """
        Calculate and add list of ordinates to object
        """
        ordinates_list = []

        for abscissa in self.abscissae:
            # Create dict of params and abscissa to instantiate object which features ordinate calculator method.
            params = copy.copy(self.params)
            params[self.abscissa_name] = abscissa

            # Initialize object, call calculator method.
            try:
                ob = self.calc_method.im_class(params)
            except:
                raise TypeError("Problem calling calc_method")
            ordinate = getattr(ob, self.calc_method.__name__)()

            ordinates_list.append(ordinate)

        ordinates = self._to_array(ordinates_list)

        self._ordinates = ordinates


    def _to_array(self, ordinates_list):
        """
        Convert a list to a numpy array

        :param list ordinates_list: List of ordinate values.

        Examines a list to see if the elements are of type `astropy.units.Quantity`; if so, the method returns a corresponding array-like object which is of type `astropy.units.Quantity`.
        """
        if isinstance(ordinates_list[0], Number):
            return ordinates_list

        if not self._identical_units(ordinates_list):
            error_msg = "ordinates_list does not have consistent units."
            raise ValueError(error_msg)

        values = [ordinate.value for ordinate in ordinates_list]
        unit = ordinates_list[0].unit
        ordinates = units.Quantity(values, unit)

        return ordinates


    def _identical_units(self, ordinates_list):
        """
        Return True if all units in list are consistent

        :param list ordinates_list: List of ordinate values where each element is an `astropy.units.Quantity`.
        """
        return all([ordinate.unit == ordinates_list[0].unit for ordinate in ordinates_list])


    def dump(self, **kwargs):
        """
        Wrapper for json.dump

        It is assumed that `self` is passed to the `obj` argument of `json.dump`.

        :param **kwargs: Arguments passed through to the `json.dump` command.
        """
        json.dump(dict(self), **kwargs)


    def dumps(self, **kwargs):
        """
        Wrapper for json.dumps

        It is assumed that `self` is passed to the `obj` argument of `json.dumps`.

        :param **kwargs: Arguments passed through to the `json.dumps` command.
        """
        return json.dumps(dict(self), **kwargs)


    def plot(self):
        """
        Return matplotlib.figure.Figure plotting abscissae vs. ordinates
        """
        fig = plt.figure()
        plt.plot(self.abscissae, self.ordinates)
        return fig


    def show(self):
        """
        Display simplest abscissae vs. ordinate plot
        """
        fig = self.plot()
        plt.show()


    def savefig(self, *args, **kwargs):
        """
        Wrapper for matplotlib.pyplot.savefig

        Plots abscissae vs ordinates.

        :param *args: Arguments passed through to the `matplotlib.pyplot.savefig` command.
        :param **kwargs: Arguments passed through to the `matplotlib.pyplot.savefig` command.
        """
        self.plot()
        plt.savefig(*args, **kwargs)
