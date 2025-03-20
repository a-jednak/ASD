from zad7testy import runtests

def maze(L): 
    n = len(L)
    G = [ [0]*n for _ in range(n)]
    D = [ [0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                G[i][j] = float('-inf')
                D[i][j] = float('-inf')

    for w in range(1,n):
        G[w][0] += G[w-1][0] +1
        D[w][0] = float('-inf')
    
    for k in range(1,n):
        G[0][k] += G[0][k-1]+1
        D[0][k] += D[0][k-1]+1

    for x in range(1,n):
        if L[0][x] != '#':
            G[0][x] = max(G[0][x-1], D[0][x-1]) +1

        for y in range(1,n):
            lewo = max(G[y][x-1], D[y][x-1])
            gora = G[y-1][x]
            if L[y][x] != '#':
                G[y][x] = max(lewo, gora) +1
            
        if L[n-1][x] != '#':
            D[n-1][x] = max(G[y][x-1], D[y][x-1]) +1

        for y in range(n-2, -1, -1):
            lewo = max(G[y][x-1], D[y][x-1])
            dol = D[y+1][x]
            if L[y][x] != '#':
                D[y][x] = max(lewo, dol)+1

    res = G[n-1][n-1]
    return res if res > 0 else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )