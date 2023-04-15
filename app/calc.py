import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    #add
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    #substract
    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    #multiply
    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    #divide
    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    #power
    def power(self, x, y):
        self.check_types(x, y)

        if (x == 0 & y < 0):
            raise TypeError("It's not possible power for base 0 and negative exponent")
        return x ** y
    
    #square_root
    def square_root(self, x):
        self.check_types_single(x)

        if x < 0:
            raise TypeError("It's not possible square root for negative numbers")
        
        return x ** (1/2)
    
    #log base 10
    def log_base_10(self, x):
        self.check_types_single(x)

        if x <= 0:
            raise TypeError("It's not possible log base 10 for negative numbers including zero")
        
        result = math.log10(x)
        return result

    #validators
    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")
    
    def check_types_single(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
