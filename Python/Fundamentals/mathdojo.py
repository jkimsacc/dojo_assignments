class MathDojo(object):
    """docstring forMathDojo."""
    def __init__(self):
        self.result=0
    def add(self, *num1):
        for i in num1:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
    def subtract(self, *num2):
        for i in num2:
            if type(i) == list or type(i) == tuple: #check if argument is list or tuple
                for k in i: #if yes, look element inside add/subtract value insde
                    self.result -= k
            else:
                self.result -= i
        return self

print MathDojo().add(2).add(2, 5).subtract(3, 2).result
