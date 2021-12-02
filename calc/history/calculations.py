"""Calculation history Class"""

# pylint: disable=line-too-long.trailing-newlines

class Calculations:
    """Class with fundamental methods to operate calculator"""
    # command pattern
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """counts number of calculations in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """gets latest calculation from user as an object"""
        return Calculations.history[-1]


    @staticmethod
    def get_first_calculation():
        """gets first calculation from user"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """get a specific calculation from history input index"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(inserted_calculation):
        """append calculation from history"""
        return Calculations.history.append(inserted_calculation)

