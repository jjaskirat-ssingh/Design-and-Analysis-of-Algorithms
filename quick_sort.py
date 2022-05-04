# A typical recursive Python
# implementation of QuickSort

# Function takes last element as pivot,
# places the pivot element at its correct
# position in sorted array, and places all
# smaller (smaller than pivot) to left of
# pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
	i = (low - 1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller
		# than or equal to pivot
		if arr[j] <= pivot:
		
			# increment index of
			# smaller element
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi + 1, high)

# Driver Code
if __name__ == '__main__' :
	
	arr = [4, 2, 6, 9, 2]
	n = len(arr)
	
	# Calling quickSort function
	quickSort(arr, 0, n - 1)
	
	for i in range(n):
		print(arr[i], end = " ")


##########################################################


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
	i = ( l - 1 )
	x = arr[h]

	for j in range(l, h):
		if arr[j] <= x:

			# increment index of smaller element
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[h] = arr[h], arr[i + 1]
	return (i + 1)

# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quickSortIterative(arr, l, h):

	# Create an auxiliary stack
	size = h - l + 1
	stack = [0] * (size)

	# initialize top of stack
	top = -1

	# push initial values of l and h to stack
	top = top + 1
	stack[top] = l
	top = top + 1
	stack[top] = h

	# Keep popping from stack while is not empty
	while top >= 0:

		# Pop h and l
		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1

		# Set pivot element at its correct position in
		# sorted array
		p = partition( arr, l, h )

		# If there are elements on left side of pivot,
		# then push left side to stack
		if p-1 > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = p - 1

		# If there are elements on right side of pivot,
		# then push right side to stack
		if p + 1 < h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h

# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
	print ("% d" % arr[i]),

