# -*- coding: utf-8 -*-
import copy


def init_abscissa(abscissae, abscissa_name, params = {}):
    """
    List of dicts to initialize object w/ calc method

    This method generates a list of dicts; each dict is sufficient to initialize an object featuring a calculator method of interest. This list can be thought of as the abscissae of a set of data. Each dict will contain data which remains constant for each calculation, but it nonetheless required to initialize the object. Each dict will also contain a datum which is the abscissa for the calculation and is also required to initialize the object.

    :param dict params: Static parameters required to initialize the object featuring the ordinate calculator method.
    :param list abscissae: Independent variable also required to initialize object featuring the ordinate calculator method.
    :param str abscissa_name: Dictionary key for the abscissa name.
    """
    dict_list = []

    for abscissa in abscissae:
        param_dict = copy.copy(params)
        param_dict[abscissa_name] = abscissa
        param_dict["abscissa_name"] = abscissa_name
        dict_list.append(param_dict)

    return dict_list


def ordinate_list(class_name, method_name, abscissae):
    """
    List of dicts including abscissa and ordinate data

    This method generates a list of dicts which include an ordinate, abscissa, and any other static data required to perform the calculation to generate the ordinate.

    :param string class_name: Class featuring ordinate generating calculator method.
    :param string method_name: Name of method used to calculate the ordinate.
    :param list abscissae: List of dicts required to initialize an object containing the desired calculator method.
    """
    dict_list = []

    for params in abscissae:
        param_dict = copy.copy(params)
        # Code to generate and add ordinate to `param_dict`
        param_dict["ordinate_name"] = method_name
        dict_list.append(param_dict)

    return dict_list
