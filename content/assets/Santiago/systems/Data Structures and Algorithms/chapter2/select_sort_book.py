'''def select(seq, start):
    minIndex=start 

    for j in range(start+1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex=j

    return minIndex

def selSort(seq):
    for i in range(len(seq)-1):
        minIndex=select(seq, i)
        tmp=seq[i]
        seq[i]=seq[minIndex]
        seq[minIndex]=tmp

    return seq

print('Give a sequence of numbers\n')

sortseq= selSort(input())

print(f'\nThe sorted list is:{sortseq}') '''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Example usage
text= input ('Give a string of numbers')
numbers = [int(x) for x in text.split()]
print(f'\nThe sorted list is  {selection_sort(numbers)}')  