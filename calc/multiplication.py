"""Multiply calculation that is being inherits the value A and value B from the calculation class"""
from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Multiplication(Calculation):
    # pylint: disable=unused-argument,redefined-outer-name,missing-class-docstring,missing-final-newline,line-too-long,missing-function-docstring
    def get_result(self):
        #you need to use self to reference the data contained in the instance of the object.  This is encapsulation
        return self.value_a * self.value_b