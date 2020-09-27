def calculate_fine(expected, actual):
	if actual[2] < expected[2]:
		return 0
	elif actual[2] == expected[2]:
		if actual[1] < expected[1]:
			return 0
		elif actual[1] == expected[1]:
			if actual[0] <= expected[0]:
				return 0
			else:
				return 15 * (actual[0] - expected[0])
		else:
			return 500 * (actual[1] - expected[1])
	else:
		return 10000

if __name__ == "__main__":
	actual = list(map(int, input().split()))
	expected = list(map(int, input().split()))

	print(calculate_fine(expected, actual))