import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('data.csv')

# Define the MIGPLAC5 values for comparison
countries = {'France': 421, 'Germany': 453, 'Mexico': 200, 'Japan': 501, 'China': 500}

# Split the data into USA and immigrants
usa_data = data[data['MIGPLAC5'].between(0, 120)]
immigrants_data = data[data['MIGPLAC5'] > 120]

# Save the split data to CSV files
usa_data.to_csv('USA_wage.csv', index=False)
immigrants_data.to_csv('immigrant_wage.csv', index=False)

# Calculate average wages for USA (excluding 0 values)
avg_USA_wage = usa_data[usa_data['US1940A_FAMERN'] != 99999]['US1940A_FAMERN'].mean()

# Calculate average wages for each immigrant group (excluding 0 values)
avg_immigrant_wages = {}
for country, migplac5 in countries.items():
    country_data = immigrants_data[immigrants_data['MIGPLAC5'] == migplac5]
    avg_wage = country_data[country_data['US1940A_FAMERN'] != 99999]['US1940A_FAMERN'].mean()
    avg_immigrant_wages[country] = avg_wage

# Save the average wages to CSV files
pd.Series(avg_USA_wage).to_csv('avg_USA_wage.csv', header=['Average_Wage'])
for country, avg_wage in avg_immigrant_wages.items():
    pd.Series(avg_wage).to_csv(f'avg_{country}_wage.csv', header=['Average_Wage'])

# Plot the results as a bar graph for USA vs. Immigrants
plt.figure(figsize=(12, 8))

# Bar for USA
plt.bar('USA', avg_USA_wage, color='blue', label='USA')

# Bars for Immigrants
for country, avg_wage in avg_immigrant_wages.items():
    plt.bar(country, avg_wage, label=country)

plt.xlabel('Group')
plt.ylabel('Average Wage')
plt.title('Average Wages (USA vs. Immigrants)')
plt.legend()
plt.show()
