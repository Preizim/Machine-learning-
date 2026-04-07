import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1,2,3,4,5])
y = np.array([120,150,130,170,160])

# Initialize parameters
m = 0
b = 0
learning_rate = 0.01

# Error function
def compute_error(x, y, m, b):
    y_pred = m * x + b
    return np.mean((y - y_pred) ** 2)

# Training loop
for i in range(1000):
    y_pred = m * x + b
    
    dm = -2 * np.mean(x * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    
    m = m - learning_rate * dm
    b = b - learning_rate * db

    # 👇 Print error every 100 iterations
    if i % 100 == 0:
        error = compute_error(x, y, m, b)
        print(f"Iteration {i}, Error: {error}")

print("Final m:", m)
print("Final b:", b)


# Predictions
y_pred = m * x + b

# Plot
plt.scatter(x, y, label="Real Data")     # actual points
plt.plot(x, y_pred, label="Prediction")  # model line

plt.xlabel("Day")
plt.ylabel("Water Usage")
plt.title("Prediction vs Real Data")

plt.legend()
plt.show()