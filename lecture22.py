# Lecture 22, April 15

# No class on Friday (April 18). Make up class to be scheduled on April 26 upon request.
# Anustubh Agnihotri will present on Data Science for Research in Social Sciences next Tuesday (April 22)
# Classes will be virtual on April 25 (and April 26 if conducted)

from typing import List

def quick_sort(l: List[int]) -> None:

    def partition(start: int, end: int) -> int:
        pivot = l[start]
        i = start + 1
        j = end

        while i <= j:
            if l[i] <= pivot:
                i += 1
            elif l[j] > pivot:
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            
        l[start], l[j] = l[j], l[start]
        return j
    
    def sort(start: int, end: int) -> None:
        if start >= end:
            return
        pivot_index = partition(start, end)
        sort(start, pivot_index - 1)
        sort(pivot_index + 1, end)

    sort(0, len(l) - 1)

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

# Binary Search 


# Now that we can sort lists... 

# l = [2, 4, 6, 10, 15, 54, 3535, 4334, 323299824]
# find 3 in l
# Compare 3 with l[4]. 3 < 15, so now? 
# Search 3 in l[0:4], that is [2, 4, 6, 10]
# Compare 3 with l[2], 3 < 6 ...



# rec def bin_search (x : int) (l : int list) : int option =
#     match l with 
#     | [] -> None
#     | [h] -> if h = x then Some 0 else None
#     | _ -> if (middle l) = x then Some (index of middle ...) else 
#                if (middle l < x) then (first_half length + 1 + (bin_search x (second_half l))) else (bin_search x (first_half l))
# ;; 

def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        # target is not in l[:left] or target is not in l[right+1:]
        current = (left + right) // 2
        if sorted_list[current] == target:
            return current
        elif sorted_list[current] < target:
            left = current + 1
        else:
            right = current - 1
    
    # right < left
    # target is not in l[:left]
    # target is not in l[right+1:]
    # so target is not in l
    return -1

"""
Problem: Count the number of index pairs (i, j) such that i < j and A[i] + A[j] ≤ K.

Input:
- A: list of n integers
- K: target sum

Output:
- One integer: number of valid pairs

Example:
Input:
[1, 3, 2, 5, 4]
6

Output:
6

This is because the valid pairs: (1,3), (1,2), (1,4), (1, 5), (3,2), (2,4)
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

# Matrix representation
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Matrix Multiplication

def get_row(matrix: List[List[int]] , i: int) -> List[int]:
    return matrix[i]

def get_column(matrix: List[List[int]] , i: int) -> List[int]:
    return [row[j] for row in matrix]

def dot_product(vec_a, vec_b):
    result = 0
    for i in range(len(vec_a)):
        result += vec_a[i] * vec_b[i]
    return result

def matrix_multiply(a, b):
    
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            row = get_row(a, i)
            col = get_column(b, j)
            result[i][j] = dot_product(row, col)

    return result

class Vector:
    def __init__(self, elements: List[int]):
        self.elements = elements
        self.dim = len(elements)
    
    def get(self, index: int) -> int:
        return self.elements[index]
    
    def dot(self, other: 'Vector') -> int:            
        result = 0
        for i in range(self.dim):
            result += self.elements[i] * other.elements[i]
        return result
    
class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = [Vector(row) for row in matrix]
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

    def get_row(self, i: int) -> List[int]:
        return self.matrix[i]

    def get_column(self, j: int) -> List[int]:
        return [row[j] for row in self.matrix]

    def multiply(self, other: 'Matrix') -> 'Matrix':
        result = [[0 for _ in range(other.num_cols)] for _ in range(self.num_rows)]
        
        for i in range(self.num_rows):
            for j in range(other.num_cols):
                row_vector = Vector(self.get_row(i))
                col_vector = Vector(other.get_column(j))
                result[i][j] = row_vector.dot(col_vector)

        return Matrix(result)