# -*- coding: utf-8 -*-
import collections
import matplotlib.pyplot as plt


class Datac(collections.Sequence):
    """
    Model of 2D data with static parameters
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
        if hasattr(self, "_abscissa_name"):
            raise AttributeError("abscissa_name is read-only")
        else:
            if type(value) is not str:
                raise TypeError("abscissa_name must be a string")
            self._abscissa_name = value


    @property
    def abscissae(self):
        return self._abscissae

    @abscissae.setter
    def abscissae(self, value):
        if hasattr(self, "_abscissae"):
            raise AttributeError("abscissae is read-only")
        else:
            try:
                iterator = iter(value)
            except TypeError:
                raise TypeError("abscissae must be iterable")
            self._abscissae = value


    @property
    def calc_method(self):
        return self._calc_method

    @calc_method.setter
    def calc_method(self, value):
        if hasattr(self, "_calc_method"):
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

    def __getitem__(self, index):
        val = self.params.copy()
        val.update({self.abscissa_name: self.abscissae[index]})
        if hasattr(self, "_ordinates"):
            val.update({self.calc_method.__name__: self.ordinates[index]})

        return val

    def __len__(self):
        return len(self.abscissae)

    def __repr__(self):
        # Construct a dict containing enough values to specify this object
        params_repr = self._params_repr()

        obj_data = {"class": self.__class__.__name__,
            "params": params_repr,
            "calc_method": self.calc_method,
            "abscissae": self.abscissae,
            "ordinates": self.ordinates, }
        rep = "%(class)s(%(params)s, calc_method=%(calc_method)r, abscissae=%(abscissae)r, ordinates=%(ordinates)r)" % obj_data
        return rep

    def _params_repr(self):
        """
        Format self.params for self.__repr__

        The dict stored in self.params need to be output with __repr__. I don't want to simply dump the self.params dict; I want the keys and values to look like "key=val" at the beginning of __repr__. Therefore, I need to construct a string out of these pairs. 
        """
        params_slug = "{0!s}={1!r}"
        params_repr = ", ".join([params_slug.format(key, val) for key, val in self.params.items()])
        return params_repr


    def _calc_ordinates(self):
        """
        Calculate and add list of ordinates to object
        """
        try:
            ordinates = [self.calc_method(**abscissae_dict) for abscissae_dict in self]
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
