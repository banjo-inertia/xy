# -*- coding: utf-8 -*-
import unittest
import datac

class Instantiation(unittest.TestCase):
    """
    Test instantiation works according to spec
    """
    def test_params_non_dict(self):
        """
        Datac instantiation should fail is params is not a dict
        """
        params = None
        abscissae = [1,2]
        abscissa_name = "abscissa"

        self.assertRaises(TypeError, datac.Datac, params, abscissae, abscissa_name)

    def test_abscissae_non_iterable(self):
        """
        Datac instantiation should fail if abscissae is not iterable
        """
        params = {"fake": 1.}
        abscissae = None
        abscissa_name = "abscissa"

        self.assertRaises(TypeError, datac.Datac, params, abscissae, abscissa_name)

    def test_abscissae_string(self):
        """
        Datac instantiation should fail if abscissae is a string
        """
        params = {"fake": 1.}
        abscissae = "a string!"
        abscissa_name = "abscissa"

        self.assertRaises(TypeError, datac.Datac, params, abscissae, abscissa_name)

    def test_abscissae_name_non_string(self):
        """
        Datac instantiation should fail if abscissae_name is not a string
        """
        params = {"fake": 1.}
        abscissae = [1, 2]
        abscissa_name = None

        self.assertRaises(TypeError, datac.Datac, params, abscissae, abscissa_name)
