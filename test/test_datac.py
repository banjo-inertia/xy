# -*- coding: utf-8 -*-
import datac
import numpy as np
import os
import unittest

class dummyclass(object):
    """
    Simple class for testing `generate_ordinates`
    """
    def __init__(self, params):
        pass

    def fun(self):
        """
        Return value of `True`
        """
        return True


params = {"temp_sun": 6000.}
bandgaps = np.linspace(0, 3.25, 100)

abscissae = datac.generate_abscissae(bandgaps, "bandgap", params)
data = datac.generate_ordinates(abscissae, dummyclass, "fun")
