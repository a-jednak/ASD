def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    
    A[i], A[r] = A[r], A[i]
    return i

def Kty(T, l, r, k):
    i = partition(T, l, r)
    if i-l == k-1:
        return T[i]
    
    if i-l > k-1:
        return Kty(T, l, i-1, k)
    
    return Kty(T, i+1, r, k-i+l-1)