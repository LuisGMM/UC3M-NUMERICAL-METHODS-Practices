import numpy as np


# TODO: Check the similarity between horner algo and the euler formula we derived years ago.  

# TODO: Test if it is well implemented.

def horner(x:list, y:list) -> np.array:
    """ Computes Horner's algorithm for some given coordinates.

    'x' and 'y' must have the same length.

    Args:
        x(list(float)): x coordinates of the points.
        y(list(float)): y coordinates of the points.

    Returns: 
        list: with the polynomial coefficients of the Newton interpolation.
    
    """
    LEN = len(y)
    matrix = np.zeros((LEN, LEN))

    #matrix column -> j
    for j in range(LEN): 
        if j == 0:   
            matrix[:,1] = y
        
        #matrix row -> i
        for i in range(LEN-j): 

            matrix[i, j] = (matrix[i+1,j] - matrix[i,j] ) / (x[i+1] - x[i] )

    return matrix[0]

def eval_horner(x, x_points:list = None, y_points:list = None, coeffs:list = None) -> float:
    """ Evaluates the polynomial returned by Horner's algorithm.

    If no coefficients are given this method will compute them

    Args:
        x(float): The points to evaluate the polynomial.
        x(list(float)): x coordinates of the points.
        y(list(float)): y coordinates of the points.
        coeffs(list(float)): coefficients of the polynomial.

    Returns:
        float: the polynomial evaluated at x.
    
    """
    coeffs_ = coeffs if coeffs is not None else horner(x_points, y_points)

    N = len(x_points) - 1
    polynom = coeffs_[N]
    
    for k in range(1,N+1):
        polynom = coeffs_[N-k] + (x -x_points[N-k])*polynom
    
    return polynom




if __name__ == '__main__':
    pass

