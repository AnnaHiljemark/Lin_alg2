import numpy as np
import matplotlib.pyplot as plt

def vectors(A, v0, n):

    vectors = np.zeros((2, n))  # Skapar en tom 2x2-matris
    vectors[:, 0] = v0  # Sätter första vektorn till v0
    
    for k in range(1, n):
        vectors[:, k] = np.matmul(A, vectors[:, k-1])  # Multiplicerar med A rekursivt
    
    return vectors #Returnerar alla vektorerna

def barnslay(n):

    A1 = np.array([[0, 0], [0, 0.16]])
    A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])  
    A3 = np.array([[0.2, -0.26], [0.23, 0.22]])  
    A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])  
    
    b1 = np.array([0, 0])
    b2 = np.array([0, 1.6])
    b3 = np.array([0, 1.6])
    b4 = np.array([0, 0.44])
    
    v = np.array([0, 0])  # Startvektor
    points = np.zeros((2, n))  # Skapar en matris för punkterna
    
    for i in range(n): 
        r = np.random.rand() #Genererar ett randomtal, om talet är inom sannolikheterna väljs någon av följande
        if r < 0.01:
            A= A1
            b = b1
        elif r < 0.86:
            A = A2
            b = b2
        elif r < 0.93:
            A = A3
            b = b3
        else:
            A = A4
            b = b4
        
        v = np.matmul(A, v) + b #Matris A multipiliceras med senaste vektorn och b adderas
        points[:, i] = v #Punkten sparas
    
    plt.scatter(points[0], points[1], s=0.1, color='darkgreen')
    plt.show()

barnslay(100000)

