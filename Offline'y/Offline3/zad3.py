# Liczy sumy prefiksowe dla x'ów oraz y'ów wszystkich punktów, s to ilość punktów które są dominowane - punkty dominujące P[i]

from zad3testy import runtests

def dominance(P):
    n = len(P)
    dom = (0,0)
    sumX = []
    sumY = []
    sumX.append(0)
    sumY.append(0)

    for i in range(n):
        x = P[i]
        a = sumX[-1]
        b = sumY[-1]
        sumX.append(x[0]+a)
        sumY.append(x[1]+b)

    maxS=0
    for i in range(n):
        x = P[i]
        s = sumX[min(n,x[0])-1] + sumY[min(n,x[1])-1] - n+1
        if s > maxS:
            maxS = s
            dom = x

    cnt = 0
    for i in range(n):
        x = P[i]
        if x[0] < dom[0] and x[1] < dom[1]:
            cnt += 1

    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

