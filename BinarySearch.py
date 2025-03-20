def binarySearch(T, val, p, k):
    if p == k:
        if T[p] > val:
            return p
        return p+1
    
    if p > k:
        return p
    
    mid = (p+k)//2
    if T[mid] < val:
        return binarySearch(T, val, mid+1, k)
    elif T[mid] > val:
        return binarySearch(T, val, p, mid-1)
    else:
        return mid
    
def insertionSort(T):
    N = len(T)
    for i in range(1, N):
        val = T[i]
        j = binarySearch(T, val, 0, i-1)
        T = T[:j] + [val] + T[j:i] + T[i+1:]

    return T