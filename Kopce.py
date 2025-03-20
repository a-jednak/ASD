#KOPCE

def swap(T, x, y):
    T[x], T[y] = T[y], T[x]

def parent(x):
    res = (x-1)//2
    return res

def heapify(A, n, i):
    l = 2*i + 1
    r = 2*i + 2
    max_ind = i
    if l<n and A[l] > A[max_ind]:
        max_ind = l
    if r<n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        swap(A, i, max_ind)
        heapify(A, n, max_ind)

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A,n,i)

T = [3,12,6,7,32,89,3,10,2,4,55,23,1,17]
A = [7,9,1,5,8]
buildheap(A)
print(A)

