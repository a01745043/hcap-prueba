import numpy as np
def convolucion(A,B):
        C = np.zeros((len(A)-2,len(A[0])-2))
        for i in range(0,(len(A)-2)) :
            for j in range(0,(len(A[0])-2)):
                C[i][j] = A[i+0][j+0]*B[0][0]+A[i+0][j+1]*B[0][1]+A[i+0][j+2]*B[0][2]+A[i+1][j+0]*B[1][0]+A[i+1][j+1]*B[1][1]+A[i+1][j+2]*B[1][2]+A[i+2][j]*B[2][0]+A[i+2][j+1]*B[2][1]+A[i+2][j+2]*B[2][2]
        return C

Matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]
A = np.array(Matriz1)
B =np.array(Filtro)

print(convolucion(A,B))
