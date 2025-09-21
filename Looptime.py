# Function 1: Recursive with n/2 and n/3 calls
def myfunction1(n):
    if n <= 0:
        return
    for i in range(0, n+1):   # O(n)
        print(i, end=" ")
    print()
    myfunction1(n//2)
    myfunction1(n//3)

# Recurrence: T(n) = T(n/2) + T(n/3) + O(n)
# Time Complexity: O(n)
# Space Complexity: O(log n)


# Function 2: Recursive with (n-1)
def myfunction2(n):
    if n <= 1:
        return
    print(n, end=" ")
    myfunction2(n-1)

# Recurrence: T(n) = T(n-1) + O(1)
# Time Complexity: O(n)
# Space Complexity: O(n)


# Function 3: Iterative loops
def myfunction(n):
    # First loop: O(n)
    for i in range(0, n+1):
        print(i, end=" ")
    print()

    # Second loop: O(log n)
    j = 1
    while j <= n+1:
        print(j, end=" ")
        j = j * 2
    print()

    # Third loop: O(1)
    for i in range(0, 100):
        print(i, end=" ")
    print()

# Time Complexity: O(n)
# Space Complexity: O(1)


# Main program
if __name__ == "__main__":
    print("Running myfunction1 with n=5")
    myfunction1(5)

    print("\nRunning myfunction2 with n=5")
    myfunction2(5)

    print("\n\nRunning myfunction (loops) with n=5")
    myfunction(5)
