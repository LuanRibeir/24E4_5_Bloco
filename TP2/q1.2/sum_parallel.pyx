from cython.parallel import prange
import numpy as np
cimport numpy as np

def soma_sequencial(np.ndarray[int, ndim=1] vetor):
    cdef int i, soma = 0
    for i in range(vetor.shape[0]):
        soma += vetor[i]
    return soma

def soma_paralela(np.ndarray[int, ndim=1] vetor):
    cdef int i, soma = 0
    for i in prange(vetor.shape[0], nogil=True):
        soma += vetor[i]
    return soma

