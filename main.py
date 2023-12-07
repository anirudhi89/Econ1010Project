import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('data/data.csv')

# Filter out values 0, 999999, and 999998 in INCWAGE
df = df[(df['INCWAGE'] != 0) & (df['INCWAGE'] != 999999) & (df['INCWAGE'] != 999998)]

# Dictionary for mapping BPL to strings
bpl_mapping = {
    (1, 99): 'USA',
    421: 'France',
    453: 'Germany',
    200: 'Mexico',
    501: 'Japan',
    500: 'China'
}

# Map the BPL values to the corresponding categories
df['BPL_CATEGORY'] = df['BPL'].apply(lambda x: next((region for category, region in bpl_mapping.items() if isinstance(category, tuple) and x in range(category[0], category[1] + 1)), bpl_mapping.get(x, 'Unknown')))


# ==================== Task 1 ====================
# Create separate bar graphs for each year
for year in [1940, 1950, 1960]:
    subset_df = df[df['YEAR'] == year]
    avg_income_per_category = subset_df.groupby('BPL_CATEGORY')['INCWAGE'].mean().reset_index()

    avg_income_per_category = avg_income_per_category[avg_income_per_category['BPL_CATEGORY'] != 'Unknown']

    # Convert 'BPL_CATEGORY' column to string type
    avg_income_per_category['BPL_CATEGORY'] = avg_income_per_category['BPL_CATEGORY'].astype(str)

    # Define colors for each BPL_CATEGORY
    colors = ['b', 'g', 'r', 'c', 'm', 'y']

    # Plotting a bar graph for each year with different colors
    plt.bar(avg_income_per_category['BPL_CATEGORY'], avg_income_per_category['INCWAGE'], color=colors, label=avg_income_per_category['BPL_CATEGORY'])
    plt.title(f'Average Income in {year} by Birthplace')
    plt.xlabel('Birthplace')
    plt.ylabel('Average Income')
    plt.legend()
    plt.show()

# ==================== Task 2 ====================
# Output average income for each bpl group for each year to a CSV file
avg_income_per_year = df.groupby(['YEAR', 'BPL_CATEGORY'])['INCWAGE'].mean().reset_index()
avg_income_per_year.to_csv('results/average_income_per_year.csv', index=False)



# ==================== Task 3 ====================
# Graph each BPL_CATEGORY group's income over time
fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size

for bpl_category in bpl_mapping.values():
    if bpl_category != 'Unknown':
        bpl_category_data = avg_income_per_year[avg_income_per_year['BPL_CATEGORY'] == bpl_category]
        ax.plot(bpl_category_data['YEAR'], bpl_category_data['INCWAGE'], label=bpl_category, linewidth=2)

        # Calculate percent growth
        initial_value = bpl_category_data['INCWAGE'].iloc[0]
        final_value = bpl_category_data['INCWAGE'].iloc[-1]
        percent_growth = ((final_value - initial_value) / initial_value) * 100

        # Display percent growth on the right side of the graph
        ax.text(bpl_category_data['YEAR'].iloc[-1] + 0.1, final_value, f'{percent_growth:.2f}%', ha='left', va='center')

ax.set_title('Average Income Over Time by Birthplace')
ax.set_xlabel('Year')
ax.set_ylabel('Average Income')
ax.set_xticks([1940, 1950, 1960]) 
ax.legend()
plt.show()


