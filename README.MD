# ECON 1010 - 
## Overview

This repository contains Python code for data analysis and visualization of average wages for different groups, specifically focusing on comparing wages between the USA and selected immigrant groups. The analysis involves filtering, splitting data, calculating averages, and creating bar graphs for visualization.

## Contents

- `data.csv`: The main dataset containing relevant information.
    - This data is sourced from [Integrated Public Use Microdata Series (IPUMS)](https://pop.umn.edu/projects/ipums-usa), from the 1940 Census data
- `main.py`: Python script for data analysis and visualization.
- `results/`: Directory for storing CSV files generated during the analysis, and generated bar graph

## Usage
Requirements: Python 3.6 or higher, and pip3

1. Download the data from the 1940 Census from [IPUMS](https://pop.umn.edu/projects/ipums-usa), with variables MIGPLAC5 and US1940A_FAMERN , and save it as `data.csv` in `data/`.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/anirudhi89/Econ1010Project.git EconDataAnalysis
   ```
   ```bash
   cd EconDataAnalysis
   ```
3. **Install Dependencies:**
   ```bash
   pip3 install pandas matplotlib
   ```
4. **Run the Script:**
   ```bash
   python3 main.py
    ```
