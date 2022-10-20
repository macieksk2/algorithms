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
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements 
# if they are in the wrong order. 
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
        # print(out)
       
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

######################### Quick Sort #########################################

# DESCRIPTION
#Like Merge Sort, QuickSort is a Divide and Conquer algorithm. 
#It picks an element as a pivot and partitions the given array around the picked pivot. 
#There are many different versions of quickSort that pick pivot in different ways. 
#
#Always pick the first element as a pivot.
#Always pick the last element as a pivot (implemented below)
#Pick a random element as a pivot.
#Pick median as the pivot.
#The key process in quickSort is a partition(). 
#The target of partitions is, given an array and an element x of an array as the pivot,
#put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, 
#and put all greater elements (greater than x) after x. All this should be done in linear time.

# PYTHON IMPLEMENTATION
A = [64, 25, 12, 22, 11, 0, 54, 21, 45, 2, 143, 1, 4, 57, 1]

def partition(input_, low, high):
   out = input_
   # Choose the rightmost element as pivot
   pivot = out[high]
   # Pointer for greater elemenet
   i = low - 1
   # traverse though all elemenets
   # Compare each element with pivot
   for j in range(low, high):
       if out[j] <= pivot:
           # If element smaller than pivot is found
           # swap it with the greater element pointed by i
           i += 1
           # Swapping element at i with the element at j
           (out[i], out[j]) = (out[j], out[i])
   # swap the pivot element
   # e greater element specified by i 
   (out[i + 1], out[high]) = (out[high], out[i + 1])
   # Return the position from where partition is done
   return i + 1
   
