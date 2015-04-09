# -*- coding: utf-8 -*-
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

        self._ordinates = self._calc_ordinates()


    def _calc_ordinates(self):
        """
        Calculate and add list of ordinates to object
        """
        # Decompose the params into (key, val) tuples and generate a
        # list of dicts used to instantiate the object defined by 
        # `calc_method`. The following could be done in one line, but
        # I split it for clarity.
        params_items = self.params.items()
        abscissae_dicts = [dict(params_items + [(self.abscissa_name, abscissa)]) for abscissa in self.abscissae]

        try:
            ordinates = [self.calc_method(**abscissae_dict) for abscissae_dict in abscissae_dicts]
        except:
            raise TypeError("Problem calling calc_method")

        return ordinates


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
