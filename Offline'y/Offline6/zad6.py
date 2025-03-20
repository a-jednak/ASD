from queue import PriorityQueue
from zad6testy import runtests

def Dijkstry(G, s, butki, N):
    d = [float('inf') for _ in range(N)] #dystans
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s, butki))     # (dystans, wierzcholek, czy but dwumilowy)

    while not Q.empty():
        dyst, u, flag = Q.get() 
        if dyst == d[u]:
           for v, waga, buty in G[u]:
               #print(d)
               if flag != buty or flag == 0:
                    if relax(d,v,u,waga):
                        Q.put((d[v],v,buty))
    #print(d)
    return d
                       
def relax(d, v, u, waga):
    if d[v] > d[u] + waga:
        d[v] = d[u]+waga
        return True
    return False

def WygodnaForma(T):
    N = len(T)
    G = [ [] for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if T[i][j] != 0:
                G[i].append((j,T[i][j], 0))     # ( sąsiad, waga, buty )
                G[j].append((i,T[i][j], 0))

    for i in range(N):
        for j in range(N):
            if T[i][j] != 0:
                for k in range(N):
                    if T[j][k] != 0 and k != i:
                        G[i].append((k, max(T[i][j], T[j][k]), 1))
    #print(G)
    return G




def jumper( G, s, w ):
    N = len(G[0])
    T = WygodnaForma(G)
    a = Dijkstry(T,s,0,N)
    b = Dijkstry(T,s,1,N)

    res = min(a[w],b[w])
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )