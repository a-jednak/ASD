# Złożoność O(nm)
# Funkcja minimum(T,x) znajduje minimalna wartosc z x'tego wiersza tablicy T (jest uzyta tylko do znalezienia koncowego wyniku)
# Funkcja minimum2(T) zapisuje do tablicy A jaka jest dotychczas najmniejsza wartosc przed aktualnym indeksem, ulatwia to 
# znalezienie najmniejszych dystansow bez przypadkowego przypisania do jednego miejsca parkingowego dwoch budynkow
# W funkcji parking(X,Y) wierszami(budynkami) wypelniana jest tablica F[i][j], ktora przetrzymuje najmniejsza mozliwa sume odleglosci
# gdy budynek[i] jest przypisany do parkingu[j]

from zad8testy import runtests

def minimum(T, x):
    res = float('inf')
    index = 0
    for i in range(x):
        if res > T[i]:
            res = T[i]
            index = i

    return res, index

def minimum2(T):
    mini = float('inf')
    n = len(T)
    A = [0 for _ in range(n)]
    for i in range(n-1):
        mini = min(mini, T[i])
        A[i+1] = mini
    return A

def parking(X,Y):
    n = len(X)  
    m = len(Y)  
    F = [ [float('inf') for _ in range(m)] for _ in range(n)]
   
    for k in range(m):
        F[0][k] = abs(X[0]-Y[k])

    for i in range(1,n):
        Arr = F[i-1]
        M = minimum2(Arr)
        for j in range(m-1, i-1, -1):
            F[i][j] = abs(X[i]-Y[j]) + M[j]      
    x = minimum(F[n-1], m)
    return x[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
