

import sys


class NoRootException(Exception):
    pass


def dev(x:float, f:any, h:float = 10**(-7))-> float:
    return ( f(x+h) - f(x) ) / h 

newton_cache = {}
def newton(f:any, err:float, x0:float = 0) -> float:
    
    if len(newton_cache) == 0:
        newton_cache[1] = x0

    last_index = len(newton_cache)
    last_newton = newton_cache[last_index]    

    newton_cache[last_index + 1] = last_newton - f(last_newton) / dev(last_newton, f)

    if abs(newton_cache[len(newton_cache)] - newton_cache[len(newton_cache) - 1]) < err:
        return newton_cache[last_index + 1] # +1 ?

    if last_index + 10 > sys.getrecursionlimit():
        raise NoRootException('Could not find a root. Maybe there are none.')

    newton(f, err, x0)




if __name__ == '__main__':

    def func(x):    return (x+1)**2 +1

    newton(func, 0.0001, 0)
