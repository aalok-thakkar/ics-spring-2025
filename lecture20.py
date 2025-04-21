# Lecture 20, April 8

from typing import List

def is_sorted (l: List[int]) -> bool:
    n = len(l)
    for i in range(n):
        # we are checking if l[i] <= l[i+1]. If so, do nothing. Otherwise:
        if i + 1 < n - 1:
            if l[i] > l[i+1]:
                return False
    return True


# let rec insert (x: int) (l: int list) : int list = 
#   match l with
#   | [] -> [x]
#   | h :: t -> 
#     match (x <= h) with
#     | true ->  x :: h :: t
#     | false -> h :: (insert x t)
# ;;

# let rec insertion_sort (l: int list) : int list = 
#   match l with
#   | [] -> []
#   | h :: t -> insert h (insertion_sort t)
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


def insertion_sort(l: List[int]) -> List[int]:
    sorted_list = []
    # sorted_list is always sorted
    for x in l:
        # sorted_list is always sorted

        # let us say sorted_list = [2, 2, 4, 6, 42433]
        # x = 43
        broken : bool = False
        for i in range(len(sorted_list)):
            # loop invariant: broken -> forall(y < x for y in sorted_list[0: i])
            # and also not broken!
            if x < sorted_list[i]:
                sorted_list = sorted_list[:i] + [x] + sorted_list[i:]
                broken = True
                break
        else:
            sorted_list.append(x)
    return sorted_list

# Creating a new list is expensive.


def insertion_sort(l: List[int]) -> None:

    # Say l = [3, 5, 6, 7, 4]
    #         [3, 4, 6, 7, _] temp = 5
    #         [3, 4, 5, 7, _] temp = 6
    #         [3, 4, 5, 6, _] temp = 7
    #         [3, 4, 5, 6, 7]


    # The first four elements are sorted. How do I insert l[4] in l[0:4]?

    # Find index 1 so that everything before is lesser, everything after is higher. 
    # return l[0:1] + [l[4]] + l[1:]

    n = len(l)

    # Loop invariant: At the start of each iteration i, the sublist l[0:i] is sorted.
    for i in range(n):
        key = l[i]

        # Find the insertion point j
        # what is the property of j? everything before is smaller... everything after is larger... 
        for j in range(i):
            if l[j] <= key:
                continue
            else:
                # Shift elements from j to i-1 one position to the right
                temp = key      # 4 gets up
                for k in range(j, i + 1):
                    l[k], temp = temp, l[k]
                break


def insertion_sort(l: List[int]) -> None:
    for i in range(len(l)):
        key = l[i]
        for j in range(i):
            if l[j] <= key:
                continue
            else:
                temp = key
                for k in range(j, i + 1):
                    l[k], temp = temp, l[k]
                break
       
# How much space does this take?    
                # One unit for key, one for temp. 
                # That is still O(1) space. 

# How much time does this take?   O(n^2)

# But this is ugly. 

def insertion_sort(l: List[int]) -> None:
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i - 1

        # Shift all elements l[0..j] that are greater than key one position to the right
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1

        # Insert key at the correct position
        l[j + 1] = key




# Quick Sort:

# let rec quick_sort (l: int list) : int list = 
#   match l with
#   | [] -> []
#   | h :: t -> quick_sort (filter (fun x -> x < h) l) @ quick_sort (filter (fun x -> x >= h) l)
# ;;

def quick_sort(l: List[int]) -> List[int]:
    if (l == []):
        return l
    else:
        pivot = l[0]
        n = len(l)
        left = []
        right = []
        for i in range(1, n):
            if l[i] < pivot:
                left.append(l[i])
            else:
                right.append(l[i])

        return quick_sort(left) + [pivot] + quick_sort(right)

# This version is correct, but why? 

# What is the complexity of quick sort? Worst Case vs. Average Case?

# This sorting algorithm is not very quick as it is not in-place.

# In place quick sort 

def quick_sort(l: List[int]) -> None:

  # [4, 8, 3, 6, 2, 1]
  # put pivot l[0] in the right list
  # pivot is 4
  # count elements smaller than 4. That is 3. 
  # Swap l[0] and l[3]
  # [6, 8, 3, 4, 2, 1]

  # Are elements left of 4 smaller? Are elements right of 4 larger or equal?
  # Swap 8 and 1.
  # [1, 8, 3, 4, 2, 6]
  # Swap 6 and 2.
  # [1, 2, 3, 4, 8, 6]

  # Quick sort on l[0:3] and quicksort on l[4:]

    def put_pivot_in_right_place(start: int, end: int) -> int:
        pivot = l[start]

        count = 0
        for i in range(start + 1, end + 1):
            if l[i] < pivot:
                count += 1

        pivot_index = start + count
        l[start], l[pivot_index] = l[pivot_index], l[start]
        return pivot_index

    def fix_around_pivot(start: int, end: int, pivot_index: int) -> None:
        pivot = l[pivot_index]
        i = start
        j = end


        # Say you had: [1, 3, 8, 4, 2, 6] with pivot index 3. l[3] = 4

        while i < pivot_index and j > pivot_index:
            if l[i] < pivot:
                i += 1
            elif l[j] >= pivot:
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

    def sort(start: int, end: int) -> None:
        if start >= end:
            return

        pivot_index = put_pivot_in_right_place(start, end)
        fix_around_pivot(start, end, pivot_index)
        sort(start, pivot_index - 1)
        sort(pivot_index + 1, end)

    sort(0, len(l) - 1)

# Now let us make it less ugly 

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

        # Place pivot in its correct position
        l[start], l[j] = l[j], l[start]
        return j

    # [4, 8, 3, 6, 2, 1]
    # pivot = l[0] = 4
    # i = 1
    # j = 5
    # [4, 8, 3, 6, 2, 1]
    # [4, 1, 3, 6, 2, 8]
    # [4, 1, 3, 2, 6, 8]

    # At the end --- swap pivot with last value of high
    # [2, 1, 3, 4, 6, 8]

    def sort(start: int, end: int) -> None:
        if start >= end:
            return
        pivot_index = partition(start, end)
        sort(start, pivot_index - 1)
        sort(pivot_index + 1, end)

    sort(0, len(l) - 1)

# What if last element was a pivot? What if a random element was a pivot? 

# Worst case complexity is still O(n^2). 

# What if there were k pivots?