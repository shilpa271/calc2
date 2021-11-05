"""Subtract two numbers"""
from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Subtraction(Calculation):
    # pylint: disable=unused-argument,redefined-outer-name,missing-class-docstring,line-too-long,too-few-public-methods
    def get_result(self):
        #you need to use self to reference the data contained in the instance of the object.  This is encapsulation
        return self.value_a - self.value_b
