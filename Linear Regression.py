import numpy as np


def linear_regression(X, y):
    # Calculate the mean of X and y
    mean_x = np.mean(X)
    mean_y = np.mean(y)

    # Calculate the differences from the mean
    diff_x = X - mean_x
    diff_y = y - mean_y

    # Calculate the slope (coefficient)
    slope = np.sum(diff_x * diff_y) / np.sum(diff_x ** 2)

    # Calculate the intercept
    intercept = mean_y - slope * mean_x

    return slope, intercept


# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Perform linear regression
slope, intercept = linear_regression(X, y)

# Print the slope and intercept
print("Slope (Coefficient):", slope)
print("Intercept:", intercept)

# Make predictions
X_new = np.array([6, 7, 8])
y_pred = slope * X_new + intercept
print("Predicted values for X_new:", y_pred)
