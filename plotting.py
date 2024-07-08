import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('output.csv', delimiter=';', names=['Time(S)', 'Cur(A)', 'Vol(V)'])

# Convert the relevant columns to numeric types
data['Time(S)'] = pd.to_numeric(data['Time(S)'], errors='coerce')
data['Cur(A)'] = pd.to_numeric(data['Cur(A)'].str.replace(',', '.'), errors='coerce')
data['Vol(V)'] = pd.to_numeric(data['Vol(V)'].str.replace(',', '.'), errors='coerce')

# Ensure there are no NaN values that could affect calculations
data = data.dropna()

# Filter out initial zero-current data points
data = data[data['Cur(A)'] > 0]

# Calculate the total time in hours
total_time_seconds = data['Time(S)'].iloc[-1] - data['Time(S)'].iloc[0]
total_time_hours = total_time_seconds / 3600

# Debug: print the total time in seconds and hours
print(f"Total time (seconds): {total_time_seconds}")
print(f"Total time (hours): {total_time_hours}")

# Calculate the constant current (assuming it remains constant after filtering)
constant_current = data['Cur(A)'].iloc[0]

# Calculate the capacity in Ah
capacity_Ah = constant_current * total_time_hours

# Plot the voltage vs time
plt.figure(figsize=(10, 6))
plt.plot(data['Time(S)'], data['Vol(V)'], label='Napięcie (V)', color='orange')
plt.xlabel('Czas (s)')
plt.ylabel('Napięcie (V)')
plt.title('Cela 1')

# Display the capacity on the plot
capacity_text = f'Obliczona pojemność: {capacity_Ah:.2f} Ah'
plt.text(0.05, 0.95, capacity_text, transform=plt.gca().transAxes, fontsize=12,
         verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
