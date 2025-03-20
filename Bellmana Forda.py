graf = [ [(1, 10), (5, 8)], [(3, 2)], [(1,1)], [(2,-2)], [(1, -4), (3, -1)], [(4,1)]]
# tablica tablic - wierzcholkow w ktorych sa zapisane krawedzie w formie (do kogo, waga)

def BellmanFord(G, s):
    V = len(G) #ilosc wierzcholkow
    d = [float('inf') for _ in range(V)]
    p = [None for _ in range(V)]
    d[s] = 0

    for _ in range(V-1):
        for u in range(V):
            W = G[u]
            for k in range(len(W)):
                v, c = W[k]
                if d[v] > d[u] + c:
                    d[v] = d[u] + c
                    p[v] = u

    for i in range(V):
        W = G[i]
        for j in range(len(W)):
            v, c = W[j]
            if d[v] > d[i] + c:
                print("Cykl ujemny!")
                return False
        
    print(d)
    return
            
BellmanFord(graf,0)