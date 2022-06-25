# create a Calculator class with a method called add that takes two numbers and returns the sum of the two numbers
# create a new instance of the Calculator class and call the add method with two numbers
# print the result of the add method

class Calculator
    def add(a, b)
       a + b
    end

    def subtract(a, b)
        a - b
    end

    def multiply(a, b)
        a * b
    end

    def divide(a, b)
        a / b
    end
end

calc = Calculator.new
int add = puts calc.add(1, 2)
int subtract = puts calc.subtract(1, 2)
int multiply = puts calc.multiply(1, 2)
int divide = puts calc.divide(1, 2)

print "add result is " + add.to_s + "\n"
print "subtract result is " + subtract.to_s + "\n"
print "multiply result is " + multiply.to_s + "\n"
print "divide result is " + divide.to_s + "\n"

