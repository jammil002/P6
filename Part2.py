import numpy as np
import matplotlib.pyplot as plt


# Define the system of differential equations
def derivativeY(x, y, velocity):
    return velocity


def derivativeVelocity(x, y, velocity):
    return (x - y) / (x ** 2 + 4)


# Runge-Kutta 4th Order Method to solve ODEs
def rungeKutta4(xStart, yStart, velocityStart, xEnd, steps):
    # Initialize arrays for x, y, and velocity
    xValues = np.linspace(xStart, xEnd, steps + 1)
    yValues = np.zeros(steps + 1)
    velocityValues = np.zeros(steps + 1)

    yValues[0], velocityValues[0] = yStart, velocityStart
    stepSize = (xEnd - xStart) / steps

    # Iterate through all steps
    for i in range(1, steps + 1):
        k1Y = stepSize * derivativeY(xValues[i - 1], yValues[i - 1], velocityValues[i - 1])
        k1Velocity = stepSize * derivativeVelocity(xValues[i - 1], yValues[i - 1], velocityValues[i - 1])

        k2Y = stepSize * derivativeY(xValues[i - 1] + stepSize / 2, yValues[i - 1] + k1Y / 2,
                                     velocityValues[i - 1] + k1Velocity / 2)
        k2Velocity = stepSize * derivativeVelocity(xValues[i - 1] + stepSize / 2, yValues[i - 1] + k1Y / 2,
                                                   velocityValues[i - 1] + k1Velocity / 2)

        k3Y = stepSize * derivativeY(xValues[i - 1] + stepSize / 2, yValues[i - 1] + k2Y / 2,
                                     velocityValues[i - 1] + k2Velocity / 2)
        k3Velocity = stepSize * derivativeVelocity(xValues[i - 1] + stepSize / 2, yValues[i - 1] + k2Y / 2,
                                                   velocityValues[i - 1] + k2Velocity / 2)

        k4Y = stepSize * derivativeY(xValues[i - 1] + stepSize, yValues[i - 1] + k3Y,
                                     velocityValues[i - 1] + k3Velocity)
        k4Velocity = stepSize * derivativeVelocity(xValues[i - 1] + stepSize, yValues[i - 1] + k3Y,
                                                   velocityValues[i - 1] + k3Velocity)

        yValues[i] = yValues[i - 1] + (k1Y + 2 * k2Y + 2 * k3Y + k4Y) / 6
        velocityValues[i] = velocityValues[i - 1] + (k1Velocity + 2 * k2Velocity + 2 * k3Velocity + k4Velocity) / 6

    return xValues, yValues


# Initial conditions and parameters
xStart, yStart, velocityStart = 0, 0, 1  # Initial conditions: y(0) = 0, y'(0) = 1
xEnd, steps = 2, 100  # Final x value and number of steps

# Solve the ODE
xValues, yValues = rungeKutta4(xStart, yStart, velocityStart, xEnd, steps)

# Plot the solution
plt.plot(xValues, yValues, label='Approx. Solution of ODE')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Numerical Solution of Differential Equation')
plt.legend()
plt.grid(True)
plt.show()
