# -*- coding: utf-8 -*-
import unittest
import datac

params = {"slope": 2.,
          "y_intercept": 1.}
abscissae = [1, 2]
abscissa_name = "abscissa"


class Test_Class(object):
    """
    Dummy class to test Datac functionality

    Implements a line.
    """
    def __init__(self, params):
        self.slope = params["slope"]
        self.y_intercept = params["y_intercept"]
        self.abscissa = params["abscissa"]

    def calc_method(self):
        """
        Calculator method
        """
        return self.slope * self.abscissa + self.y_intercept


class Instantiation(unittest.TestCase):
    """
    Test instantiation works according to spec
    """
    def test_params_non_dict(self):
        """
        Datac instantiation should fail is params is not a dict
        """
        self.assertRaises(TypeError, datac.Datac, None, abscissae, abscissa_name)

    def test_abscissae_non_iterable(self):
        """
        Datac instantiation should fail if abscissae is not iterable
        """
        self.assertRaises(TypeError, datac.Datac, params, None, abscissa_name)

    def test_abscissae_string(self):
        """
        Datac instantiation should fail if abscissae is a string
        """
        self.assertRaises(TypeError, datac.Datac, params, "string", abscissa_name)

    def test_abscissa_name_non_string(self):
        """
        Datac instantiation should fail if abscissa_name is not a string
        """
        self.assertRaises(TypeError, datac.Datac, params, abscissae, None)

    def test_ordinates_exist_with_calc_method(self):
        """
        Datac ordinates property should exist if object instantiated with calc_method
        """
        test_obj = datac.Datac(params, abscissae, abscissa_name, Test_Class.calc_method)
        try:
            test_obj.ordinates
        except AttributeError:
            self.fail("Datac ordinates property should exist")


class API(unittest.TestCase):
    """
    Test API behaves
    """
    def setUp(self):
        """
        Create a Datac object for testing
        """
        self.test_obj = datac.Datac(params, abscissae, abscissa_name)

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
        legit_ordinates = [1,2]

        self.assertRaises(AttributeError, setattr, self.test_obj, "ordinates", legit_ordinates)


if __name__ == "__main__":
    test_obj = datac.Datac(params, abscissae, abscissa_name)
