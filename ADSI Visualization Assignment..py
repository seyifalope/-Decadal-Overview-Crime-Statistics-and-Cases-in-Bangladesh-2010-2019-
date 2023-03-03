# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:12:03 2023

@author: SEYI FALOPE 
"""

# Github Link:
# Dataset Link:https://www.kaggle.com/datasets/firozkabir1/crime-statistics-of-bangladesh-2010-2019


# Importing necessary Python libraries for exploration and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading in the dataset
crime = pd.read_csv(r"C:\Users\USER\Documents\Crime Statistics Of Bangladesh.csv")
print(crime)

"""
Inspecting the data set to check for:

The dimension of the set
The general information about the data and,
if the data has no missing values
"""

print(crime.shape)  # The data has 180 rows and 18 columns

print(crime.info()) # The data contains 1 categorical value  and 17 numerical values 

print(crime.isnull().sum()) # No missing values, so there is no need to clean it up


# Extracting only the columns we need for our visualization
crime = crime[['Year', 'Robbery', 'Murder', 'Kidnapping', 'Police Assault']]
print(crime)

# Grouping and aggregating the columns to get the aggregate crime cases per year
crime = crime.groupby('Year').sum()
print(crime)


# Declaring a function to plot a line graph for the selected crime cases
def plot_line(variable_x, variable_y, xlabel, ylabel, xlim, title, color='', label=''):
    """
    Create a function that plots a line graph for the crime cases.

    Args:
        variable_x : List of values for the x-axis.
        variable_y : List of values for the y-axis.
        color : The color of the line plotted.
        label : Label for the plotted line.
        xlabel: Label for the x-axis.
        ylabel: Label for the y-axis.
        xlim : Set to True to set the x-axis limits.
        title : Title of the graph plotted.

        return
    """
    # Plotting the graph, assigning a color and legend
    plt.plot(variable_x, variable_y, color=color, label=label)

    # Setting labels, limits and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xlim:
        plt.xlim(min(variable_x), max(variable_x))
    plt.title(title)

    # Showing the legend
    plt.legend()

    # Saving the plotted line plot
    plt.savefig('plot_line.png')


# Plotting lineplot for Robbery vs Year
plot_line(crime.index, crime['Robbery'], 'Years', 'No of Crime Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'blue',
          'Robbery')

# Plotting lineplot for Murder Vs Year
plot_line(crime.index, crime['Murder'], 'Years', 'No of Crime Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'r',
          'Murder')

# Plotting lineplot for Kidnapping Vs Year
plot_line(crime.index, crime['Kidnapping'], 'Years', 'No of Crime Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'g',
          'Kidnapping')

# Plotting lineplot for Police Assault
plot_line(crime.index, crime['Police Assault'], 'Years', 'No of Crime Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'y',
          'Police Assault')

# Showing the Plot
plt.show()


"""
Next we want to plot a pie chart, to calculate the total porportion  of 
each crime in comparison to each other.

Hence the total sum of each crime will be calculated
"""

# Calculating the total crime cases for each crime
crime_total = np.sum(crime, axis=0)
print(crime_total)


# Creating the data for each crime and thier respective total cases
crime_names = ['Robbery', 'Murder', 'Kidnapping', 'Police Assault']
total_cases = [8210, 36333, 6754, 6250]


# Declaring a function to plot a pie chart for the selected crime cases
def plot_pie(variable, variable_label, label='', title='', **others):
    """
    Creating a function to plot a pie chart

    Args:
    variable: the values to be plotted on the pie chart.
    variable_label: the names corresponding to the values plotted
    title: the title of the pie chart.
    **others: other arguments to pass into the pie plot function as need be 

    return
    """
    # Creating a figure size for the graph
    plt.figure(figsize=(10, 10))

    # Plotting the pie chart
    plt.pie(variable, labels=variable_label, **others)

    # Setting the legend and title of the plot
    plt.legend(variable_label)
    plt.title(title)

    # Saving the plotted bar chart
    plt.savefig('plot_pie.png')

    # Showing the pie chart
    plt.show()


# Plotting the pie chart
plot_pie(total_cases, crime_names, title='Crime Statistics Of Bangladesh 2010-2019',
         autopct='%2.1f%%', explode=[0, 0.1, 0, 0.], shadow=True)


"""
Thirdly we want to creat a bar chart,
to compare the total cases per year against each year

Hence the total crime rate each year  will be calculated 
"""

# Calculating the total crime cases for each year
year_total = np.sum(crime, axis=1)
print(year_total)

# Data for total crime cases for each year
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
crime_year = [6390, 6408, 6587, 7550, 7291, 6409, 5473, 5258, 5647, 534]




# Defining a function to plot a bar graph for the selected crime cases against each year
def plot_bar(x_variable, y_variable, xlabel, ylabel, title,  xticks=None, **others):
    """
    Creating a function to plot a bar chart

    Args:
    x_variable: the label to be plotted on x-axis.
    y_variable: the values of the data to be plotted
    xlabel: the name of the the x-axis
    ylabel: the name of the the y-axis
    title: title for the bar chart.
    **others: other arguments to pass into the pie plot function as need be
    return: None
    """
    # Delaring the figure size for the bar graph
    plt.figure(figsize=(10, 6))

    # Plotting the pie chart
    plt.bar(x_variable, y_variable, **others)

    # Setting xlabels, ylabels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Setting the xtick label
    if xticks:
        plt.xticks(x_variable)

    # Saving the plotted graph as a png file
    plt.savefig('plot_bar.png')

    # Showing the pie chart
    plt.show()


# plotting the bar chart
plot_bar(years, crime_year, 'Years', 'No of Cases',
         'Crime Statistics Of Bangladesh 2010-2019', True, color='red')






