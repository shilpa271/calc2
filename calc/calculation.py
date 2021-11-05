"""This is our calculation base class / Abstract Class"""

class Calculation:
    # pylint: disable=unused-argument,redefined-outer-name,missing-class-docstring,line-too-long,too-few-public-methods
    #contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class

        self.value_a = value_a
        self.value_b = value_b
    # bound to the class and not the instance of the class
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)
