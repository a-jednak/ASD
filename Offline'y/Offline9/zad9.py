# Zlozonosc O(mnlog(mn))

from zad9testy import runtests

def trip(M):
    n = len(M) #ile wierszy
    m = len(M[0]) #ile kolumn

    F = [ [1]*m for _ in range(n)]    
    S = [(M[i][j], i, j) for i in range(n) for j in range(m)]      # S - szczyty

    S.sort()  #Sortuje S na podstawie M[i][j]
    
    kierunki = [(1,0), (-1,0), (0,1), (0,-1)] #(x,y)

    for h, x, y in S:
        for kx,ky in kierunki:
            w = x+kx
            k = y+ky
            if 0 <= k < m and 0 <= w < n and h < M[w][k]:
                    F[w][k] = max(F[w][k], F[x][y]+1)

    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res, F[i][j])  

    #print(F)
    #print(S)

    return res
    
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )

M = [ [7,6,5,12],
[8,3,4,11],
[9,1,2,10] ]

#print(trip(M))
