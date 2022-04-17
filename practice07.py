import numpy as np
import sys


from practice03 import dev, newton



class NoRootException(Exception):
    pass

def parse_f(str, iterator, *args):

    ans = str
    for var in args:
        ans = ans.replace(var, f'{var}[{iterator}]')

    return ans

def dev_str(x:float, f_str:str, h:float = 10**(-3))-> float:
    '''Computes the derivate of f_str at x.
    Remarks: 
        - f_str depends on u[i+1], that is its variable, i.e. f_str(u[i+1])
    '''
    f_dev_str_h = f_str.replace("u[i+1]", "x+h")
    f_dev_str = f_str.replace("u[i+1]", "x")
 
    return ( eval( f_dev_str_h ) - eval( f_dev_str ) ) / h

newton_cache = {}
def newton_str(f:any, err:float, x0:float = 0) -> float:
    
    if len(newton_cache) == 0:
        newton_cache[1] = x0

    last_index = len(newton_cache)
    last_newton = newton_cache[last_index]    

    newton_cache[last_index + 1] = last_newton - f(last_newton) / dev_str(last_newton, f)

    if abs(newton_cache[len(newton_cache)] - newton_cache[len(newton_cache) - 1]) < err:
        return newton_cache[last_index + 1] # +1 ?

    if last_index + 10 > sys.getrecursionlimit():
        raise NoRootException('Could not find a root. Maybe there are none.')

    newton_str(f, err)




def euler_explicit(f_t_y:str, y0:float, t0:float, t:float, h:float)-> list:

    t_ = np.arange(t0, t+h, h)
    N = len(t_)

    u = np.zeros_like(t_)
    u[0] = y0

    # f = parse_f(f_t_y, 'i', 'y', 't_')   
    f = eval('lambda y, t: ' + f_t_y)

    for i in range(N-1):
        # u[i+1] = u[i] + h * eval(f)
        u[i+1] = u[i] + h * f(u[i], t_[i])
    
    return u


def euler_implicit(f_t_y:str, y0:float, t0:float, t:float, h:float)-> list:
    
    global t_, i, h_

    t_ = np.arange(t0, t+h, h)
    N = len(t_)

    u = np.zeros_like(t_)
    u[0] = y0
        
    f = eval('lambda y: ' + f_t_y.replace("t", "t_[i+1]"))

    i = 0
    h_ = h

    for j in range(N-1):        
        i = j

        # g = -u[i+1] + u[i] + h * f(u[i+1], t_[i+1])
        g_newton = eval('lambda y: ' + "h_ *" + f_t_y.replace("t", "t_[i+1]") + '-y ' + f'+ {u[i]}' ) #This magic works, or not. Look 
        
        u[i+1] = newton(g_newton, 0.01, u[i])

    return u




if __name__ == '__main__':
    
    f_t_y = "- (3* t**2 * y + y**2) / (2* t**3 + 3* t*y)"
    h_vec = [0.0001, 0.001, 0.01, 0.1]

    for hi in h_vec:

        # print(f"Euler explicit wit h={hi} yields {euler_explicit(f_t_y, -2, 1, 2, hi)}")
        print(f"Euler implicit wit h={hi} yields {euler_implicit(f_t_y, -2, 1, 2, hi)}")    
        
    