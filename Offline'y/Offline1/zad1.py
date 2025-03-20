# OPIS:
# Algorytm sprawdza czy k jest równe 0 (przypadek gdzie lista jest posortowana). Jeśli k jest
# różne od 0, sortuje listę używając sortowania przez scalanie.
# Złożoność algorytmu dla:
# k = Θ(1)      wynosi O(nlogn)
# k = Θ(log n)  wynosi O(nlogn)
# k = Θ(n)      wynosi O(nlogn)

from zad1testy import Node, runtests          

def SortH(p,k):
    if k == 0:
        return p

    def merge(p1,p2):
        head = x = Node()
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else: 
                head.next = p2
                p2 = p2.next
            head = head.next

        if p1 != None:
            head.next = p1
        
        if p2 != None:
            head.next = p2
        
        return x.next

    def extract(a):
        while a.next != None and a.next.val >= a.val:
            a = a.next
        
        q = a.next
        a.next = None
        return q
    
    def end(a):
        while a.next != None:
            a = a.next

        return a

    def mergeSort(a):
        h = Node()     
        h.next = a        #dolaczamy wartownika (nie bedzie w finalnym rozwiazaniu)
        e = end(a)
        while True:
            q = extract(a)
            if q == None:
                return a 
            z = extract(q)
            x = merge(a,q)
            if z == None:
                return x
            e.next=x
            e = end(x)
            a = z

    return mergeSort(p)

    pass 


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )        