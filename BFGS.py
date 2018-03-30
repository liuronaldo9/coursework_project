import numpy as np
from scipy.optimize import minimize

def rosen(x):
	"""The Rosenbrock function"""
	return np.sin(x)

def rosen_der(x):

	return np.cos(x)

x0 = 10.0  # Initial guess
res = minimize(rosen, x0, method='BFGS', jac=rosen_der, options={'disp': True})

print(res.x) # Optimization result