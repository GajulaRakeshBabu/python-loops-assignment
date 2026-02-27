import numpy as np
import time

temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
avg_fahrenheit = np.mean(temps_fahrenheit)

print("Task 1:")
print("Temperatures in Celsius:", temps_celsius)
print("Temperatures in Fahrenheit:", temps_fahrenheit)
print("Average temperature in Fahrenheit:", round(avg_fahrenheit, 1))
print()

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Task 2:")
print("Scores array shape:", scores.shape)
print("Total number of scores:", scores.size)
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))
print("Score range:", np.max(scores) - np.min(scores))
print()

nums_np = np.arange(1, 50001)
nums_list = list(range(1, 50001))

start_np = time.time()
sum_np = np.sum(nums_np)
end_np = time.time()
time_np = end_np - start_np

start_list = time.time()
sum_list = sum(nums_list)
end_list = time.time()
time_list = end_list - start_list

print("Task 3:")
print("NumPy sum:", sum_np)
print("Python list sum:", sum_list)
print("NumPy time (seconds):", f"{time_np:.4f}")
print("Python list time (seconds):", f"{time_list:.4f}")
if time_np > 0:
    speedup = time_list / time_np
    print("NumPy is", round(speedup, 4), "times faster")