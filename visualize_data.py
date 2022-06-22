import matplotlib.pyplot as plt 
import pandas as pd
# given 1 parameter list, make histogram
def make_hist(param):
	plt.hist(param)
	plt.show()

# given 2 general parameter lists, make scatter plots of them plotted against each other
def make_scatter(param1, param2):
	plt.scatter(param1, param2)
	plt.show()

def read_data(X,Y,file_name='mean_radial_velocities.dat'):
    file = open(file_name,'r')
    x,y = pd.read_csv(file,skiprows=2,header=None,delim_whitespace=True,usecols=(X,Y)).values.T
    return x,y
# tests
p = [3, 2, 4, 3, 1, 2]
q = [4, 2, 3, 1, 2, 3]

make_hist(p)
make_scatter(p, q)

x, y = read_data(0,1)
print(x,y)
