# Dynamik O(n^2)

from zad1ktesty import runtests

def roznica( S ):
    n = len(S)
    F = [ [ 0 for _ in range(n)] for _ in range(n)]
    maks = 0


    for a in range(n):
        for b in range(a,n):
            x = S[b]
            if x == '0':
                x = -1
            else:
                x = 1
            F[a][b] = F[a][b-1] + x
            maks = max(maks, abs(F[a][b]))

   
    return maks if maks < n else -1

runtests ( roznica )
# testy chyba mogą być schrzanione