# ECON 1010 - Final Project

#### How did the average income vary over the decades of 1940, 1950, and 1960 for individuals categorized by their birthplaces?

## Team Members
- Anirudh Iyer, AKI22
- Rahul Mannepuli, RVM15
- Aakash Arvapalli, AAA240
- Daniel Mancini, DPM62

## Overview

This repository contains Python code for data analysis and visualization of average wages for different groups, specifically focusing on comparing wages between the USA and selected immigrant groups. The analysis involves filtering, splitting data, calculating averages, and creating bar graphs for visualization.

## Contents
- `preprocess/`: 
   - This code contains the labels from the IPUMS data for variables `BPL`/`BPLD`, and `RACE`/`RACED`. The labels are stored in `BPLD_key.csv` and `RACED_key.csv` respectively. 
- `data/`:
   - `data/data.csv.gz`: The main dataset containing relevant information, compressed.
   - `data/data.csv`: The main dataset containing relevant information 
   - This data is sourced from [Integrated Public Use Microdata Series (IPUMS)](https://pop.umn.edu/projects/ipums-usa), from the 1940 Census data
- `main.py`: 
   - Python script for data analysis and visualization.
- `results/`
   - Directory for storing CSV files generated during the analysis, generated bar graph, and the generated line graphs

## Usage
Requirements: Python 3.6 or higher, and pip3

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/anirudhi89/Econ1010Project.git EconDataAnalysis
   ```
   ```bash
   cd EconDataAnalysis
   ```
2. **Download the Data:**
Download the data from the 1940 Census from [IPUMS](https://pop.umn.edu/projects/ipums-usa), with the added harmonic variables `RACED`, `BPLD`, and `INCWAGE`, and change the data format to csv. Download this file, run ` gzip -ad ~/Downloads/data.csv.gz` to unzip the file, and move it to the `data/` directory. Be sure to rename it to `data.csv`.

3. **Install Dependencies:**
   ```bash
   pip3 install pandas matplotlib
   ```
4. **Run the Script:**
   ```bash
   python3 main.py
    ```