def quick_sort(input_, low , high):
    out = input_
    if low < high:
        # find pivot element such that
        # elemenet smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(out, low, high)
        # Recursive call on the left of pivot
        quick_sort(out, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(out, pi + 1, high)
    return out
                    
print("Sorted array with selection sort: ")
print(quick_sort(A, 0, len(A) - 1))


# PSEUDO CODE

#/* low  –> Starting index,  high  –> Ending index */
#
#quickSort(arr[], low, high) {
#
#    if (low < high) {
#
#        /* pi is partitioning index, arr[pi] is now at right place */
#
#        pi = partition(arr, low, high);
#
#        quickSort(arr, low, pi – 1);  // Before pi
#
#        quickSort(arr, pi + 1, high); // After pi
#
#    }
#
#}

#Pseudo code for partition()  
#
#/* This function takes last element as pivot, places the pivot element at its correct position in sorted array, 
# and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot */
#
#partition (arr[], low, high)
#{
#    // pivot (Element to be placed at right position)
#    pivot = arr[high];  
#
#    i = (low – 1)  // Index of smaller element and indicates the 
#    // right position of pivot found so far
#
#    for (j = low; j <= high- 1; j++){
#
#        // If current element is smaller than the pivot
#        if (arr[j] < pivot){
#            i++;    // increment index of smaller element
#            swap arr[i] and arr[j]
#        }
#    }
#    swap arr[i + 1] and arr[high])
#    return (i + 1)
#}

# COMPLEXITY

#Time taken by QuickSort, in general, can be written as follows. 
#
# T(n) = T(k) + T(n-k-1) + \theta               (n)
#
#The first two terms are for two recursive calls, the last term is for the partition process. 
# k is the number of elements that are smaller than the pivot. 
#The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.
#
#Worst Case: 
#The worst case occurs when the partition process always picks the greatest or smallest element as the pivot. 
#If we consider the above partition strategy where the last element is always picked as a pivot, 
#the worst case would occur when the array is already sorted in increasing or decreasing order. 
#Following is recurrence for the worst case.  
#
# T(n) = T(0) + T(n-1) + \theta(n)
#which is equivalent to  T(n) = T(n-1) + \theta(n)
#
#The solution to the above recurrence is (n2). 
#

# STABILITY, IN-PLACE
#
#Is QuickSort stable? 
#The default implementation is not stable. 
#However any sorting algorithm can be made stable by considering indexes as comparison parameter. 
#
#Is QuickSort In-place? 
#As per the broad definition of in-place algorithm it qualifies as an in-place sorting algorithm 
#as it uses extra space only for storing recursive function calls but not for manipulating the input. 

##################### Heap Sort ###########################################################################

# DESCRIPTION

#Heap sort is a comparison-based sorting technique based on Binary Heap data structure. 
# It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. 
# Repeat the same process for the remaining elements.
#
#Heap sort is an in-place algorithm. 
#Its typical implementation is not stable, but can be made stable (See this)
#Typically 2-3 times slower than well-implemented QuickSort.  The reason for slowness is a lack of locality of reference.
#Advantages of heapsort:
#Efficiency –  The time required to perform Heap sort increases logarithmically 
#while other algorithms may grow exponentially slower as the number of items to sort increases. 
#This sorting algorithm is very efficient.
#Memory Usage – Memory usage is minimal because apart from what is necessary to hold the initial list of items to be sorted, 
#it needs no additional memory space to work
#Simplicity –  It is simpler to understand than other equally efficient sorting algorithms because 
#it does not use advanced computer science concepts such as recursion
#Applications of HeapSort:
#Heapsort is mainly used in hybrid algorithms like the IntroSort.
#Sort a nearly sorted (or K sorted) array 
#k largest(or smallest) elements in an array 
#The heap sort algorithm has limited uses because Quicksort and Mergesort are better in practice. 
#Nevertheless, the Heap data structure itself is enormously used. 

#What is meant by Heapify? 
#Heapify is the process of creating a heap data structure from a binary tree represented using an array. 
# It is used to create Min-Heap or Max-heap. Start from the first index of the non-leaf node whose index is given by n/2 – 1. 
# Heapify uses recursion

# PYTHON IMPLEMENTATION
A = [64, 25, 12, 22, 11, 0, 54, 21, 45, 2, 143, 1, 4, 57, 1]

def heapify(input_, N, i):
    # Initialize largest as root
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    # See if the left child of root exists and is
    # greater than root
    if l < N and input_[largest] < input_[l]:
        largest = l

    # See if the right child of root exists and is
    # greater than root
    if r < N and input_[largest] < input_[r]:
        largest = r
        
    # Change root, if needed
    if largest != i:
        input_[i], input_[largest] = input_[largest], input_[i]  # swap
 
        # Heapify the root.
        heapify(input_, N, largest)
 
# The main function to sort an array of given size
def heapSort(input_):
    out = input_
    N = len(out)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(out, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        out[i], out[0] = out[0], out[i]  # swap
        heapify(out, i, 0)   
    return out
print("Sorted array with selection sort: ")
print(heapSort(A))

# TIME COMPLEXITY

#Time Complexity: O(N log N)
#Auxiliary Space: O(1)

# STABILITY

#What are the two phases of Heap Sort?
#The heap sort algorithm consists of two phases. In the first phase the array is converted into a max heap. 
# And in the second phase the highest element is removed (i.e., the one at the tree root) and 
# the remaining elements are used to create a new max heap.
#
#Why Heap Sort is not stable?
#Heap sort algorithm is not a stable algorithm. This algorithm is not stable because the operations 
# that are performed in a heap can change the relative ordering of the equivalent keys.
#
#Is Heap Sort an example of “Divide and Conquer” algorithm?
#Heap sort is NOT at all a Divide and Conquer algorithm. It uses a heap data structure to efficiently sort its element 
#and not a “divide and conquer approach” to sort the elements.
#
#Which sorting algorithm is better – Heap sort or Merge Sort?
#The answer lies in the comparison of their time complexity and space requirement. 
#The Merge sort is slightly faster than the Heap sort. But on the other hand merge sort takes extra memory. Depending on the requirement, one should choose which one to use.
#
#Why Heap sort better than Selection sort?
#Heap sort is similar to selection sort, but with a better way to get the maximum element. 
# It takes advantage of the heap data structure to get the maximum element in constant time.

########################### Counting Sort #############################################

# DESCRIPTION


# PYTHON IMPLEMENTATION

### Counting Sort
import random
# Counting Sort
def counting_sort(A):
    # initiate
    B = [0] * (len(A) + 1)
    k = max(A) + 1
    C = []
    for i in range(k + 1):
        C.append(0)
    for j in range(len(A)):
        C[A[j]] += 1
    # C[i] now contains the number of elements equal to i
    for i in range(k + 1):
        C[i] += C[i - 1]
    # C[i] now contains the number of elements less than or equal to i
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
    # remove the first element (zero)
    return B[1:]#, C

A = [2,10,3,0,2,3,0,3]
out = counting_sort(A)

A = [2,10,3,0,2,3,0,3,76,23,52,1,0,0,5,4,7,8,3,6]
out = counting_sort(A)

A = random.sample(range(1, 1000), 100)
out = counting_sort(A)

# 8.2.3
# Counting Sort modified
def counting_sort_mod(A):
    # initiate
    B = [0] * (len(A) + 1)
    k = max(A) + 1
    C = []
    for i in range(k + 1):
        C.append(0)
    for j in range(len(A)):
        C[A[j]] += 1
    # C[i] now contains the number of elements equal to i
    for i in range(k + 1):
        C[i] += C[i - 1]
    # C[i] now contains the number of elements less than or equal to i
    # Modify
    for j in range(len(A)):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
    # remove the first element (zero)
    return B[1:]#, C

A = [2,10,3,0,2,3,0,3]
out = counting_sort_mod(A)

#A = random.sample(range(1, 1000), 100)
#out = counting_sort_mod(A)


####################### Radix Sort ########################################

# DESCRIPTION

# PYTHON IMPLEMENTATION

def counting_sort(arr, exp1):
 
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]        
# Method to do Radix Sort
def radix_sort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        counting_sort(arr, exp)
        exp *= 10
    return arr

####################### Bucket Sort ########################################

# DESCRIPTION

# PYTHON IMPLEMENTATION

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up: 
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up     
    return b     
              
# Bucket sort for numbers 
# having integer part
def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)
  
    # range(for buckets)
    rnge = (max_ele - min_ele) / noOfBuckets
    temp = []
  
    # create empty buckets
    for i in range(noOfBuckets):
        temp.append([])
  
    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)
  
        # append the boundary elements to the lower array
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
  
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
  
    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
  
    # Gather sorted elements 
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1
    return temp

