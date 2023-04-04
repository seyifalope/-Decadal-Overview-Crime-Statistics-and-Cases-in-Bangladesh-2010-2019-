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
indicators = world_data[world_data['Indicator Name'].isin(['Forest area (% of land area)', 
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
for further accessibilty and ease of data analysis, datasets that combines all 
countries on each indicator will be created in five years increments from 1990 to 2010
"""
# Creating a dataframe for all selected countries on Urban population
urban_pop_allyears=countries.iloc[1:,[0,4,8,12,16,20,24]] # dataframe for all years in study
urban_pop=countries.iloc[[1,6,11,16,21],[0,4,8,12,16,20,24]] # data frame for 5 years increment
urban_pop=urban_pop.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
urban_pop.index=pd.to_numeric(urban_pop.index) # converting index values to numeric format
urban_pop

# creating a dataframe for all selected countries on c02 emission
co2_allyears= countries.iloc[1:,[1,5,9,13,17,21,25]] # dataframe for all years in study
co2= countries.iloc[[1,6,11,16,21],[1,5,9,13,17,21,25]] # data frame for 5 years increment
co2=co2.apply(pd.to_numeric)  # converting to data type to a numeric format
co2.index=pd.to_numeric(co2.index) # converting index values to numeric format
co2

# creating a dataframe for all selected countries on electric consumption 
electric_allyears=countries.iloc[1:,[2,6,10,14,18,22,26]] # dataframe for all years in study
electric=countries.iloc[[1,6,11,16,21],[2,6,10,14,18,22,26]]# data frame for 5 years increment
electric=electric.apply(pd.to_numeric)  # converting to data type to a numeric format
electric.index=pd.to_numeric(electric.index) # converting index values to numeric format
electric

# creating a dataframe for all selected countries on Arable land
forest_allyears=countries.iloc[1:,[3,7,11,15,19,23,27]] # dataframe for all years in study
forest=countries.iloc[[1,6,11,16,21],[3,7,11,15,19,23,27]] # data frame for 5 years increment
forest=forest.apply(pd.to_numeric)# converting the data type to a numeric format
forest.index=pd.to_numeric(forest.index) # converting index values to numeric format
forest.head()

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
print(co2.describe())
print(co2.mean()) # checking the mean co2
print(co2.median()) # checking the median co2
print(co2.std()) # checking the co2 standard deviation

#Statistical function for electric consumption 
print(electric.describe())
print(electric.mean()) # checking the mean co2
print(electric.median()) # checking the median co2
print(electric.std()) # checking the co2 standard deviation

#Statistical function for Arable Land 
print(forest.describe())
print(forest.mean()) # checking the mean for arable land
print(forest.median()) # checking the median arable land
print(forest.std()) # checking the arable land standard deviation

"""
Plotting a grouped bar of CO2 emission for the nations  in 5 years increments
from the year 1990 to 2010 
"""
plt.style.use('ggplot')
co2.T.plot(kind='bar')
plt.title('Co2 emission in 5 years increments (1990-2010)')
plt.xlabel('Countries')
plt.ylabel('Co2 emission (kt)')
plt.show()


"""
plotting a line plot showing Trend in Urban Population for the selected countries
"""
plt.figure(figsize=(10,6))
plt.style.use('ggplot')
urban_pop.T.plot(kind='bar')
plt.title('Urban Population Trend from 1990-2010')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.show()

"""
plotting a line plot showing Trend in electricity consumption per capita for the countries
"""
plt.style.use('ggplot')
electric.plot()
plt.title('Electricity Consumption per capital from 1990 to 2010')
plt.xlabel('Year')
plt.ylabel('electric consuption per capital')
plt.xticks([1990,1995,2000,2005,2010])
plt.legend(bbox_to_anchor=(1.0,1))
plt.show()

"""
Plotting a scatter plot to show relationship for Co2 emmission and Forest Area for China
"""
plt.style.use('ggplot')
plt.scatter(forest_allyears['China'], co2_allyears['China'])
plt.title('Relationship between Forest Area and Co2 emmission in China')
plt.xlabel('Forest area (% of land area)')
plt.ylabel('Co2 Emmision')
plt.show()

"""
Plotting a scatter plot to show relationship for Co2 emmission and Forest Area for Brazil
"""
plt.style.use('ggplot')
plt.scatter(forest_allyears['Brazil'],co2_allyears['Brazil'])
plt.title('Relationship between Forest Area and Co2 emmission in Brazil')
plt.xlabel('Forest area (% of land area)')
plt.ylabel('Co2 Emmision')
plt.show()




    
