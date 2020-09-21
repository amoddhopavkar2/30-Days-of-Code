n = int(input())
arr = list(map(int, input().split()))

swaps = 0
for i in range(n):
	for j in range(n-1):
		if arr[j] > arr[j+1]:
			temp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = temp

			swaps += 1
	
	if swaps == 0:
		break

print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(arr[0]))
print("Last Element: {}".format(arr[-1]))