import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('data.csv')

# Split the data into USA and immigrants
usa_data = data[data['MIGPLAC5'].between(0, 120)]
immigrants_data = data[data['MIGPLAC5'] > 120]

# Save the split data to CSV files
usa_data.to_csv('r3/USA_wage.csv', index=False)
immigrants_data.to_csv('r3/immigrant_wage.csv', index=False)

# Calculate average wages for USA and immigrants
avg_USA_wage = usa_data['FWAGE1'].mean()
avg_immigrant_wage = immigrants_data['FWAGE1'].mean()

# Save the average wages to CSV files
pd.Series(avg_USA_wage).to_csv('r3/avg_USA_wage.csv', header=['Average_Wage'])
pd.Series(avg_immigrant_wage).to_csv('r3/avg_immigrant_wage.csv', header=['Average_Wage'])

# Plot the results as a bar graph, USA, and Immigrants
plt.figure(figsize=(10, 6))
bars = plt.bar(['USA', 'Immigrants'], [avg_USA_wage, avg_immigrant_wage], color=['blue', 'orange'])
plt.xlabel('Group')
plt.ylabel('Average Wage')
plt.title('Average Wages (USA vs. Immigrants)')
plt.show()
