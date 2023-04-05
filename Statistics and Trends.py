# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:34:24 2023

@author: SEYI FALOPE
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import stats


"""
Creating a def function to read in our datasets and returns  two 
dataframes:one with years as columns, the other with nations
"""


def read_data(filename, **others):
    """
    A function that reads in climate change data alongside various indicators from 
    the world bank database and returns both the original and transposed version of
    the dataset

    Args:
        filename: the name of the world bank data that will be read for analysis 
        and manupulation

        **others: other arguments to pass into the functions as need be

    Returns: 
        The original dataset format as obtained from the world bank and its transposed version
    """

    # Reading in the climate dataset for to be used for analysis with years as columns
    world_data = pd.read_csv(filename, skiprows=4)

    # Transposing and cleaning the dataset such that the country names are the columns
    world_data2 = pd.DataFrame.transpose(world_data)
    world_data2 = world_data2.drop(
        ['Country Name', 'Country Code', 'Indicator Code'])
    world_data2.columns = world_data2.iloc[0]
    world_data2 = world_data2.iloc[1:]

    return world_data, world_data2


# Reading in our datasets for analysis
world_data, world_data2 = read_data(
    r"C:\Users\USER\Desktop\World Bank Data.csv")
print(world_data)

# For this analysis, we will make do with 4 indicators of choice
indicators = world_data[world_data['Indicator Name'].isin(['Forest area (% of land area)',
                                                          'Urban population', 'CO2 emissions (kt)',
                                                           'Electric power consumption (kWh per capita)'])]
print(indicators)

"""
The data looks complex and uneasy to work with, 
various data wrangling exercise will be perform to make the data accessible
 and easier to analyze
"""
world_data = pd.DataFrame.transpose(indicators)  # Transposing the data
print(world_data)

# Making the country name as columns.
world_data.columns = world_data.iloc[0]
world_data

# dropping rows not needed from the data
world_data = world_data.drop(
    ['Country Name', 'Country Code', 'Indicator Code'])
print(world_data)

"""
For this analysis, 7 countries of choice across various continents
will be selected 
"""
# Selecting countries for analysis
countries = world_data[['China', 'Nigeria', 'India',
                        'Philippines', 'United States', 'Germany', 'Brazil']]
print(countries)

# Checking for missing values
# We have lots of missing values in our datasets
print(countries.isnull().mean())

# dropping all missing values from our datasets
countries.dropna(inplace=True)
countries.head()
countries.index
print(countries)

"""
for further accessibilty and ease of data analysis, datasets that combines all 
countries on each indicator will be created in five years increments from 1990 to 2010
"""
"""
Creating a dataframe for all selected countries on Urban population
"""
# dataframe for all years in study
urban_pop_allyears = countries.iloc[1:, [0, 4, 8, 12, 16, 20, 24]]
# data frame for 5 years increment
urban_pop = countries.iloc[[1, 6, 11, 16, 21], [0, 4, 8, 12, 16, 20, 24]]
# converting to dataframe data type to a numeric format
urban_pop = urban_pop.apply(pd.to_numeric)
# converting index values to numeric format
urban_pop.index = pd.to_numeric(urban_pop.index)
print(urban_pop)

"""
creating a dataframe for all selected countries on c02 emission
"""
# dataframe for all years in study
co2_allyears = countries.iloc[1:, [1, 5, 9, 13, 17, 21, 25]]
# data frame for 5 years increment
co2 = countries.iloc[[1, 6, 11, 16, 21], [1, 5, 9, 13, 17, 21, 25]]
co2 = co2.apply(pd.to_numeric)  # converting to data type to a numeric format
# converting index values to numeric format
co2.index = pd.to_numeric(co2.index)
print(co2)

"""
creating a dataframe for all selected countries on electric consumption
"""
# dataframe for all years in study
electric_allyears = countries.iloc[1:, [2, 6, 10, 14, 18, 22, 26]]
# data frame for 5 years increment
electric = countries.iloc[[1, 6, 11, 16, 21], [2, 6, 10, 14, 18, 22, 26]]
# converting to data type to a numeric format
electric = electric.apply(pd.to_numeric)
# converting index values to numeric format
electric.index = pd.to_numeric(electric.index)
print(electric)

"""
creating a dataframe for all selected countries on Forest land
"""
# dataframe for all years in study
forest_allyears = countries.iloc[1:, [3, 7, 11, 15, 19, 23, 27]]
# data frame for 5 years increment
forest = countries.iloc[[1, 6, 11, 16, 21], [3, 7, 11, 15, 19, 23, 27]]
# converting the data type to a numeric format
forest = forest.apply(pd.to_numeric)
# converting index values to numeric format
forest.index = pd.to_numeric(forest.index)
print(forest.head())

