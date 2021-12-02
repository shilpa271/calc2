"""Calculation Class"""
class Calculation:
    """ calculation abstract base class"""
    # pylint: disable=too-few-public-methods,missing-final-newline,trailing-newlines
    def __init__(self, values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(values)
    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)

