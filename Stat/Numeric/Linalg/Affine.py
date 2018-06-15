import numpy as np


class Affine:
    """
    Affine transformations
    y = A*x+b
    """

    def __init__(self, A: np.ndarray, b: np.ndarray):
        self.__A = A
        self.__b = b

    @property
    def A(self):
        return self.__A

    @property
    def b(self):
        return self.__b

    @property
    def dim(self):
        return self.A.shape[0]

    def trans(self,x: np.ndarray) -> np.ndarray:
        return self.A.dot(x) + self.b

    def itrans(self,y: np.ndarray) -> np.ndarray:
        return np.linalg.solve(self.A,y-self.b)

    @staticmethod
    def default(n: int):
        """
        :param n: dimension
        :return: default transformation
        """

        A = np.eye(n)
        b = np.ones([n,1])

        return Affine(A,b)