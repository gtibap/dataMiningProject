import scipy
import matplotlib.pyplot as plt
import numpy as np
import pymc
import math


#Sine parameters

true_intercept=5
true_slope=1.74
extra_par=0.08
true_err=0.3
size=50


'''
#Lineal parameters
true_intercept=5
true_slope=1.74
extra_par=0.08
true_err=6.2
size=50
'''

'''
true_intercept=105
true_slope=1.74
extra_par=0.08
true_err=10.2
size=50
'''

t = np.array(range(0,size))
true_regression_line = true_intercept + true_slope * np.sin(t*extra_par*math.pi)
print "Max: ",np.max(true_regression_line)
#true_regression_line = true_intercept - true_slope * t**2
y = true_regression_line + np.random.normal(scale=true_err, size=size)
#y = [min(p, 6) for p in y]
#y = true_regression_line


'''
# *************************************
#      Bayesian Linear Regression
# *************************************

b0 = pymc.Normal("b0", 0, 0.0003)
b1 = pymc.Normal("b1", 0, 0.0003)
err = pymc.Uniform("err", 0, 500)

x_weight = pymc.Normal("weight", 0, 1, value=t, observed=True)

@pymc.deterministic
def pred(b0=b0, b1=b1, x=t):
    return b0 + b1*x

y_pred = pymc.Normal("y", pred, err, value=y, observed=True)

model = pymc.Model([pred, b0, b1, y_pred, err, x_weight])


mcmc = pymc.MCMC(model)
mcmc.sample(50000, 20000)

print "b0: ",np.mean(mcmc.trace('b0')[:]),"b1: ",np.mean(mcmc.trace('b1')[:]),"err: ",np.mean(mcmc.trace('err')[:])

b0 = np.mean(mcmc.trace('b0')[:])
b1 = np.mean(mcmc.trace('b1')[:])

plt.scatter(t,y)
plt.plot(t, [b0 + p*b1 for p in t])
plt.show()


''
# *************************************
#      Bayesian Polinomial Regression (Quadratic)
# *************************************
b0 = pymc.Normal("b0", 0, 0.0003)
b1 = pymc.Normal("b1", 0, 0.0003)
b2 = pymc.Normal("b2", 0, 0.0003)
err = pymc.Uniform("err", 0, 500)

x_weight = pymc.Normal("weight", 0, 1, value=t, observed=True)

@pymc.deterministic
def pred(b0=b0, b1=b1, b2=b2, x=x_weight):
    return b0 + b1*x + b2*x*x

y_pred = pymc.Normal("y", pred, err, value=y, observed=True)

model = pymc.Model([pred, b0, b1, b2, y_pred, err, x_weight])


mcmc = pymc.MCMC(model)
mcmc.sample(50000, 20000)

print "b0: ",np.mean(mcmc.trace('b0')[:]),"b1: ",np.mean(mcmc.trace('b1')[:]),"b2: ",np.mean(mcmc.trace('b2')[:]),"err: ",np.mean(mcmc.trace('err')[:])

b0 = np.mean(mcmc.trace('b0')[:])
b1 = np.mean(mcmc.trace('b1')[:])
b2 = np.mean(mcmc.trace('b2')[:])

plt.scatter(t,y)
plt.plot(t, [b0 + p*b1 + p*p*b2 for p in t])
plt.show()
'''

# *************************************
#      Bayesian Sinusoidal Regression 
# *************************************
b0 = pymc.Normal("b0", 0, 0.0003)
b1 = pymc.Normal("b1", 0, 0.0003)
b2 = pymc.Normal("b2", 0, 0.0003)
err = pymc.Uniform("err", 0, 500)

time = pymc.Normal("weight", 0, 1, value=t, observed=True)

@pymc.deterministic
def pred(b0=b0, b1=b1, b2=b2, t=time):
    return b0 + b1*np.sin(t * b2)

y_pred = pymc.Normal("y", pred, err, value=y, observed=True)

model = pymc.Model([pred, b0, b1, b2, y_pred, err, time])


mcmc = pymc.MCMC(model)
mcmc.sample(50000, 20000)

print "b0: ",np.mean(mcmc.trace('b0')[:]),"b1: ",np.mean(mcmc.trace('b1')[:]),"b2: ",np.mean(mcmc.trace('b2')[:]),"err: ",np.mean(mcmc.trace('err')[:])

b0 = np.mean(mcmc.trace('b0')[:])
b1 = np.mean(mcmc.trace('b1')[:])
b2 = np.mean(mcmc.trace('b2')[:])

plt.scatter(t,y)
plt.plot(t, [b0 + b1*np.sin(p*b2) for p in t])
plt.show()
#'''

