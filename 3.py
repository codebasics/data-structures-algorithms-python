def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

# Sorts a (portion of an) array, divides it into partitions, then sorts those
def quicksort(A, lo, hi):
  if lo >= 0 and lo < hi:
    lt, gt = partition(A, lo, hi) # Multiple return values
    quicksort(A, lo, lt - 1)
    quicksort(A, gt + 1, hi)

# Divides array into three partitions
def partition(A, lo, hi):
  # Pivot value
  pivot = A[(lo + hi) // 2] # Choose the middle element as the pivot (integer division)
  
  # Lesser, equal and greater index
  lt = lo
  eq = lo
  gt = hi
  
  # Iterate and compare all elements with the pivot

  while eq <= gt:
    if A[eq] < pivot:
        # Swap the elements at the equal and lesser indices
        swap(eq, lt, A)
        # Increase lesser index
        lt += 1
        # Increase equal index
        eq += 1
    elif A[eq] > pivot:
        # Swap the elements at the equal and greater indices
        swap(eq, gt, A)
        # Decrease greater index
        gt -= 1
    else:  # A[eq] == pivot
        # Increase equal index
        eq += 1
  
  # Return lesser and greater indices
  return lt, gt

elements = [11,9,29,7,2,15,28]
# elements = ["mona", "dhaval", "aamir", "tina", "chang"]
quicksort(elements, 0, len(elements)-1)
print(elements)

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
]

try:
    # Your script's entry point, e.g., function calls
    for elements in tests:
        quicksort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
except Exception as e:
    print(f"Error occurred: {e}")