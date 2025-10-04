A = int(input("Enter value of A (0 or 1): "))
B = int(input("Enter value of B (0 or 1): "))
C = int(input("Enter value of C (0 or 1): "))

Q = (A and B) or ((B or C) and (B and C))

print("Output Q =", int(Q))
