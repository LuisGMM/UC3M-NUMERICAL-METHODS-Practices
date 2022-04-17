

import numpy as np
import matplotlib.pyplot as plt



def euler_explicit_midpoint(f:'Callable[float, float]', y0:float, t0:float, t:float, h:float)-> np.ndarray:
    """Computes the explicit (forward) midpoint Euler method to solve ODEs.

    Args:
        f (Callable[float, float]): Function depending on y and t in that order.
            Equivalent to f(y,t).
        y0 (float): Initial value of the answer.
            Equivalent to y(t0).
        t0 (float): Initial time.
        t (float): Final time.
        h (float): Separation between the points of the interval.

    Returns:
        np.ndarray: Numerical solution of the ODE in the interval [t0, t0+h, t-h, t].
    """
    t_ = np.arange(t0, t0+t, h) 
    N = len(t_)

    u = np.zeros_like(t_)
    u_previous = y0 - h * f(y0, t_[0])
    u[0] = y0
 
    for i in range(N-1):
        if i == 0:
            u[i+1] = u_previous +2 * h * f(u[i], t_[i])    
        else:
            u[i+1] = u[i-1] + 2 *h * f(u[i], t_[i])
    
    return u, t_

def euler_explicit(f:'Callable[float, float]', y0:float, t0:float, t:float, h:float)-> np.ndarray:
    """Computes the explicit (forward) Euler method to solve ODEs.

    Args:
        f (Callable[float, float]): Function depending on y and t in that order.
            Equivalent to f(y,t).
        y0 (float): Initial value of the answer.
            Equivalent to y(t0).
        t0 (float): Initial time.
        t (float): Final time.
        h (float): Separation between the points of the interval.

    Returns:
        np.ndarray: Numerical solution of the ODE in the interval [t0, t0+h, t-h, t].
    """
    t_ = np.arange(t0, t0+t, h) 
    N = len(t_)

    u = np.zeros_like(t_)
    u[0] = y0
 
    for i in range(N-1):
        u[i+1] = u[i] + h * f(u[i], t_[i])
    
    return u, t_

def euler_explicit_systems(f:'Callable[float, ...]', vec0:np.ndarray, t0:float, t:float, h:float)-> np.ndarray:

    t_ = np.arange(t0, t0+t, h)  
    N = len(t_)

    u = np.zeros((vec0.shape[0], N))

    u[:, t0] = vec0
 
    for i in range(N-1):
        u[..., i+1] = u[..., i] + h * f(*u[..., i])
    
    return u, t_


def exercise1(section, method):

    if section==1:
            
        h = [0.5, 0.25, 0.1]
        t0, t = 0, 1
    elif section==2:
        h = [0.1]
        t0, t = 0, 100  
    
    y0 =1
    f = lambda y, t: -y

    for hi in h:
        sol = method(f, y0, t0, t, hi)
        plt.plot(sol[1], sol[0], label=f'{hi}')
    
    t= np.arange(t0, t+ 0.001, 0.001)

    plt.plot(t, np.exp(-t), label='analytical')

    plt.legend()
    plt.show()



def exercise2():

    t0, tf = 0, 50
    vec0 = np.array([0, 1, 1.05])

    s, r, b = 10, 28, 8/3

    f = lambda x, y, z: np.array([s*(y-x), x*(r-z)-y, x*y - b*z])
    
    h = 1e-4

    u, _ = euler_explicit_systems(f, vec0, t0, tf, h)

    fig = plt.figure(figsize = (10,10))

    ax = plt.axes(projection='3d')

    ax.grid()

    ax.plot3D(u[0,:], u[1, :], u[2, :])

    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)

    plt.show()


if __name__=='__main__':
    
    # exercise1(1, euler_explicit)
    exercise2()