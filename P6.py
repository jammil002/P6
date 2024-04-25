import numpy as np
import matplotlib.pyplot as plt
import math
from fractions import Fraction


# Define the function for the linear Taylor polynomial
def taylorSeriesLinear(x):
    return 6 + (x - 3)


# Define the function for the exponential Taylor series
def taylorSeriesExponential(x, termsCount):
    result = 1
    for i in range(1, termsCount + 1):
        result -= x ** i / math.factorial(i)
    return result


# Define the function for calculating coefficients using a recursive formula
def calculateCoefficients(termLimit):
    coefficients = [Fraction(1, 1), Fraction(1, 1)]  # Starting values for a0, a1 as Fractions
    for n in range(2, termLimit + 1):
        numerator = -1 * (n * (n - 1) + 1)
        denominator = 4 * (n + 2) * (n + 1)
        coefficient = Fraction(numerator, denominator).limit_denominator()
        coefficient *= coefficients[n - 2]  # Recursive relation
        coefficients.append(coefficient)
    # Convert all coefficients to tuple
    return [coef.as_integer_ratio() for coef in coefficients]


# Plot for Linear Taylor Polynomial
xValuesLinear = np.linspace(2.5, 3.5, 100)
yValuesLinear = taylorSeriesLinear(xValuesLinear)
plt.figure(figsize=(10, 6))
plt.plot(xValuesLinear, yValuesLinear, label='Linear Taylor Polynomial', color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Taylor Polynomial near x=3')
plt.legend()
plt.grid(True)
plt.show()

# Plot for True Function vs Taylor Series Approximation
xValuesExp = np.linspace(-1, 4, 400)
yTrue = 1 - xValuesExp
yTaylorExp = taylorSeriesExponential(xValuesExp, 4)
plt.figure(figsize=(10, 6))
plt.plot(xValuesExp, yTrue, label='True Function (1-x)', color='green')
plt.plot(xValuesExp, yTaylorExp, label='Taylor Series Approximation (n=4)', linestyle='--', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('True Function vs Taylor Series Approximation')
plt.legend()
plt.grid(True)
plt.show()

# Plot for Recursive Coefficient Function and Polynomial Sum
initialValues = [1, 1]  # a0, a1
coefficients = calculateCoefficients(8)
x = np.linspace(0, 10, 100)
y_terms = []
for n, coef in enumerate(coefficients):
    num, denom = coef  # Unpack coefficient
    term = (num / denom) * x ** n
    if n % 2 == 0:
        term *= initialValues[0]
    else:
        term *= initialValues[1]
    y_terms.append(term)
y_sum = sum(y_terms)
plt.plot(x, y_sum, color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of General Solution using Recursive Coefficients')
plt.grid(True)
plt.show()
