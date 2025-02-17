

import numpy as np
import matplotlib.pyplot as plt

#numpy.matmul(A, B) : matrismultiplikation mellan två matriser
#matplotlib.pyplot.scatter(x, y) : skapar ett punktdiagram med punkter vid koordinaterna (x, y)
#numpy.random.rand(d0, d1, ...) : genererar en matris med slumpmässiga tal
#numpy.zeros(shape) : skkapar en matris fylld med nollor av angiven shape

def conditions(A,v,n):
    if isinstance(n, int) and n > 0:
        if len(v) == 2:
            if len(A)==2 and len(A[0])==2 and len(A[1])==2:
                return A,v,n
            else:
                print("A must be 2x2 matrix")
        else:
            print("v must be a 2-vector")
    else:
        print("n must be positive integer")

def generate_vectors(A, v0, n):
    # Skapa en matris för att lagra vektorerna
    vectors = np.zeros((2, n))
    vectors[:, 0] = v0  # Sätt första vektorn till v0
    
    # Generera resterande vektorer rekursivt
    for k in range(1, n):
        vectors[:, k] = np.matmul(A, vectors[:, k-1])
    
    return vectors

# Testa funktionen
A = np.array([[0.85, 0.04], [-0.04, 0.85]])  # Exempel på 2x2-matris
v0 = np.array([0, 0])  # Startvektor
n = 10000  # Antal vektorer

vectors = generate_vectors(A, v0, n)

# Plotta vektorerna
plt.scatter(vectors[0, :], vectors[1, :], s=0.1)
plt.show()


def barnsley_fern(n):
    # Definiera matriser och vektorer för de fyra affina transformationerna
    A1 = np.array([[0, 0], [0, 0.16]])
    A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
    A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
    A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])
    
    b1 = np.array([0, 0])
    b2 = np.array([0, 1.6])
    b3 = np.array([0, 1.6])
    b4 = np.array([0, 0.44])

    # Initialisera startvektor
    v = np.array([0, 0])
    
    # Lista för att lagra alla vektorer
    points = []
    
    # Generera n punkter
    for _ in range(n):
        r = np.random.rand()  # Slumpa ett tal mellan 0 och 1
        if r < 0.01:
            A = A1
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
        
        # Uppdatera vektorn
        v = np.matmul(A, v) + b
        points.append(v)
    
    points = np.array(points)
    
    # Plotta punkterna
    plt.scatter(points[:, 0], points[:, 1], s=0.1)
    plt.show()

# Testa genereringen av fraktalen med 10 000 punkter
barnsley_fern(10000)

# def bruh(A, v, n):
#     A,v,n = conditions(A,v,n)
#     vector_list = []