#splitting a list in two until getting singletons and then compare the way up.

''' 
def merge(seq, start, mid, stop):
    text= input ('Give a string of numbers')
    lst = [int(x) for x in text.split()]
    i=start
    j=mid

    #Merge the two lists

    while i < mid and j<stop:
        if seq[i]<seq[j]:
            lst.append(seq[i])
            i+=1

        else:
            lst.append(seq[j])
            j+=1

    #Copy in the rest of the start to mid sequence

    while i < mid:
        lst.append(seq[i])
        i+=1

    # Copy the elements back to the original sequence
    for i in range(len(lst)):
        seq[start+i]=lst[i]

def mergeSortRecursively(seq, start, stop):
    # We must use >= here only when the sequence we are sorting
    # is empty. Otherwise start == stop-1 in the base case.
    if start >= stop-1:
        return

    mid = (start + stop) // 2  

    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)

def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))

'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage
numbers = [64, 25, 12, 22, 11]
print(merge_sort(numbers))  # [11, 12, 22, 25, 64]