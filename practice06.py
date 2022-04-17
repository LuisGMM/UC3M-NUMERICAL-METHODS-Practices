

import numpy as np
import matplotlib.pyplot as plt


def composite_midpoint(f_, a:float, b:float, n:float)-> float: 
    
    
    x = np.linspace(a, b, n)
    f = f_(x)
    h = (b - a) / (n - 1)
    m = np.shape(f)[0]
    return h * sum(f[:m-1])

def composite_trapezoid(f_, a:float, b:float, n:float)-> float:
    
    x = np.linspace(a, b, n)
    f = f_(x)
    h = (b - a) / (n - 1)
    m = np.shape(f)[0]
    return h/2 * sum(f[:m-1] + f[1:m])


def simp_int(f_, a:float, b:float, n:float)-> float:

    '''This function approximates the value of the integral for the function values given by "f" 
    which must be taken at equispaced nodes deparated by a distance "h"  '''
    
    x = np.linspace(a, b, n)
    f = f_(x)
    h = (b - a) / (n - 1)
    n = np.shape(f)[0]
    I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) \
                + 4*sum(f[1:n-1:2]) + f[n-1])
    
    return I_simp

def simp_int2(f,h):
    '''This function approximates the value of the integral for the function values given by "f" 
    which must be taken at equispaced nodes deparated by a distance "h"  '''

    n = np.shape(f)[0]
    I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) \
                + 4*sum(f[1:n-1:2]) + f[n-1])
    
    return I_simp



def exercise1():
    
    a = -3
    b = 3
    n = 11
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    f = lambda x: 1/ (1 + x**2)

    mid_f = composite_midpoint(f, a, b, 11), \
            composite_midpoint(f, a, b, 101), \
            composite_midpoint(f, a, b, 1001), \
            composite_midpoint(f, a, b, 10001) 

    trap_f = composite_trapezoid(f, a, b, 11), \
            composite_midpoint(f, a, b, 101), \
            composite_midpoint(f, a, b, 1001), \
            composite_midpoint(f, a, b, 10001) 

    rich_f = simp_int(f, a, b, 11), \
            simp_int(f, a, b, 101), \
            simp_int(f, a, b, 1001), \
            simp_int(f, a, b, 10001) 

    print(mid_f, '\n', trap_f, '\n', rich_f)

    real_value = 2.498091545 # of the integral

    err_mid_f = [abs(real_value - i ) for i in mid_f]
    err_trap_f = [abs(real_value - i ) for i in trap_f]
    err_rich_f = [abs(real_value - i) for i in rich_f]

    print(err_mid_f, '\n', err_trap_f, '\n', err_rich_f)

    x_values = [(3-(-3))/10, (3-(-3))/100, (3-(-3))/1000, (3-(-3))/10000] # We have to plot 

    plt.loglog(x_values, err_mid_f, color='red', label='mid')
    plt.loglog(x_values, err_trap_f, color='green', label='trap')
    plt.loglog(x_values, err_rich_f, color='blue', label='rich')
    plt.legend()
    plt.show()



if __name__ == '__main__':

    
    t = np.arange(84,6)

    h = 6
    speed = [124, 134, 148, 156, 147, 133, 121, 109, 99, 85, 78, 89, 104, 116, 123]
    
    print(simp_int2(speed, h))