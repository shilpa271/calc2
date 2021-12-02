"""Multiplication Class"""
from calc.calculations.calculation import Calculation
# pylint: disable=missing-final-newline,missing-function-docstring
class Multiplication(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
