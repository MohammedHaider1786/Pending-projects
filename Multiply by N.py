# Function 1: Multiply using 1 iteration (direct multiplication)
def multiply_one_iteration(N, M):
    return N * M   # O(1)


# Function 2: Multiply using N iterations (repeated addition)
def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):   # Loop runs N times
        result += M
    return result   # O(N)


# Main program
if __name__ == "__main__":
    N = int(input("Enter value of N: "))
    M = int(input("Enter value of M: "))

    print("\nUsing 1 iteration (direct multiplication):")
    print(f"{N} * {M} = {multiply_one_iteration(N, M)}")

    print("\nUsing N iterations (repeated addition):")
    print(f"{N} * {M} = {multiply_n_iterations(N, M)}")
