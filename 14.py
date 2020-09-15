class Difference:
	def __init__(self, a):
		self.__elements = a
		self.maximumDifference = None


	def computeDifference(self):
		n = len(self.__elements)
		
		max = float("-inf")
		for i in range(n):
			for j in range(n):
				value = abs(self.__elements[i] - self.__elements[j])
				if value > max:
					max = value

		self.maximumDifference = max

if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, input().split()))

	d = Difference(arr)
	d.computeDifference()

	print(d.maximumDifference)