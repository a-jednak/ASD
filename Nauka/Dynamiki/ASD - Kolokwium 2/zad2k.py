# Zlozonosc O(n^2)

from zad2ktesty import runtests

def palindrom( S ):
    n = len(S)
    res = ""
    l = len(res)
    F = [ [None for _ in range(n)] for _ in range(n)]
    
# Wersja iteracyjna:
# [0.32 sek]

    for i in range(n):
        F[i][i] = True

    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if i+1 == j:
                if S[i] == S[j]:
                    F[i][j] = True
                else:
                    F[i][j] = False
            else:
                if S[i] != S[j]:
                    F[i][j] = False
                else:
                    F[i][j] = F[i+1][j-1]

            if F[i][j] == True and len(S[i:j+1]) > l:
                res = S[i:j+1]
                l = len(res)

    #print(F)
    
# Wersja rekurencyjna:
# [0.46 sek]
    """
    def rekPal(S, s,k):
        if s == k:
            return True
        elif s+1 == k:
            return True if S[s] == S[k] else False
        else:
            if S[s] != S[k]:
                return False
            else:
                return rekPal(S, s+1, k-1)
            
    for i in range(n):
        for j in range(i,n):
            F[i][j] = rekPal(S, i, j)
            if F[i][j] == True and len(S[i:j+1]) > l:
                res = S[i:j+1]
                l = len(res)
    """
    return res

runtests ( palindrom )

#s = "aacaccabcc"
#print(palindrom(s))