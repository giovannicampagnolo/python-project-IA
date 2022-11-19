import numpy as np
import pandas as pd

def linear_regr(dataset, value):
	data = pd.read_csv(dataset, header=0, names=['x', 'y'])
	data.insert(0, 'Ones', 1)
	columns = data.shape[1]
	X = data.iloc[:,0:columns-1]
	y = data.iloc[:,columns-1:columns]
	X = np.matrix(X.values)
	y = np.matrix(y.values)
	theta = np.matrix(np.array([0,0]))
	alpha = 0.01
	iters = 1000
	# calculate gradient descent
	temp = np.matrix(np.zeros(theta.shape))
	par = int(theta.ravel().shape[1])
	cost = np.zeros(iters)
	for i in range(iters):
		# calculate error
		error = (X*theta.T)-y
		#calculate new theta vector
		for j in range(par):
			term = np.multiply(error, X[:,j])
			temp[0,j] = theta[0,j]-((alpha/len(X))*np.sum(term))
		theta = temp
		# calculate compute cost
		cost[i] = np.sum(np.power(((X*theta.T)-y), 2))/(2*len(X))
	f = theta[0,0] + (theta[0,1]*value)
	return f


def vertical_stack(a, b):
    a=np.array(a)
    b=np.array(b)
    if (len(a)==0 or len(b)==0 or len(a)!=len(b)):
        return []
    return np.vstack((a,b))

def match(a, b):
    a=np.array(a)
    b=np.array(b)
    if (len(a)==0 or len(b)==0 or len(a)!=len(b)):
        return []
    return np.where(a==b)