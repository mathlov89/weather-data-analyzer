import numpy as np
import pandas as pd
from scipy.optimize import fmin_cg  # Nonlinear conjugate gradient method
from Numeric.Linalg.FinDiff import cdiff1D as diffop  # Finite difference matrix creation

class PoiFit:
    """
    Inhomogeneous Poisson process intensity estimator
    """

    __maxiter = 100  # Maximum number of iterations to perform.
    __gtol = 1e-5    # Stop when the norm of the gradient is less than gtol.
    __a = 100000   # Regulator multiplier

    def __init__(self, value: pd.Series):

        self.__events = value

    @property
    def events(self):
        """
        :return: vector of integers
        """
        return self.__events

    @events.setter
    def events(self, value: pd.Series):
        self.__events = value

    def fit(self)->pd.Series:

        x = self.events.as_matrix()

        # problem size
        n = len(x)

        # Sparse matrices of the appropriate size
        diff = diffop(n=n)  # Difference matrix
        lapl = -np.dot(diff.transpose(), diff)  # Discrete Laplacian

        def L(f: np.ndarray)->np.float64:
            """
            Regularized log-likelihood function
            :return:
            """
            df = diff.dot(f)
            return -0.5*x.dot(np.log(f**2))+0.5*f.dot(f)+0.5*PoiFit.__a*df.dot(df)

        def gradL(f: np.ndarray)->np.ndarray:
            """
            Gradient of the regularized log likelihood function
            :return:
            """

            return -x/f + f - PoiFit.__a*lapl.dot(f)

        # Initial guess
        r = 0.01
        f0 = np.sqrt((1-r)*x + r*np.mean(x)*np.ones(n))

        # Do optimization
        f = fmin_cg(L, f0, fprime=gradL, gtol=PoiFit.__gtol, maxiter=PoiFit.__maxiter, disp=False)
        retval = pd.Series(f**2.0, index=self.events.index)

        return retval
