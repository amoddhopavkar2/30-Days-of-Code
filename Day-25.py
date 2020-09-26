def is_prime(n):
	if n == 1:
		return False

	sqrt_n = int(n ** 0.5)
	for i in range(2, sqrt_n + 1):
		if n % i == 0 and n != i:
			return False
	return True

t = int(input())
for _ in range(t):
	n = int(input())

	if is_prime(n):
		print("Prime")
	else:
		print("Not prime")