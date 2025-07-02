def is_prime(n):
	if n <= 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			return False
	return True
prime = [x for x in range(1, int(input("Enter a num: "))) if is_prime(x)]

print(prime)