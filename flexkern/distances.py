from __future__ import print_function
from scipy.spatial import distance

def distance(x, y, weights = [], p = 3, method = "euclidean"):
    '''

    :param weights:
    :param p:
    :param x: X vector
    :param y: Y vector
    :param method: Method to Find Distance
    :return: The Distance Value
    '''

    value = 0.00
    if method == "euclidean":
        value = distance.euclidean(x, y)
    elif method == "minkowski":
        value = distance.minkowski(x, y, p)
    elif method == "cosine":
        value  = distance.cosine(x, y)
    elif method == "manhattan":
        value = distance.cityblock(x, y)
    elif method == "dice":
        value = distance.dice(x, y)
    elif method == "jaccard":
        value = distance.jaccard(x, y)
    elif method == "hamming":
        value == distance.hamming(x, y)
    elif method == "canbera":
        value == distance.chebyshev(x, y)
    else:
        print(method, " Not Found! unsing Eclidean Distance!")
        value = distance.euclidean(x, y)
    return value
