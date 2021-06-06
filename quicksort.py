def partition(arr, low, high):
	pivot = arr[low]
	i, j = low + 1, high
	while i < j:
		while arr[i] <= pivot and i <= high:
			i += 1
		while arr[j] > pivot and j >= low:
			j -= 1
		if i < j:
			arr[i], arr[j] = arr[j], arr[i]
	arr[low], arr[j] = arr[j], arr[low]
	return j

def quicksort(arr, low, high):
	if high - low > 1:
		j = partition(arr, low, high)
		quicksort(arr, low, j)
		quicksort(arr, j + 1, high)