def ternary_search(l, r, key, arr):
	while r >= l:
		
		mid1 = l + (r-l) // 3
		mid2 = r - (r-l) // 3

		if key == arr[mid1]:
			return mid1
		if key == mid2:
			return mid2

		if key < arr[mid1]:
			r = mid1 - 1
		elif key > arr[mid2]:
			l = mid2 + 1
		else:
			l = mid1 + 1
			r = mid2 - 1
	return -1