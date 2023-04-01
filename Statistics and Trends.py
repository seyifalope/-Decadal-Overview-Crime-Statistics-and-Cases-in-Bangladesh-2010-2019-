# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:34:24 2023

@author: SEYI FALOPE
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
world_data, world_data2 = read_data(r"C:\Users\USER\Desktop\World Bank Data.csv")
print(world_data)

# For this analysis, we will make do with 4 indicators of choice
indicators = world_data[world_data['Indicator Name'].isin(['Arable land (% of land area)', 
                                                          'Urban population','CO2 emissions (kt)',
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
world_data=world_data.drop(['Country Name','Country Code','Indicator Code'])
print(world_data)

"""
For this analysis, 7 countries of choice across various continents
will be selected 
"""
# Selecting countries for analysis
countries=world_data[['China', 'Nigeria', 'India','Philippines','United States', 'Germany','Brazil']]
print(countries)

# Checking for missing values
print(countries.isnull().mean()) # We have lots of missing values in our datasets

# dropping all missing values from our datasets
countries.dropna(inplace=True)
countries.head()
countries.index
print(countries)

"""
for further accessibilty and ease of data analysis, 
datasets that combines all countries on each indicator will be created
"""
# Creating a dataframe for all selected countries on Urban population
urban_pop=countries.iloc[1:,[0,4,8,12,16,20,24]] 
urban_pop=urban_pop.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
urban_pop.index=pd.to_numeric(urban_pop.index) # converting index values to numeric format
print(urban_pop.head())

# creating a dataframe for all selected countries on c02 emission
co2= countries.iloc[1:,[1,5,9,13,17,21,25]] 
co2=co2.apply(pd.to_numeric)  # converting to data type to a numeric format
co2.index=pd.to_numeric(co2.index) # converting index values to numeric format
co2.head()

# creating a dataframe for all selected countries on electric consumption 
electric=countries.iloc[1:,[2,6,10,14,18,22,26]]
electric=electric.apply(pd.to_numeric)  # converting to data type to a numeric format
co2.index=pd.to_numeric(co2.index) # converting index values to numeric format
print(electric.head())

# creating a dataframe for all selected countries on Arable land
arable=countries.iloc[1:,[3,7,11,15,19,23,27]]
arable=arable.apply(pd.to_numeric)# converting the data type to a numeric format
arable.index=pd.to_numeric(arable.index) # converting index values to numeric format
print(arable.head())

"""
Statistical overview for the urban population across selected countries.
Checking Statistical overview for the four selected indicators 
across the 7 selected countries.
"""
#statistical function for urban population
print(urban_pop.describe())
print(urban_pop.mean()) # checking the mean urban population
urban_pop.median() # checking the median urban population
urban_pop.std() # checking the urban population standard deviation

#Statistical function for c02 emission
co2.describe()
co2.mean() # checking the mean urban population
co2.median() # checking the median urban population
co2.std() # checking the urban population standard deviation



urban_pop.describe()
urban_pop.mean()
urban_pop.median()
urban_pop.std()



    