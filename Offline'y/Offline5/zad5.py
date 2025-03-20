# Program przekrztałca dane wejściowe aby mieć łatwy dostęp i wyobrażenie grafu, a następnie stosuje algorytm Dijikstra,
# który zapisuje w tablicy najkrótsze (w tym wypadku o najmniejszym czasie) trasy z punktu a, do każdego innego punktu grafu.
# Z tablicy odpowiedzią jest wartość przy indeksie b (naszego punktu końcowego)

from zad5testy import runtests
from queue import PriorityQueue

def WygodnaForma(A, TP):
    N = len(A)
    VerCnt = 0
    for i in range(N):
        x = A[i]
        VerCnt = max(x[1], x[0], VerCnt)
    WF = [ [] for _ in range(VerCnt+1)]
   
    for i in range(N):
        x = A[i]
        WF[x[0]].append((x[1],x[2]))
        WF[x[1]].append((x[0],x[2]))

    for i in range(len(TP)):
        for j in range(len(TP)):
            if i != j:
                WF[TP[i]].append((TP[j], 0))
    return WF


def Dijikstra(T, a):
    N = len(T)
    time = [float('inf') for _ in range(N)] 
    time[a] = 0
    Q = PriorityQueue()
    Q.put((0,a))
    while not Q.empty():
        x = Q.get()
        w = x[0]
        u = x[1]
        if w == time[u]:
            for v,c in T[u]:
                if relax(time, v, c, u):
                    Q.put((time[v], v))
    return time


def relax(time, v, c, u):
    #print(v, c, u)
    if time[v] > time[u] + c:
        time[v] = time[u] + c
        return True
    return False


def spacetravel( n, E, S, a, b ):
    
    T = WygodnaForma(E,S)
    Time = Dijikstra(T,a)

    return Time[b] if Time[b] != float('inf') else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests = True )