"""
Statistical overview  to explore the data  across selected countries.
Checking Statistical overview for the four selected indicators 
across the 7 selected countries.
"""
# statistical function for urban population
# Checking describe function for urban population
print(urban_pop.describe())
print('Skewness:', stats.skew(urban_pop))  # skweness for urban population
print('Kurtosis:', stats.kurtosis(urban_pop))  # Kurtosis for urban population

# Statistical function for c02 emission
print(co2.describe())  # describe function for co2 emission
print('Skewness:', stats.skew(co2))  # skweness for co2 emission
print('Kurtosis:', stats.kurtosis(co2))  # Kurtosis for co2 emission


# Statistical function for electric power consumption (kWh per capita)'
print(electric.describe())  # describe function for electric power consumption
# skweness for electric power consumption
print('Skewness:', stats.skew(electric))
# Kurtosis for electric power consumption
print('Kurtosis:', stats.kurtosis(electric))

# Statistical function for Forest area (% of land area)
print(forest.describe())  # describe function for forest area
print('Skewness:', stats.skew(forest))  # skweness for forest area
print('Kurtosis:', stats.kurtosis(forest))  # Kurtosis for forest area

"""
Plotting a grouped bar of CO2 emission for the 7 nations  in 5 years increments
from the year 1990 to 2010 
"""
# choosing a style for the bar chart
plt.style.use('ggplot')

# plotting the bar chart for Urban Population
co2.T.plot(kind='bar')

# setting the Legend title, xlabel and ylabel
plt.title('Nations co2 emission in 5 years increments', size=12, weight='bold')
plt.xlabel('Countries', weight='bold')
plt.ylabel('Co2 emission (kt)', weight='bold')

# Saving the plotted line Graph
plt.savefig('co2_barplot.png')

# Showing the line plot plot
plt.show()

"""
plotting a line plot showing Trend in Urban Population for the selected countries
"""
# Creating a figure size for the graph
plt.figure(figsize=(10, 6))

# choosing a style for the line plot
plt.style.use('ggplot')

# plotting the line plot for Urban Population
urban_pop.plot()

# setting the Legend title, xlabel and ylabel
plt.title('Urban Population Trend from 1990-2010', size=15, weight='bold')
plt.xlabel('Year', weight='bold')
plt.ylabel('Urban Population', weight='bold')
plt.xticks([1990, 1995, 2000, 2005, 2010])
plt.legend(bbox_to_anchor=(1.0, 1))

# Saving the plotted line Graph
plt.savefig('urban_lineplot.png')

# Showing the line plot plot
plt.show()

"""
plotting a line plot showing Trend in Electric power consumption (kWh per capita)
"""
# choosing a style for the line plot
plt.style.use('ggplot')

# plotting the line plot for Electric power consumption (kWh per capita)
electric.plot()

# setting the title, xlabel and ylabel
plt.title('Electric power consumption from 1990 to 2010',
          size='12', weight='bold')
plt.xlabel('Year', weight='bold')
plt.ylabel('electric consuption per capital', weight='bold')
plt.xticks([1990, 1995, 2000, 2005, 2010])
plt.legend(bbox_to_anchor=(1.0, 1))

# Saving the plotted line Graph
plt.savefig('electric_lineplot.png')

# Showing the line plot plot
plt.show()


"""
Plotting a scatter plot to show relationship for Co2 emmission and Forest Area for China
"""
# choosing a style for the plot
plt.style.use('ggplot')

# plotting the scatter plot
plt.scatter(forest_allyears['China'], co2_allyears['China'])

# setting the , title, xlabel and ylabel
plt.title('Relationship between Forest Area and Co2 emmission in China', size='11')
plt.xlabel('Forest area (% of land area)', fontsize=10, weight='bold')
plt.ylabel('Co2 Emmision', fontsize=10, weight='bold')

# Saving the plotted scatter plot
plt.savefig("scatter_china.png")

# Showing the scatter plot
plt.show()


"""
Plotting a scatter plot to show relationship for Co2 emmission and Forest Area for Brazil
"""
# choosing a style for the plot
plt.style.use('ggplot')

# Plotting the scatter plot
plt.scatter(forest_allyears['Brazil'], co2_allyears['Brazil'])

# Setting the , title, xlabel and ylabel
plt.title('Relationship between Forest Area and Co2 emmission in Brazil',
          fontsize=11, weight='bold')
plt.xlabel('Forest area (% of land area)', weight='bold')
plt.ylabel('Co2 Emmision', weight='bold')

# Saving the plotted scatter plot
plt.savefig('scatter_brazil.png')

# Showing the scatter plot
plt.show()
