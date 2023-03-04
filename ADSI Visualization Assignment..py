
"""
Created on Wed Mar  1 22:12:03 2023

@author: SEYI FALOPE 
"""

"""
SUMMARY OF THE DATASET
The dataset illustrates the crime statistics of various crimes and their crime cases 
in Bangladesh, a densely populated country in Asia across a decade period, 
from year 2010 to 2019.

To visulaizing and draw insights from the data,3 types of visualization methods will be
employed, Namely:
    
Line plot: A line plot is used to displays data points over a period of time, hence line 
plot be employed to show crime cases for each crime over the decade    

Pie Chart: A pie chart helps to displays categories of elements in relative proportion 
to each other. This will be employed to show the proportion of each crime in relation to
each other

Bar Chart: A bar chart helps us compare different data points together. This will be employed
to show the compare the total crimes case across the decade
"""

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
INTERPRETING THE LINE PLOT
The line graph provides insight for 4 crimes: robbery, kidnapping, murder and police assault
and thier total reported cases in Bangladesh for the year 2010 to 2019. From the graph, 
it can be drawn that the number of robbery cases remained relatively stable 
from 2010 to 2013 with a slight increase in 2014 followed by a decrease in the following
years. The murder cases appear to be relatively fluctuating from year to year. However,
there is a slight increase in the year 2014, followed by a decrease in 2015 and a sharp 
 increase in 2018. Kidnapping and police incidents appear to be stable over
the years. However, it shows a slight increase in 2014 and 2018 for both crimes
 
The plot also shows that all the 4 crime cases experienced decline in year 2019
"""



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

"""
INTERPRETING THE BAR CHART:
The bar chart shows that the crime rates were stagnant/increasing from year 2010 t0 2013 
and starting  decreasing afterwqrds from year 2014 t0 2018. From the graph, it 
can be deduce that 2013 had the highest crime reported incident and 2019 has the lowest 
reported crime rate
"""    







