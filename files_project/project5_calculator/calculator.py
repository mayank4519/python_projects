from addition import Addition

class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def multiply(cls, num1, num2):
        total = 0
        for i in range(0, num2):
            total = cls.add(total, num1)
        return total

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)

    @classmethod
    def divide(cls, num1, num2):
        pass

cal = Calculator()
print(f"multiply = {cal.multiply(2, 5)}, subtract = {cal.subtract(5,3)}")