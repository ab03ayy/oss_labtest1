import numpy as np
import matplotlib.pyplot as plt

cities = ['City A', 'City B', 'City C', 'City D']
temps = {
    'City A': [30, 32, 31, 29, 28, 27, 26],
    'City B': [35, 34, 36, 33, 32, 31, 30],
    'City C': [25, 26, 27, 28, 29, 30, 31],
    'City D': [22, 23, 24, 25, 26, 27, 28]
}

temp_array = np.array([temps['City A'], temps['City B'], temps['City C'], temps['City D']])

average_temp_city = np.mean(temp_array, axis=1)


max_temp_city = np.max(temp_array, axis=1)
min_temp_city = np.min(temp_array, axis=1)


print("Average temperature for each city :")
for i, city in enumerate(cities):
    print(f"{city}: {average_temp_city[i]:} ")

print("\nMaximum temperature for each city:")
for i, city in enumerate(cities):
    print(f"{city}: {max_temp_city[i]} ")

print("\nMinimum temperature for each city:")
for i, city in enumerate(cities):
    print(f"{city}: {min_temp_city[i]} ")

# function 
average_temp_day = np.mean(temp_array, axis=0)

print("\nAverage temperature across all cities :")
for day in range(7):
    print(f"Day {day + 1}: {average_temp_day[day]:} ")

# line trend
days = np.arange(1, 8)

plt.figure(figsize=(10, 6))
for i, city in enumerate(cities):
    plt.plot(days, temp_array[i], label=city)

plt.title("Temperature Trends Over 7 Days")
plt.xlabel("Day")
plt.ylabel("Temp")
plt.xticks(days)
plt.legend()
plt.grid(True)
plt.show()

# temp range
temp_range = max_temp_city - min_temp_city

# Bar chart
plt.figure(figsize=(8, 5))
#plt.bar(cities, temp_range, color=['yellow', 'pink', 'green', 'violet'])
plt.hist(cities, temp_range, color=['yellow', 'pink', 'green', 'violet'])

plt.title("Temperature Range for Each City Over 7 Days")
plt.xlabel("City")
plt.ylabel("Temperature Range (°C)")
plt.show()
