""" division calculation that is being inherits the value A and value B from the calculation class"""
from calc.calculation import Calculation

#This is how you extend the division class with the Calculation
class Division(Calculation):
    # pylint: disable=unused-argument,redefined-outer-name,missing-function-docstring,line-too-long
    """The division class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_result(self):
        #you need to use self to reference the data contained in the instance of the object.  This is encapsulation
        return self.value_a / self.value_b
