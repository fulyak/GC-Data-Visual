import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

# create dictionary that points parameters to column number
def make_dict(file_name='mean_radial_velocities.csv'): 
	"""Make a dictionary
    Creates a dictionary that maps parameter names to the corresponding index from the original data
    Args:
        file_name (string): data set name
    Returns:
        dictionary: maps parameter names to index 
	"""
	params_list = pd.read_csv(file_name,delimiter=',',skiprows=[1]).columns
	unit_list = pd.read_csv(file_name,delimiter=',',skiprows=[0]).columns
	d = {}
	u = []
	for i in range(len(params_list)):
		d[params_list[i].split('\\')[0]] = i
		u.append(unit_list[i].split('.')[0])
		#u[unit_list[i].split('.')[0]]=i
	return d,u

#col,unit = make_dict(file_name='mean_radial_velocities.csv')
#print('params_list=',col)
#print('unit_list=',unit)
def read_data(X,Y,file_name='mean_radial_velocities.csv'):
	if Y != 'N/A':	
		x,y = pd.read_csv(file_name,skiprows=2,header=None,delimiter=',',usecols=(X,Y)).values.T
		return x,y
	else:
		y,x = pd.read_csv(file_name,skiprows=2,header=None,delimiter=',',usecols=(0,X)).values.T
		return x
#d, u = make_dict()
#ind1 = d['X']
#ind2 = d['Y']
#x1,y1 = read_data(ind1,ind2)
#print(x1,y1)
#print('X=',ind1,'Y=',ind2,'X_unit=',u[ind1],'Y_unit=',u[ind2])

# given 1 parameter list, make histogram
def make_hist(param, x, d, u):
	plt.hist(param)
	ind1=d[x]
	plt.xlabel(x+' '+u[ind1])
	plt.ylabel('Number of Globular Clusters')
	plt.show()

# given 2 general parameter lists, make scatter plots of them plotted against each other
def make_scatter(param1, param2, x, y, d, u):
	plt.scatter(param1, param2)
	ind1 = d[x]
	ind2 = d[y]
	plt.xlabel(x+' '+u[ind1])
	plt.ylabel(y+' '+u[ind2])
	plt.show()


d,u = make_dict()
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
	make_hist(param1_list, x,d,u)
else:
	ind2 = d[y]
	param1_list, param2_list = read_data(ind1, ind2)
	if ind1 < ind2:
		make_scatter(param1_list, param2_list, x, y,d,u)
	else: 
		make_scatter(param2_list, param1_list, x, y,d,u)
