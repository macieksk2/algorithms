##########################################
# SORTING ALGORITHMS
# EXAMPLES, O(N), o(n)
# PROS, CONS
# Python code, Pseudo code
##########################################
# https://www.freecodecamp.org/news/sorting-algorithms-explained/
import sys
############# Selection Sort #############
# DESCRIPTION

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
# from the unsorted part and putting it at the beginning. 
# Follow the below steps to solve the problem:
#
# 1. Initialize minimum value(min_idx) to location 0.
# 2. Traverse the array to find the minimum element in the array.
# 3. While traversing if any element smaller than min_idx is found then swap both the values.
# 4. Then, increment min_idx to point to the next element.
# 5. Repeat until the array is sorted.

# PYTHON IMPLEMENTATION
A = [64, 25, 12, 22, 11]

def select_sort(input_ = A):
    out = input_
    # Traverse through all elements
    # First loop
    for i in range(len(input_)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        # Second loop
        for j in range(i + 1, len(out)):
            if out[min_idx] > input_[j]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        out[i], input_[min_idx] = out[min_idx], input_[i]
    return out

print("Sorted array with selection sort: ")
print(select_sort())

# PSEUDO CODE

# For I = 0 to N-1 do:
#   Smallsub = I
#   For J = I + 1 to N-1 do:
#     If A(J) < A(Smallsub)
#       Smallsub = J
#     End-If
#   End-For
#   Temp = A(I)
#   A(I) = A(Smallsub)
#   A(Smallsub) = Temp
# End-For

# TIME COMPLEXITY

# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:
# 1. One loop to select an element of Array one by one = O(N)
# 2. Another loop to compare that element with every other Array element = O(N)
# Therefore, overall complexity = O(N) * O(N) = O(N*N) = O(N2)
# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. 
# The selection sort never makes more than O(N) swaps and can be useful when memory write is a costly operation. 

# STABILITY, IN PLACE

# Is Selection Sort Algorithm stable?
# Stability: The default implementation is not stable. However, it can be made stable. Please see stable selection sort for details.
#
# Is Selection Sort Algorithm in place?
# Yes, it does not require extra space.

############# Bubble Sort ###################
# DESCRIPTION
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 
# This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# Steps:
    
# 1. Run a nested for loop to traverse the input array using two variables i and j, such that 0 ≤ i < n-1 and 0 ≤ j < n-i-1
# 2. If arr[j] is greater than arr[j+1] then swap these adjacent elements, else move on

# PYTHON IMPLEMENTATION

A = [64, 25, 12, 22, 11]

def bubble_sort(input_ = A):
    n = len(input_)
    out = input_
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n - i - 1
            # Swap if the element found is greater
            # than the next element
            if out[j] > out[j + 1]:
                out[j], out[j + 1] = out[j + 1], out[j]
    return out

print("Sorted array with selection sort: ")
print(bubble_sort())

# PSEUDO CODE

# begin BubbleSortAlgorithm( Array )
#
# For all the elements of the array
#
#        if array[i] > array [i + 1]
#
#            switch ( array[i] , array[i+!])
#
#        end if
#
# end for
#
# return array
#
#end BubbleSortAlgorithm

# TIME COMPLEXITY
# Time Complexity: O(N2) (nested loop)
# Auxiliary Space: O(1) 
#
# Optimized Implementation of Bubble Sort: 
# The above function always runs O(N2) time even if the array is sorted. 
# It can be optimized by stopping the algorithm if the inner loop didn’t cause any swap

# Optimized version:
    
A = [64, 25, 12, 22, 11, 0, 54, 21, 45, 2, 143, 1, 4, 57, 1]

def bubble_sort_optim(input_ = A):
    n = len(input_)
    out = input_
    
    # Traverse through all array elements
    for i in range(n):
        swap = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n - i - 1
            # Swap if the element found is greater
            # than the next element
            if out[j] > out[j + 1]:
                out[j], out[j + 1] = out[j + 1], out[j]
                swap = True
        if swap == False:
            break
    return out

print("Sorted array with selection sort: ")
print(bubble_sort_optim())

# Worst Case Analysis for Bubble Sort:
# The worst-case condition for bubble sort occurs when elements of the array are arranged in decreasing order.
# In the worst case, the total number of iterations or passes required to sort a given array is (n-1). 
# where ‘n’ is a number of elements present in the array.
#
#  At pass 1 :  Number of comparisons = (n-1)
#                     Number of swaps = (n-1)
#
#  At pass 2 :  Number of comparisons = (n-2)
#                     Number of swaps = (n-2)
#
#  At pass 3 :  Number of comparisons = (n-3)
#                    Number of swaps = (n-3)
#                              .
#                             .
#                             .
#  At pass n-1 :  Number of comparisons = 1
#                        Number of swaps = 1
#
# Now, calculating total number of comparison required to sort the array
# = (n-1) + (n-2) +  (n-3) + . . . 2 + 1
# = (n-1)*(n-1+1)/2  { by using sum of N natural Number formula }
# = n (n-1)/2    
#
# For the Worst case:
# Total number of swaps = Total number of comparison
# Total number of comparison (Worst case) = n(n-1)/2
# Total number of swaps (Worst case) = n(n-1)/2
#
# Worst and Average Case Time Complexity: O(N2). The worst case occurs when an array is reverse sorted.
# Best Case Time Complexity: O(N). The best case occurs when an array is already sorted.
# Auxiliary Space: O(1)

# Recursive Implementation Of Bubble Sort:
# The idea is to place the largest element in its position and keep doing the same for every other element.
#
# Follow the below steps to solve the problem:
#
# Place the largest element at its position, this operation makes sure that the first largest element will be placed at the end of the array.
# Recursively call for rest n – 1 elements with the same operation and place the next greater element at their position.
# The base condition for this recursion call would be, when the number of elements in the array becomes 0 or 1 then, simply return (as they are already sorted).
# Below is the implementation of the above approach:
# TBD

# STABILITY, IN PLACE

# What is the Boundary Case for Bubble sort? 
# Bubble sort takes minimum time (Order of n) when elements are already sorted. 
# Hence it is best to check if the array is already sorted or not beforehand, to avoid O(N2) time complexity.
#
# Does sorting happen in place in Bubble sort?
# Yes, Bubble sort performs swapping of adjacent pairs without the use of any major data structure. 
# Hence Bubble sort algorithm is an in-place algorithm.
#
# Is the Bubble sort algorithm stable?
# Yes, the bubble sort algorithm is stable.
#
# Where is the Bubble sort algorithm used?
# Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm. 
# In computer graphics, it is popular for its capability to detect a tiny error 
# (like a swap of just two elements) in almost-sorted arrays and fix it with just linear 
# complexity (2n). 
#
# Example: It is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinate 
# at a specific scan line (a line parallel to the x-axis), and with incrementing y their order changes (two elements are swapped) 
# only at intersections of two lines (Source: Wikipedia)

############# Insertion Sort ###################

# DESCRIPTION
# Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
# The array is virtually split into a sorted and an unsorted part. 
# Values from the unsorted part are picked and placed at the correct position in the sorted part.
#
# Characteristics of Insertion Sort:
# 1. This algorithm is one of the simplest algorithm with simple implementation
# 2. Basically, Insertion sort is efficient for small data values
# 3. Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.

# Insertion Sort Algorithm 
# To sort an array of size N in ascending order: 
#
# 1. Iterate from arr[1] to arr[N] over the array. 
# 2. Compare the current element (key) to its predecessor. 
# 3. If the key element is smaller than its predecessor, compare it to the elements before. 
# 4. Move the greater elements one position up to make space for the swapped element.

# PYTHON IMPLEMENTATION
A = [64, 25, 12, 22, 11, 0, 54, 21, 45, 2, 143, 1, 4, 57, 1]

def insertion_sort(input_ = A):
    out = input_
    # Traverse through 1 to len(arr)
    for i in range(1, len(input_)):
        key = out[i]
        # Move elements of array[0:..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < out[j]:
            out[j + 1] = out[j]
            j -= 1
        out[j + 1] = key
       
    return out

print("Sorted array with selection sort: ")
print(insertion_sort())

# PSEUDO CODE
# https://www.ecb.torontomu.ca/~courses/coe428/sorting/insertionsort.html#:~:text=The%20pseudocode%20for%20insertion%20sort,by%20length%5BA%5D.)

# INSERTION-SORT (A)
#  for j <- 2 to length[A]
#2       do key <- A[j]
#3         Insert A[j] into the sorted sequence A[1 . . j - 1].
#4        i <- j - 1
#5        while i > 0 and A[i] > key
#6           do A[i + 1] <- A[i]
#7              i <- i - 1
#8        A[i + 1] <- key    
    
# TIME COMPLEXITY

# Time Complexity: O(N^2) (nested loop)
# Auxiliary Space: O(1)

# STABILITY, IN PLACE

# 1. What are the Boundary Cases of the Insertion Sort algorithm?
# Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
# And it takes minimum time (Order of n) when elements are already sorted. 
#
# 2. What are the Algorithmic Paradigm of Insertion Sort algorithm?
# Insertion Sort algorithm follows incremental approach.
#
# 3. Is Insertion Sort an in-place sorting algorithm?
# Yes, insertion sort is an in-place sorting algorithm.
#
# 4. Is Insertion Sort a stable algorithm?
# Yes, insertion sort is a stable sorting algorithm.
#
# 5. When is the Insertion Sort algorithm used?
# Insertion sort is used when number of elements is small. 
# It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
#
#6. What is Binary Insertion Sort? 
# We can use binary search to reduce the number of comparisons in normal insertion sort. 
# Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration. 
# In normal insertion, sorting takes O(i) (at ith iteration) in worst case. We can reduce it to O(logi) by using binary search. 
# The algorithm, as a whole, still has a running worst case running time of O(n^2) 
# because of the series of swaps required for each insertion. 
# Implementation of sort for Linked List
# https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/

# Create an empty sorted (or result) list
# Traverse the given list, do following for every node.
# Insert current node in sorted way in sorted or result list.
# Change head of given linked list to head of sorted (or result) list. 

############# Merge Sort #######################
# DESCRIPTION
# The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm. 
# In this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner.
#
# Merge Sort Working Process:
# Think of it as a recursive algorithm continuously splits the array in half until it cannot be further divided. 
# This means that if the array becomes empty or has only one element left, the dividing will stop, 
# i.e. it is the base case to stop the recursion. 
# If the array has multiple elements, split the array into halves and recursively invoke the merge sort on each of the halves. 
# Finally, when both halves are sorted, the merge operation is applied. 
# Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.

# PYTHON IMPLEMENTATION
A = [64, 25, 12, 22, 11, 0, 54, 21, 45, 2, 143, 1, 4, 57, 1]

def merge_sort(input_ = A):
    out = input_
    if len(out) > 1:
        # Find the mid of the array
        mid = len(out) // 2
        # Divide the array elements
        L = out[:mid]
        # into 2 halves
        R = out[mid:]
        # Sort the 1st half
        merge_sort(L)
        # Sort the 2nd half
        merge_sort(R)
        i = j = k = 0
        # Copy the data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                out[k] = L[i]
                i += 1
            else:
                out[k] = R[j]
                j += 1
            k += 1
        # Check if any element was left
        while i < len(L):
            out[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            out[k] = R[j]
            j += 1
            k += 1
    return out
            
print("Sorted array with selection sort: ")
print(merge_sort())

# PSEUDO CODE
#
#step 1: start
#
#step 2: declare array and left, right, mid variable
#
#step 3: perform merge function.
#    if left > right
#        return
#    mid= (left+right)/2
#    mergesort(array, left, mid)
#    mergesort(array, mid+1, right)
#    merge(array, left, mid, right)
#
#step 4: Stop

#Follow the steps below the solve the problem:
#
#MergeSort(arr[], l,  r)
#If r > l
#
#Find the middle point to divide the array into two halves: 
#middle m = l + (r – l)/2
#Call mergeSort for first half:   
#Call mergeSort(arr, l, m)
#Call mergeSort for second half:
#Call mergeSort(arr, m + 1, r)
#Merge the two halves sorted in steps 2 and 3:
#Call merge(arr, l, m, r)

# TIME COMPLEXITY

#Time Complexity: O(N log(N)),  
#Sorting arrays on different machines. 
#Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
#
#T(n) = 2T(n/2) + θ(n)
#
#The above recurrence can be solved either using the Recurrence Tree method or the Master method. 
#It falls in case II of the Master Method and the solution of the recurrence is θ(Nlog(N)). 
#The time complexity of Merge Sort isθ(Nlog(N)) in all 3 cases (worst, average, and best) 
#as merge sort always divides the array into two halves and takes linear time to merge two halves.
#
#Auxiliary Space: O(n), In merge sort all elements are copied into an auxiliary array. 
#So N auxiliary space is required for merge sort.

# STABILITY, IN-PLACE

#Is Merge sort In Place?
#No, In merge sort the merging step requires extra space to store the elements.
#
#Is Merge sort Stable?
#Yes, merge sort is stable. 
#
#How can we make Merge sort more efficient?
#Merge sort can be made more efficient by replacing recursive calls with Insertion sort for smaller array sizes, 
#where the size of the remaining array is less or equal to 43 as the number of operations required to sort an array 
#of max size 43 will be less in Insertion sort as compared to the number of operations required in Merge sort.
#
#Analysis of Merge Sort:
#A merge sort consists of several passes over the input. The first pass merges segments of size 1, 
#the second merges segments of size 2, and the i_{th}  pass merges segments of size 2i-1. 
#Thus, the total number of passes is [log2n]. 
#As merge showed, we can merge two sorted segments in linear time, which means that each pass takes O(n) time. 
#Since there are [log2n] passes, the total computing time is O(nlogn).

#Quick Sort

#Heap Sort

#Counting Sort

#Radix Sort

#Bucket Sort
