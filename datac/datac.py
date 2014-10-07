# -*- coding: utf-8 -*-
import copy
import json
import matplotlib.pyplot as plt


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
    def abscissae(self):
        return self._abscissae

    @property
    def abscissa_name(self):
        return self._abscissa_name

    @property
    def ordinates(self):
        return self._ordinates

    # Setting the `calc_method` attribute is valid if it wasn't set during instantiation. However, the `calc_method` property has set-once behavior.
    @property
    def calc_method(self):
        return self._calc_method

    @calc_method.setter
    def calc_method(self, value):
        if self._calc_method:
            raise AttributeError("calc_method cannot be changed once it has been set")
        else:
            self._calc_method = value
            self.calc_ordinates()
        

    def __init__(self, params, abscissae, abscissa_name, calc_method = None):

        # Type checking on the way in
        # params
        if type(params) is not dict:
            raise TypeError("params must be a dict")

        # abscissae
        if type(abscissae) is str:
            raise TypeError("abscissae cannot be a string")
        try:
            iterator = iter(abscissae)
        except TypeError:
            raise TypeError("abscissae must be iterable")

        # abscissa_name
        if type(abscissa_name) is not str:
            raise TypeError("abscissa_name must be a string")

        self._params = params
        self._abscissae = abscissae
        self._abscissa_name = abscissa_name
        self._calc_method = calc_method

        if calc_method:
            self.calc_ordinates()


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
        ordinates = []

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

            ordinates.append(ordinate)

        self._ordinates = ordinates


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
