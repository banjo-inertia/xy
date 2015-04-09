# -*- coding: utf-8 -*-
import unittest
import datac
import numpy as np

# Some control data and function for the purposes of testing.
params = {"width": 2., "depth": 3.}
abscissa_name = "height"
abscissae = np.linspace(1., 10., 100)

def cuboid_volume(height, width, depth):
    """
    Return volume of cuboid
    """
    vol = height * width * depth

    return vol


class Instantiation(unittest.TestCase):
    """
    Test instantiation works according to spec
    """
    def test_calc_method_non_function(self):
        """
        `calc_method` must be a function
        """
        not_a_function = "this is a string."
        self.assertRaises(TypeError, datac.Datac, not_a_function, abscissa_name, abscissae, **params)

    def test_abscissa_name_non_string(self):
        """
        Datac instantiation should fail if abscissa_name is not a string
        """
        self.assertRaises(TypeError, datac.Datac, params, abscissae, None)

    def test_abscissae_non_iterable(self):
        """
        Datac instantiation should fail if abscissae is not iterable
        """
        self.assertRaises(TypeError, datac.Datac, params, None, abscissa_name)

class API(unittest.TestCase):
    """
    Test API behaves
    """
    def setUp(self):
        """
        Create a Datac object for testing
        """
        self.test_obj = datac.Datac(cuboid_volume, abscissa_name, abscissae, **params)

    def tearDown(self):
        """
        Destroy the test Datac object
        """
        del self.test_obj

    def test_params_read_only(self):
        """
        The params attribute should be read-only
        """
        legit_params = {"one": 1.}

        self.assertRaises(AttributeError, setattr, self.test_obj, "params", legit_params)

    def test_abscissae_read_only(self):
        """
        The abscissae attribute should be read-only
        """
        legit_abscissae = [3, 4]

        self.assertRaises(AttributeError, setattr, self.test_obj, "abscissae", legit_abscissae)

    def test_abscissa_name_read_only(self):
        """
        The abscissa_name attribute should be read-only
        """
        legit_abscissa_name = "legit"

        self.assertRaises(AttributeError, setattr, self.test_obj, "abscissa_name", legit_abscissa_name)

    def test_ordinates_read_only(self):
        """
        The ordinates attribute should be read-only
        """
        legit_ordinates = [1, 2]

        self.assertRaises(AttributeError, setattr, self.test_obj, "ordinates", legit_ordinates)

    def test_calc_method_read_only(self):
        """
        calc_method should be read-only
        """
        self.assertRaises(AttributeError, setattr, self.test_obj, "calc_method", cuboid_volume)
