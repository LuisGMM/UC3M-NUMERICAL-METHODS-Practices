import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')



def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial 
    at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p



def exercise_1():

    time = [0,20,40,60,80,100,120,140, 160, 180, 200]
    pen = [0, 106, 1600, 3000, 5810, 8600, 9430, 10950, 10280, 9620, 9400]

    coefs = divided_diff(time, pen)[0]

    fig, ax = plt.subplots()

    ax.scatter(time, pen)

    ax.plot(np.arange(0,201, 1),[newton_poly(coefs, time, x) for x in np.arange(0,201, 1)])

    plt.scatter(250, newton_poly(coefs, time, 250))

    plt.show()


def f(x): return 1 / (1 + x**2)


def exercise_2():


    x = np.linspace(-5,5, 11, endpoint=True)

    f_x = f(x)

    coef = divided_diff(x, f_x)[0]

    fig, ax = plt.subplots()

    ax.scatter(x, f_x)

    x_2 = np.arange(-5, 5.01, 0.01)
    ax.plot(x_2, [newton_poly(coef, x, x_i) for x_i in x_2])
    
    ax.plot(x_2, f(x_2))

    from scipy.interpolate import interp1d

    f_new = interp1d(x, f_x)

    x_3 = np.linspace(-5, 5, 100, endpoint=True)
    plt.plot(x_3, f_new(x_3))
    
    
    plt.show()


if __name__=="__main__":

    exercise_1()


