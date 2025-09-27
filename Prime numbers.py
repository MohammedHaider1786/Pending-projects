# Program to find all 2-digit prime numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to square root of n
        if n % i == 0:
            return False
    return True

# Collect and print all 2-digit prime numbers
prime_numbers = []
for num in range(10, 100):
    if is_prime(num):
        prime_numbers.append(num)

print("Two-digit prime numbers are:")
print(prime_numbers)
