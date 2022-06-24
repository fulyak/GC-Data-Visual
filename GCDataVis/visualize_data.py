import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 
import os
def read_headers(file_name='mean_radial_velocities.csv'): 
	""" Reads the headers into a preferred format from the original dataset, file_name
    Creates a dictionary that maps parameter names to its corresponding index and a list of units. 
    Args:
        file_name (string): data set file name
    Returns:
        d (dictionary): maps parameter names to its corresponding index in the original dataset
		u (list): unit names in the order of the parameters in the original dataset
	"""
	filename = os.path.join(os.path.dirname(__file__),file_name)
	params_list = pd.read_csv(filename,delimiter=',',skiprows=[1]).columns
	unit_list = pd.read_csv(filename,delimiter=',',skiprows=[0]).columns
	d = {}
	u = []
	for i in range(len(params_list)):
		d[params_list[i].split('\\')[0]] = i
		u.append(unit_list[i].split('.')[0])
	return d,u

def read_data(X,Y,file_name='mean_radial_velocities.csv'):
	""" Reads the numerical data corresponding to the column numbers X, Y from the original dataset, file_name
	Returns the list of values for the desired parameters.
	Args: 
		X (integer): column number of the first desired parameter 
		Y (integer): column number of the second desired parameter; if no second parameter is desired, Y is N/A
		file_name (string): data set file name
	Returns:
		x (list): list of the parameter values in the Xth column.
		y (list): (returned only if Y is not N/A) list of the parameter values in the Yth column.
	"""
	filename = os.path.join(os.path.dirname(__file__),file_name)
	if Y != 'N/A':	
		x,y = pd.read_csv(filename,skiprows=2,header=None,delimiter=',',usecols=(X,Y)).values.T
		return x,y
	else:
		y,x = pd.read_csv(filename,skiprows=2,header=None,delimiter=',',usecols=(0,X)).values.T
		return x

def make_hist(param, x, d, u):
	""" Makes a histogram plot of the parameter values with the proper labels and units.
	Args:
		param (list): list of the desired parameter values 
		x (string): parameter name that the user wants to plot 
		d (dictionary): dictionary mapping parameter names to its corresponding index
		u (list): unit names in the corresponding order of the parameters  
	Returns:
		None
	"""
	plt.hist(param)
	ind1=d[x]
	plt.xlabel(x+' '+u[ind1])
	plt.ylabel('Number of Globular Clusters')
	plt.show()

def make_scatter(param1, param2, x, y, d, u):
	""" Makes a scatter plot of the first desired parameter values vs. the second desired 
	parameter values. The proper labels and units are included in the plot.
	Args:
		param1 (list): list of the first desired parameter values 
		param2 (list): list of the second desired parameter values
		x (string): first parameter name that the user inputs to plot 
		y (string): second parameter name that the user inputs to plot
		d (dictionary): dictionary mapping parameter names to its corresponding index
		u (list): unit names in the corresponding order of the parameters
	Returns:
		None
	"""
	plt.scatter(param1, param2)
	ind1 = d[x]
	ind2 = d[y]
	plt.xlabel(x+' '+u[ind1])
	plt.ylabel(y+' '+u[ind2])
	plt.show()


"""Main body code:
The user enters the one or two parameters they would like to plot from the data catalog, 
and the plots are created. 
"""

# read the data
d,u = read_headers()

# create a list of the parameter names
a = [i for i in d.keys()]

# prompt the user to type in the first parameter they want to plot
print('What parameter(s) would you like to plot? Valid parameters include: ', ', '.join(a))
x = input()

# if what the user typed is not in the data parameters, prompt user to retype a valid name
while x not in d:
	print('Please enter a valid parameter! Valid parameters include: ', ', '.join(a))
	print('What parameter(s) would you like to plot?')
	x = input()

# if the user types a valid parameter name, save the index of that parameter
if x in d:
	ind1 = d[x]

# prompt the user to type in the second parameter they want to plot and perform the same process as above
print('What other parameter would you want to plot? Please enter N/A if you only want to plot one parameter.')
y = input()
while y not in d and y != 'N/A':
	print('Please enter a valid parameter! Valid parameters include: ', ', '.join(a))
	print('What other parameter would you want to plot? Please enter N/A if you only want to plot one parameter.')
	y = input()

# if the user types a valid second parameter name, display a scatter plot. If the second parameter is N/A, display a histogram.
print("Here is your plot!")
if y == 'N/A':
	ind2 = 'N/A'
	param1_list = read_data(ind1, ind2)
	make_hist(param1_list, x,d,u)
else:
	ind2 = d[y]
	param1_list, param2_list = read_data(ind1, ind2)
	if ind1 < ind2:
		make_scatter(param1_list, param2_list, x, y,d,u)
	else: 
		make_scatter(param2_list, param1_list, x, y,d,u)
