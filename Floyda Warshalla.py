graf = [ [(2,-2)], [(0,4), (2,3)], [(3,2)], [(1,-1)]]

def FloydWarshall(G):
    V = len(G)
    d = [ [ float('inf') for _ in range(V)] for _ in range(V)]
    for i in range(V):
        d[i][i] = 0
    
    for i in range(V):
        u = G[i]
        for j in range(len(u)):
            v, w = u[j]
            d[i][v] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    print(d)


FloydWarshall(graf)