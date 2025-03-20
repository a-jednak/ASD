from zad4ktesty import runtests

def falisz ( T ):
    n = len(T)
    F = [ [0 for _ in range(n)] for _ in range(n)]

    for i in range(1,n):
        F[i][0] = F[i-1][0] + T[i][0]
        F[0][i] = F[0][i-1] + T[0][i]

    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = T[i][j] + min(F[i-1][j], F[i][j-1])

    return F[n-1][n-1]

runtests ( falisz )
