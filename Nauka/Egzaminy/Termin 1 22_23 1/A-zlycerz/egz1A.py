# Program używa algorytmu Dijkstry by znaleźć najkrótsze ścieżki
# By znaleźć wszystkie możliwe koszta (biorąc pod uwagę jeden rabunek po drodze) wystarczy puścić dwa razy Dijkstrę po dwóch grafach
# Pierwsza Dijkstra idzie z grafu G danego na wejściu, szuka ona najkrótszych ścieżek zanim złycerz okradł jakikolwiek zamek
# Następnie tworzymy drugi graf NG, który jest kopią G, ale z cenami krawędzi takimi jak po kradzieży
# Puszczamy Dijkstrę po NG, zaczynając z wierzchołka t, dzięki temu możemy połączyć Dist[i] i StealDist[i] - będzie to ścieżka
# startująca w s, przechodząca przez zamek i (kradzież) i kończąca się w t
# Szukając wyniku patrzymy na minimum z Dist[i]+StealDist[i] - V[i], czyli wszystkie ścieżki z kradzieżami w i'tym zamku odejmując
# skradzione złoto.
# Złożoność obliczeniowa: O(ElogV)
# Złożoność pamięciowa: O(VE)

from egz1Atesty import runtests
from queue import PriorityQueue

def Dijkstry(G,s):
    n = len(G)
    D = [float('inf') for _ in range(n)]
    D[s] = 0
    Q = PriorityQueue()
    Q.put((D[s],s))
    while not Q.empty():
        w, u = Q.get()
        if w == D[u]:
            for v,c in G[u]:
                if relax(D,v,u,c):
                    Q.put((D[v],v))
    return D

def relax(D,v,u,c):
    if D[v] > D[u] + c:
        D[v] = D[u] + c
        return True
    return False

def gold(G,V,s,t,r):
    Dist = Dijkstry(G,s)  #najtansze sciezki bez kradziezy
    n = len(G)

    # modyfikujemy graf, tak jakby złyczerz obrabował jakiś zamek
    NG = [ [ [0,0] for _ in range(len(G[i])) ] for i in range(n)]

    for i in range(n):
        d = len(G[i]) #stopień wierzchołka
        for j in range(d):
            NG[i][j][0] = G[i][j][0]
            NG[i][j][1] = G[i][j][1]*2 + r

    StealDist = Dijkstry(NG,t)   # najtansze sciezki z punktu koncowego (w koncu po kradziezy mamy skonczyc w t)
    
    res = float('inf')
    for i in range(n):
        res = min(res, Dist[i]+StealDist[i]-V[i])
          
    return res


#zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
