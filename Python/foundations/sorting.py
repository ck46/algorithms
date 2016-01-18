# -*- coding: utf-8 -*-

class Sorting(object):
    def __init__(self, lst=[]):
        self.lst = lst
        self.size = len(lst)

    ## Insertion Sort Algorithm
    def insertion(self):
        A = list(self.lst)
        for j in range(1, self.size):
            key = A[j]
            i = j-1
            while i>=0 and A[i]>key:
                A[i+1] = A[i]
                i -= 1
            A[i+1] = key
        return A

    ## Merge Sort Algorithm
    def merge(self):
        return self.lst

    ## Bubble Sort Algorithm
    def bubble(self):
        return self.lst
    pass

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [A[p+i-1] for i in range(n1)]
    R = [A[q+j] for j in range(n2)]
    L.append(1000)
    R.append(1000)
    i = 0
    j = 0
    #lst = list(A)
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge_sort(A):
    p = 0
    r = len(A)
    lst = list(A)
    merge_sort_helper(lst, p, r)
    return lst

def merge_sort_helper(A, p, r):
    if p < r:
        q = (p + r)/2
        merge_sort_helper(A, p, q)
        merge_sort_helper(A, q+1, r)
        merge(A, p, q, r)
        print A[q:r]


A = Sorting([5,2,4,6,1,3])
# print A.insertion()
B = [5, 2, 4, 7, 1, 3, 2, 6]
print merge_sort(B)
