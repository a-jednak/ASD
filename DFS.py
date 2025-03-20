#pseudokod
"""
def DFS(G):
    # G = (V,E)

    def DFSvisit(G, u):
        nonlocal time
        time += 1
        u.visited = True
        for v sasiaduje z u:
            if not v.visited:
                v.parent = u
                DFSvisit(G,v)
        time += 1

    for v in V:
        v.visited = False
        v.parent = None
    
    time = 0
    for u in V:
        if not u.visited:
            DFSvisit(G,u)
"""
#implementacja dla offline 4

def DFS(L):
    N = len(L)
    visited = [0 for _ in range(N)]
    time = 0

    def DFSvisit(L, u):
        nonlocal time
        time += 1
        visited[u] = 1
        sasiad = []
        for i in range(N):
            e = L[i]
            if e[0] == u:
                sasiad.append((e[1],e[2]))
            if e[0] > u:
                break
        
        for i in range(len(sasiad)):
            if visited[sasiad[i]] == 0:
                DFSvisit(L, sasiad[i])

        time += 1
    
    time = 0
    DFSvisit(L,x)
