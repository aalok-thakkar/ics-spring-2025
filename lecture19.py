# Lecture 19, April 4

from typing import List

def is_sorted (l: List[int]) -> bool:
    n = len(l)
    for i in range(n):
        # should add a loop invariant to prove this part as well.
        # we are checking if l[i] >= l[i+1]. If so, do nothing. Otherwise:
        if i + 1 < n - 1:
            if l[i] < l[i+1]:
                return False
    return True

test_list : List[str] = ["a", "b", "c", "d", "e"]
# iterate [0, 1, 2, 3]

# what about []
# is range(-1) even defined?

def selection_sort(l: List[int]) -> List[int]:
    n : int = len(l)
    
    for i in range(n):
        # First i elements are sorted
        assert (is_sorted(l[0:i]))
        assert all(l[k] <= l[k + 1] for k in range(i))
        
        min_index = i
        for j in range(i + 1, n):
            assert all(l[k] >= l[min_index] for k in range(i, j))  
            # All elements in l[i...j-1] are >= l[min_index]
            if l[j] < l[min_index]:
                min_index = j
        
        assert l[min_index] <= l[i]  # min_index element is <= current element
        
        l[i], l[min_index] = l[min_index], l[i]
        
        assert (is_sorted(l[0:i+1]))
        assert all(l[k] <= l[k + 1] for k in range(i + 1))
    
    return l


# [12, 10, 5, 4, 3]

# [10, 5, 4, 3, 12] # after 4 swaps

# [5, 10, 4, 3, 12]
# [5, 4, 10, 3, 12]
# [5, 4, 3, 10, 12]
# [5, 4, 3, 10, 12]  # no change required

# [4, 5, 3, 10, 12]
# [4, 3, 5, 10, 12]
# [4, 3, 5, 10, 12] # no change required
# [4, 3, 5, 10, 12] # no change required

# [3, 4, 5, 10, 12] 
# [3, 4, 5, 10, 12] # no change required
# [3, 4, 5, 10, 12] # no change required
# [3, 4, 5, 10, 12] # no change required

def bubble_sort(l: List[int]) -> List[int]:
    n = len(l)
    for i in range(n):
        assert(isinstance(l[i], int))
        # last i elements are sorted
        # l[a:b] = [l[a], l[a+1], ... l[b-1]]
        assert(is_sorted(l[n - i:n]))
        assert(i <= n)
        # should it be empty?
        for j in range(0, (n - 1) - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    # the above loop is effectively while (i < n)...
    # Hence, after the loop, we can assume i >= n.
    # Conclude i = n.
    assert(is_sorted(l[0:n]))
    return l


from typing import List

def bubble_sort(l: List[int]) -> List[int]:
    assert all(isinstance(x, int) for x in l)
    
    n = len(l)
    for i in range(n):

        # After each iteration, l[j] <= l[j+1] for the traversed section
        for j in range(0, n - i - 1):

            
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]  # Swap elements if they are out of order

            # The max of l[0] to l[j+1] is at l[j+1]
            assert max(l[:j+1]) == l[j+1]
        
        # everything before (n - i - 1)th position is smaller
        assert l[n - (i + 1)] == max(l[:n - i])
        # Assert that the last i elements are sorted
        assert all(l[k] <= l[k+1] for k in range(n - i - 1, n - 1))
    
    # Postcondition: The entire list must be sorted
    assert all(l[k] <= l[k+1] for k in range(n - 1))
    
    return l


# Which is better? Selection Sort or Bubble Sort?


# Running Time?
# We can evaluate it on several inputs and test. 
# What about very large inputs?



# Time Complexity measures how the number of 'basic' operations an algorithm takes grows with input size 'n'. The notation we use is the Big-O notation (O(f(n))) to describe the worst-case upper bound of an algorithm.
# If an algorithm runs in '3n^2 + 5n + 7' units of time, we simplify it to 'O(n^2)'
# This predicts performance for large datasets. Helps compare different algorithms beyond small input sizes.

# There are also other parameters such as stability, adaptability, and swap efficiency. We will push it to another day. 


# Selection Sort:

# First pass: Compare 'n' elements
# Second pass: Compare 'n-1' elements
# Third pass: Compare 'n-2' elements ...
# In general:

# N passes on the list. For the ith pass, it compares (n- i - 1) elements
# Let T(n) denote the number of basic operation till the nth pass (including previous passes)
# T(n) = T(n-1) + (n - 1)
# T(2) = 1
# T(3) = T(2) + 2 = 3
# T(4) = 3 + 3 = 6
# T(5) = 6 + 4 = 10


# T(n) = sum of (2 - 1) + (3 - 1) + (4 - 1) + .. .(n - 1) = sum of 1 + 2 + 3 ... (n - 1)
#                                                         = n*(n-1)/2
#   We say that T(n) is quadratic. O(n^2). 

# O(n^2) captures the notion that, in AT MOST some quadratic time, we can run selection sort. 

# T(n)= c*n + T(n−1)


# What about Bubble Sort? 

# First pass: Compares n-1 elements.
# Second pass: Compares n-2 elements. ..


# T(n) = (n-1) + T(n−1)
# So we get O(n^2)


# So both of them seem equal. 

# What if we change bubble sort to: 

from typing import List

def bubble_sort_opt(l: List[int]) -> List[int]:
    assert all(isinstance(x, int) for x in l)

    n = len(l)
    for i in range(n):
        swapped = False  # Track if swaps occur
        for j in range(0, n - i - 1):
            assert max(l[:j+1]) == l[j+1]
            
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True  # Swap occurred

        assert all(l[k] <= l[k+1] for k in range(n - i - 1, n - 1))
        assert l[n - i - 1] == max(l[:n - i])

        # If no swaps happened, the list is already sorted
        if not swapped:
            break
    
    assert all(l[k] <= l[k+1] for k in range(n - 1))
    return l

# What about the best case in this, vs original bubble sort?

# Can we do a faster algorithm?

# Can we do recursion? 
# OCAML TIME!


# let rec insert (x: int) (l: int list) : int list = 
#   match l with
#   | [] -> [x]
#   | h :: t -> 
#     match (x < h) with
#     | true ->  x :: h :: t
#     | false -> h :: (insert x t)
# ;;

# let rec insertion_sort (l: int list) : int list = 
#   match l with
#   | [] -> []
#   | h :: t -> insert h (insertion_sort t )
# ;;

def insert (x: int, l: List[int]) -> List[int]:
    if (l == []):
        return [x]
    else: 
        n = len(l)
        for i in range(n):
            if (x < l[i]):
                return (l[0:i] + [x] + l[i:n])
        else:
            return l + [x]
        
def insertion_sort(l: List[int]) -> List[int]:
    n = len(l)
    for i in range(n):
        insert(l[i], l[i+1:n])
    return l

# Write this as a single function and identify the loop invariants, and prove correctness.
