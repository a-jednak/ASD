# Sortowanie przez zliczanie O(n+k)

def counting_sort(A, k):    #tablica zawiera liczby naturalne ze zbioru {0, ..., k-1}
    n = len(A)
    B = [None]*n
    C = [0]*k
    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    
    for i in range(n):
        A[i] = B[i]

A = [1,2,0,2,3,0,4,0]
k = 5
counting_sort(A, k)
print(A)