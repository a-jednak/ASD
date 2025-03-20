# Program tworzy tablicę 'help' rozmiaru p, będzie ona zawierać w sobie kolejne p elementów danej nam
# tablicy T. 'help' jest zawsze posortowana by łatwo móc znaleźć k-ty największy element. W zmiennej x
# zapisujemy ostatni element zbioru, który usuniemy przy następnym przejściu. W pętli pobieramy kolejny 
# elemnt z tablicy T i wstawiamy go w odpowiednie miejsce posortowanej tablicy help.
# Złożoność czasowa: (n-p)logp + nlogn -> nlogn

from zad2testy import runtests

def mergeSort(T):
    if len(T) > 1:
        mid = len(T)//2
        L = T[:mid]
        R = T[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1

def binSearch(T, k, val):
    p = 1
    while (p < k):
        mid = (p + k) // 2
        if(T[mid - 1] < val):
            p = mid + 1
        else:
            k = mid
    if p == k:
        return p-1
    return p


def ksum(T, k, p):
    sum = 0
    help = []
    for i in range(p):
        help.append(T[i])

    mergeSort(help)
    sum += help[p-k]
    x = binSearch(help, p, T[0])
    for i in range(len(T)-p):
        del help[x]  
        y = binSearch(help,p, T[i+p])            
        help.insert(y,T[i+p])
        sum += help[p-k]
        x = binSearch(help, p, T[i+1])

    return sum

runtests( ksum, all_tests=True )
