import json
import matplotlib.pyplot as plt

# Load the JSON data
with open('path_to_your_file/ID001.json', 'r') as file:
    data = json.load(file)

# Extract the raw data
raw_data = data["raw_data"]

# Create a plot
plt.figure(figsize=(12, 6))
plt.plot(raw_data, label='ICG Reading', color='b')
plt.title('ICG Reading of Heart')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('ICG Reading')
plt.legend()
plt.grid(True)


# Show the plot
plt.show()