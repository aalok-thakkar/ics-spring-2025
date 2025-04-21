# Lecture 21, April 10

from typing import List

def is_sorted (l: List[int]) -> bool:
    n = len(l)
    for i in range(n):
        # we are checking if l[i] <= l[i+1]. If so, do nothing. Otherwise:
        if i + 1 < n - 1:
            if l[i] > l[i+1]:
                return False
    return True


def quick_sort(l: List[int]) -> None:

    def partition(start: int, end: int) -> int:
        # assumptions: start < len(l) and end < len(l)
        # end > start
        # forall(isinstance(x, int) for x in l)
        l_being_partitioned = l[start: end+1]
        pivot = l[start]
        i = start + 1
        j = end

        # [7, 3, 18, 6, 14, 3], start = 0, end = 5
        # pivot = 7
        # i0 = start + 1 = 1
        # j0 = end = 5

        while i <= j:
            # for all x in l[start+1: i], x <= pivot
            # for all x in l[j+1: end + 1], x > pivot (or (j < end -> for all x in l[j+1:end+1], x > pivot)
            # i + 1 <= j
            # j > start
            if l[i] <= pivot:
                i += 1
            elif l[j] > pivot:
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            
            # for all x in l[start+1: i+1], x <= pivot
            # for all x in l[j: end + 1], x > pivot

        # for all x in l[start+1: i], x <= pivot
        # for all x in l[j + 1: end + 1], x > pivot
        # (i > j) and (i + 1 <= j) -> i + 1 = j

        # therefore, 
        # for all x in l[start+1: j + 1], x <= pivot
        # for all x in l[j + 1: end + 1], x > pivot

        # What about l[j]? This lies in l[start+1: j + 1]. From the invariant. j > start.
        # Therefore l[j] < pivot

        l[start], l[j] = l[j], l[start]

        # for all x in l[start: j], x <= pivot
        # jth element is the pivot
        # for all x in l[j + 1: end + 1], x > pivot

        # guarantee:
        # let p be the index of the pivot after the function call
        # for all i < p, l[i] <= l[p]
        # for all i > p, l[i] > l[p]
        return j
    
    def sort(start: int, end: int) -> None:
        # assume forall(isinstance(x) for x in l)
        if start >= end:
            return
        
        # singleton lists are sorted. This is the base case. 

        pivot_index = partition(start, end)
        # by guarantee of partition, 
        # forall x in l[start, pivot_index - 1], x <= pivot
        # # forall x in l[pivot_index+1, end + 1], x > pivot

        sort(start, pivot_index - 1)

        # if the guarantee holds for the recursive call of sort, then 
        # l[start, pivot_index - 1] is sorted
        sort(pivot_index + 1, end)

        # if the guarantee holds for the recursive call of sort, then 
        # l[pivot_index + 1, end + 1] is sorted

        # therefore we have: 
        # guarantee: is_sorted(l[start, end+1])
        
    # start = 0
    # end = len(l) - 1
    # from guarantee of sort
    sort(0, len(l) - 1)

# Can we force the best case of QuickSort every time? Kinda.

# let rec merge (l1 : int list) (l2: int list) : int list = 
#   match l1 with
#   | [] -> l2
#   | h1 :: t1 -> 
#     match l2 with
#     | [] -> l1
#     | h2 :: t2 ->
#       match (h1 < h2) with
#       | true -> h1 :: h2 :: merge t1 l2
#       | false -> h2 :: h1 :: merge l1 t2
# ;;

# let rec split (l : int list) : (int list * int list) = 
#   match l with 
#   | [] -> ([], [])
#   | [x] -> ([x], [])
#   | x1 :: x2 :: xs -> let (left, right) = split xs in (x1 :: left, x2 :: right)
# ;;
 
# let rec mergesort (l : int list) : int list = 
#   match l with 
#   | [] -> []
#   | _ -> let (left, right) = split l in merge (merge_sort left) (merge_sort right)
# ;;

def merge_sort_in_place(l: List[int]) -> None:
    def merge(start: int, mid: int, end: int) -> None:
        left = l[start:mid+1]
        right = l[mid+1:end+1]

        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1

    def sort(start: int, end: int) -> None:
        if start >= end:
            return
        mid = (start + end) // 2
        sort(start, mid)
        sort(mid + 1, end)
        merge(start, mid, end)

    sort(0, len(l) - 1)

# What is the worst case time complexity of Merge Sort? T (n) = 2T(n/2) + c*n -> O(n log n) 
# What is k Merge Sort?

# Which is the best sorting algorithm?
# Selection Sort
# Bubble Sort
# Insertion Sort
# Quick Sort
# Merge Sort
# Any others?






# Applications:

"""
Problem: Count the number of index pairs (i, j) such that i < j and A[i] + A[j] ≤ K.

Input:
- n: number of elements
- A: list of n integers
- K: target sum

Output:
- One integer: number of valid pairs

Example:
Input:
5
[1, 3, 2, 5, 4]
6

Output:
6

Explanation:
Valid pairs: (1,3), (1,2), (1,4), (3,2), (3,4), (2,4)
"""



"""
Problem: Count the number of inversions in the array (i < j and A[i] > A[j]).

Input:
- n: number of elements
- A: list of integers

Output:
- One integer: number of inversions

Example:
Input:
5
[2, 4, 1, 3, 5]

Output:
3

Explanation:
Inversions: (2,1), (4,1), (4,3)
"""


"""
Problem: Given start and end times of meetings, return the minimum number of meeting rooms required.

Input:
- n: number of meetings
- intervals: list of tuples (start, end)

Output:
- One integer: minimum rooms needed

Example:
Input:
3
[(0, 30), (5, 10), (15, 20)]

Output:
2

Explanation:
(0-30) overlaps with both other meetings → need 2 rooms
"""
