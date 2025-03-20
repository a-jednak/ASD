graf = [ [(1,3)], [(2,2), (3,5)], [(0,1)], [(2,4)]]

from queue import PriorityQueue

def relax(p, d, v, u, c):
    if d[v] > d[u] + c:
        d[v] = d[u] + c
        p[v] = u
        return True
    return False

def Dijkstry(G, s):
    V = len(G)
    d = [float('inf') for _ in range(V)]
    p = [None for _ in range(V)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((d[s], s))

    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v,c in G[u]:
                if relax(p,d,v,u,c):
                    Q.put((d[v], v))

    return d, p

print(Dijkstry(graf,0))
