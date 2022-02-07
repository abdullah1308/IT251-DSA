import random

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        
        j = i
        insert = arr[i]
        while j > 0 and arr[j - 1] > insert:
            arr[j] = arr[j - 1]
            j -= 1
        
        arr[j] = insert
        
# Merge Sort
def merge_sort(arr, start, end):
    if end - start < 2:
        return
    
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    if arr[mid - 1] < arr[mid]:
        return
    
    l = start
    r = mid
    
    merge_arr = []
    
    while l < mid and r < end:
        if arr[l] < arr[r]:
            merge_arr.append(arr[l])
            l+=1
        else:
            merge_arr.append(arr[r])
            r+=1
    
    if l < mid:
        merge_arr.extend(arr[l:mid])
    
    if r < end:
        merge_arr.extend(arr[r:end])
        
    arr[start : end] = merge_arr
    
# Quick Sort
def quick_sort(arr, start, end):
    if end - start < 2:
        return
    
    pivot_index = partition(arr, start, end)
    quick_sort(arr, start, pivot_index)
    quick_sort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    # randomly picking a pivot
    pivot_index = random.randint(start, end - 1)
    
    pivot_elem = arr[pivot_index]
    
    # swapping chosen pivot element with leftmost element in partition
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    
    left = start
    right = end - 1
    
    while left < right:
        while left < right and arr[right] >= pivot_elem:
            right-=1
        
        if left < right:
            arr[left] = arr[right]
        
        while left < right and arr[left] <= pivot_elem:
            left+=1
            
        if left < right:
            arr[right] = arr[left]
    
    arr[left] = pivot_elem
    return left
            
def main():
    arr = []
    
    n = int(input("Enter number of elements: "))
    
    print("Enter elements: ")
    for i in range(n):
        elem = int(input())
        arr.append(elem)
        
    arr_copy1 = arr[:]
    insertion_sort(arr_copy1)
    print("Array after sorting with insertion sort:", end=' ')
    print(arr_copy1)
    
    arr_copy2 = arr[:]
    merge_sort(arr_copy2, 0, len(arr))
    print("Array after sorting with merge sort:", end=' ')
    print(arr_copy2)
    
    arr_copy3 = arr[:]
    quick_sort(arr_copy3, 0, len(arr))
    print("Array after sorting with quick sort:", end=' ')
    print(arr_copy3)
    
if __name__ == '__main__':
    main()
        