from zad4testy import runtests


def Flight(L,x,y,t):
  N = len(L)
  visited = [0 for _ in range(N)]
  flag = False

  def DFSvisit(L, u, minp):
    nonlocal flag
    visited[u] = 1
    sasiad = []
    for i in range(N):
      e = L[i]
      if e[0] == u:
        sasiad.append((e[1],e[2]))
      if e[1] == u:
        sasiad.append((e[0],e[2]))
      if e[0] > u:
        break
        
    for i in range(len(sasiad)):
      tmp = sasiad[i]
      p = tmp[1]
      minp = min(minp, p)
      if tmp[0] == y and abs(p-minp) <= t*2:
        flag = True
        
      if visited[tmp[0]] == 0 and (u==x or abs(p-minp) <= t*2):
        DFSvisit(L, tmp[0], minp)
        
        
        

  DFSvisit(L, x, 100000000000)
  return flag
  



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
