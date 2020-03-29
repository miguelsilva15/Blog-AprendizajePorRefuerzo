import numpy as np

def e_greedy(Q, epsilon, nA, observation):
    '''Retorna la mejor acción dada la politica Q, esto 
    siempre con la probabilidad epsilon de elegir una acción
    al azar'''
    A = np.ones(nA) * epsilon / nA
    best_action = np.argmax(Q[observation])
    A[best_action] += (1.0 - epsilon)
    return A