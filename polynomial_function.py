from matplotlib import pyplot as plt
import numpy as np


def get_k_polynomial_with_d_features(feature_set, k):
    A = feature_set[0] ** 0
    numOfSamples=feature_set.shape[1]
    if k==0:
        return A.T
    A=np.vstack((A, feature_set))
    if k==1:
        return A.T
    previous_new_terms=feature_set.copy()
    for i in range(2, k+1):
        current_new_terms = []
        for j in range(0, feature_set.shape[0]):
            fproduct=np.array([])
            for v in previous_new_terms[j:]:
               fproduct = np.append(fproduct,np.multiply(v, feature_set[j]))
            fproduct.shape = (-1, numOfSamples)
            A = np.vstack((A,fproduct))
            current_new_terms.append(fproduct)

        previous_new_terms = current_new_terms.copy()
    return A.T


A=np.array([[1,2,3],[4,5,6],[4,3,4],[2,4,6]])
A=get_k_polynomial_with_d_features(A,23)
print(A.shape[1])