# Driver Code
A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
print("Sorted Array is")
print(bucketSort(A))

# test efficiency
import random
import time
from matplotlib import pyplot as plt

def time_elapsed(func, inp_range = 10000, inp_no = 1000):
    random.seed(10)
    A = random.sample(range(1, inp_range), inp_no)
    start = time.time()
    print(str(func))
    if func == "quick_sort":
        test = eval(str(func) + "(A,0, len(A) - 1)")
    elif func == "bucket_sort":
        test = eval(str(func) + "(A,1)")
    else:
        test = eval(str(func) + "(A)")
    end = time.time()
    print(end - start)
    return end - start
    
test1 = time_elapsed("select_sort")
test2 = time_elapsed("bubble_sort")
test3 = time_elapsed("bubble_sort_optim")
test4 = time_elapsed("insertion_sort")
test5 = time_elapsed("merge_sort")
test6 = time_elapsed("quick_sort")
test7 = time_elapsed("heapSort")
test8 = time_elapsed("radix_sort")
test9 = time_elapsed("bucketSort")


# test efficiency for different lengths
test_len_1 = []
for n in range(999):
    print(n)
    test1 = time_elapsed("select_sort", inp_no = n + 1)
    test_len_1.append(test1)
    
plt.plot(test_len_1)
plt.show()

test_len_2 = []
for n in range(999):
    print(n)
    test2 = time_elapsed("bubble_sort", inp_no = n + 1)
    test_len_2.append(test2)
    
plt.plot(test_len_2)
plt.show()

test_len_3 = []
for n in range(999):
    print(n)
    test3 = time_elapsed("bubble_sort_optim", inp_no = n + 1)
    test_len_3.append(test3)
    
plt.plot(test_len_3)
plt.show()

test2_add = time_elapsed("bubble_sort", inp_range = 100000, inp_no = 50000)
test3_add = time_elapsed("bubble_sort_optim", inp_range = 100000, inp_no = 50000)


test_len_4 = []
for n in range(999):
    print(n)
    test4 = time_elapsed("insertion_sort", inp_no = n + 1)
    test_len_4.append(test4)
    
plt.plot(test_len_4)
plt.show()

test_len_5 = []
for n in range(9999):
    print(n)
    test5 = time_elapsed("merge_sort", inp_no = n + 1)
    test_len_5.append(test5)
    
plt.plot(test_len_5)
plt.show()

test_len_6 = []
for n in range(4999):
    print(n)
    test6 = time_elapsed("quick_sort", inp_no = n + 1)
    test_len_6.append(test6)
    
plt.plot(test_len_6)
plt.show()

plt.plot([x / test_len_6[2] for x in test_len_6])
plt.show()

plt.plot([x * np.log(x) for x in range(len(test_len_6))])
plt.show()

