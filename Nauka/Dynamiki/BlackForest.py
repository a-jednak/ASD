Las = [45,16,50,69,3,14,15,20,4,3]

def ScinamyDrzewa(A):
    n = len(A)
    F = [0 for _ in range(n)] #co jak scinamy drzewo i-te
    G = [0 for _ in range(n)] #co jak nie scinamy drzewka
    F[0] = A[0]

    for i in range(1,n):
        F[i] = G[i-1] + A[i]
        G[i] = max(F[i-1], G[i-1])

    return max(F[n-1], G[n-1])

print(ScinamyDrzewa(Las))