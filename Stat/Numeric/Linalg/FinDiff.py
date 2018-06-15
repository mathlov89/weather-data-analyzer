"""
Finite difference methods sparse matrix library
"""
import numpy as np
from scipy import sparse

def cdiff1D(n: int, dx=1, boundary='Neumann', method='backward') -> sparse.dia_matrix:
    """
    :param n:
    :return: n x n discrete difference operator
    """

    if boundary is 'Neumann' and method is 'backward':
        d0 = [0] + (n-1)*[1]
        d1 = n*[-1]
        data = np.asarray([d0,d1])
        diags = np.asarray([0,-1])

        return (1/dx)*sparse.spdiags(data, diags, n, n)

    else:
        raise AttributeError('Method not yet implemented.')

