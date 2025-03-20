# Merge Sort

class Node:
    def __init__(self, val,next):
        self.next = next
        self.val = val

# Na listach
def MergeSortList(a):
    h = Node(None,None)
    h.next = a
    e = end(a)
    while True:
        q = extract(a)
        if q == None:
            return a
        z = extract(q)
        x = merge(a,q)
        if z == None:
            return x
        e.next = x
        e = end(x)
        a = z


def end(a):
    while a.next != None:
        a = a.next
    return a

def extract(a):
    while a.next != None and a.next.val >= a.val:
        a = a.next
    q = a.next
    a.next = None
    return q

def merge(p1, p2):
    h = x = Node(None,None)
    h.next = x
    while p1 != None and p2 != None:
        if p1.val < p2.val:
            x.next = p1
            p1 = p1.next
        else:
            x.next = p2
            p2 = p2.next
        x = x.next

    if p1 != None:
        x.next = p1
    if p2 != None:
        x.next = p2

    return h.next

"""
a = Node(3, None)
b = Node(4, a)
c = Node(31, b)
d = Node(17,c)
e = Node(0,d)
f = Node(69,e)

def printlist(h):
    while h != None:
        print(h.val)
        h = h.next

printlist(f)
printlist(MergeSortList(f))
"""

# Na tablicy

def MergeSort(a):
    n = len(a)
    if n > 1:
        mid = n//2
        Left = a[:mid]
        Right = a[mid:]

        MergeSort(Left)
        MergeSort(Right)

        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                a[k] = Left[i]
                i += 1
            else:
                a[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):
            a[k] = Left[i]
            k += 1
            i += 1
        while j < len(Right):
            a[k] = Right[j]
            k += 1
            j += 1


