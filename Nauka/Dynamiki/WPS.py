A = [ [6,2,8,9], [8,1,3,2], [4,7,2,6], [1,5,7,4]]

def wedrowka(A):
    n = len(A)
    F = [ [0 for _ in range(n)] for _ in range(n)]
    F[0][0] = A[0][0]

    for i in range(1,n):
        F[i][0] = F[i-1][0] + A[i][0]
        F[0][i] = F[0][i-1] + A[0][i]

    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = A[i][j] + min(F[i-1][j], F[i][j-1])

    return F[n-1][n-1]

print(wedrowka(A))
