import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

# create dictionary that points parameters to column number
def make_dict(file_name): 
	"""Make a dictionary
	Creates a dictionary that maps parameter names to the corresponding index from the original data
	Args:
		file_name (string): data set name
	Returns:
		dictionary: maps parameter names to index 
	"""
	file = open(file_name, 'r')
	param_names = pd.read_csv(file, nrows=1)
	params_list = (param_names.iloc[0].index[0]).split( )
	d = {}
	for i in range(len(params_list)):
		if params_list[i] == 'RAPO\\':
			params_list[i] = 'RAPO'
		d[params_list[i]] = i
	return d
	
def read_data(X,Y,file_name='mean_radial_velocities.dat'):
	file = open(file_name,'r')
	if Y != 'N/A':
		x,y = pd.read_csv(file,skiprows=2,header=None,delim_whitespace=True,usecols=(X,Y)).values.T
		return x,y
	else:
		y,x = pd.read_csv(file,skiprows=2,header=None,delim_whitespace=True,usecols=(0,X)).values.T
		print('x', x)
		return x

# given 1 parameter list, make histogram
def make_hist(param, x):
	plt.hist(param)
	plt.xlabel(x)
	plt.ylabel('Number of Globular Clusters')
	plt.show()

# given 2 general parameter lists, make scatter plots of them plotted against each other
def make_scatter(param1, param2, x, y):
	plt.scatter(param1, param2)
	plt.xlabel(x)
	plt.ylabel(y)
	plt.show()


d = make_dict('mean_radial_velocities.dat')
print('What parameter(s) would you like to plot?')
x = input()

while x not in d:
	a = [i for i in d.keys()]
	print('Please enter a valid parameter! Valid parameters include: ', ', '.join(a))
	print('What parameter(s) would you like to plot?')
	x = input()

if x in d:
	ind1 = d[x]

print('What other parameter would you want to plot? Please enter N/A if not applicable.')
y = input()

while y not in d and y != 'N/A':
	a = [i for i in d.keys()]
	print('Please enter a valid parameter! Valid parameters include: ', ', '.join(a))
	print('What other parameter would you want to plot? Please enter N/A if not applicable.')
	y = input()

print("Here is your plot!")
if y == 'N/A':
	ind2 = 'N/A'
	param1_list = read_data(ind1, ind2)
	make_hist(param1_list, x)
else:
	ind2 = d[y]
	param1_list, param2_list = read_data(ind1, ind2)
	if ind1 < ind2:
		make_scatter(param1_list, param2_list, x, y)
	else: 
		make_scatter(param2_list, param1_list, x, y)
