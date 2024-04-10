import matplotlib.pyplot as plt
from sympy import symbols, factorial, lambdify
import numpy as np

# Define symbols for calculations
x, y = symbols('x y')


# Function for Taylor Series Expansion (first differential equation)
def taylorSeriesExpansion():
    initialY = 1
    initialYPrime = -1
    doublePrimeAtZero = 0
    triplePrimeAtZero = -4
    quadruplePrimeAtZero = -6

    # Construct Taylor series up to n=4
    taylorSeries = initialY + initialYPrime * x + (doublePrimeAtZero / factorial(2)) * x ** 2 + \
                   (triplePrimeAtZero / factorial(3)) * x ** 3 + (quadruplePrimeAtZero / factorial(4)) * x ** 4

    return taylorSeries


# Function for Second-order Taylor Polynomial (second differential equation)
def secondOrderTaylorPolynomial():
    initialYAtThree = 6
    initialYPrimeAtThree = 1
    doublePrimeAtThree = -1
    x0 = 3

    # Construct the polynomial
    secondOrderTaylor = initialYAtThree + initialYPrimeAtThree * (x - x0) + \
                        (doublePrimeAtThree / factorial(2)) * (x - x0) ** 2

    return secondOrderTaylor


# Plotting function
def plotFunction(function, xRange, title):
    # Convert sympy expression to a function that can be used by numpy
    func = lambdify(x, function, modules=['numpy'])

    # Generate x values
    xValues = np.linspace(xRange[0], xRange[1], 400)
    # Calculate y values
    yValues = func(xValues)

    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(xValues, yValues, label=str(function))
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Taylor Series Expansion plot
plotFunction(taylorSeriesExpansion(), (0, 5), 'Taylor Series Expansion at x=3.5')

# Second-order Taylor Polynomial plot
plotFunction(secondOrderTaylorPolynomial(), (2, 4), 'Second-order Taylor Polynomial near x=3')
