import matplotlib.pyplot as plt 

# given 1 parameter list, make histogram
def make_hist(param):
	plt.hist(param)
	plt.show()

# given 2 general parameter lists, make scatter plots of them plotted against each other
def make_scatter(param1, param2):
	plt.scatter(param1, param2)
	plt.show()


# tests
p = [3, 2, 4, 3, 1, 2]
q = [4, 2, 3, 1, 2, 3]

make_hist(p)
make_scatter(p, q)