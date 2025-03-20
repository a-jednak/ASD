from zad3ktesty import runtests

def ksuma( T, k ):
    n = len(T)
    F = [0]*n
    for i in range(k):
        F[i] = T[i]
    
    for i in range(k, n):
        mini = F[i-1]
        for w in range(i-k, i):
            mini = min(mini, F[w])
            
        F[i] = T[i] + mini

    mini = F[n-1]
    for i in range(n-k,n):
        mini = min(mini, F[i])

    return mini
    
runtests ( ksuma )
