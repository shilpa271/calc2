"""Calculation history Class"""
from calc.calculations import addition
from calc.calculations import multiplication
from calc.calculations import subtraction
from calc.calculations import division

class Calculations:
    # pylint: disable=missing-class-docstring
    history = []
    # pylint: disable=too-few-public-methods,missing-class-docstring,missing-function-docstring,
    @staticmethod
    def clear_history():
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(addition.create(values))
        #Get the result of the calculation
        return Calculations.get_last_calculation_object()
    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(subtraction.create(values))
        return Calculations.get_last_calculation_object()
    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(multiplication.create(values))
        return Calculations.get_last_calculation_object()
    @staticmethod
    def add_division_calculation(values):
        """ Create a division object to history using factory method create"""
        Calculations.add_calculation(division.create(values))
        return Calculations.get_last_calculation_object()