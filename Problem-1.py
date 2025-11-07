class Calculator:
    def __init__(self,a,b,op):
        self.a=a
        self.b=b
        self.op=op
    def calculate(self):
        if self.op=="add":
            return self.a+self.b
        elif self.op=="sub":
            return self.a-self.b
        elif self.op=="multiply":
            return self.a*self.b
        elif self.op=="divide":
            return "Error:Cannot be divided by zero" if self.b==0 else self.a/self.b
        else:
            return "Invalid operation"
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
op=input("Enter operation(add/sub/multiply/divide):")
obj=Calculator(a,b,op)
print("Result",obj.calculate())