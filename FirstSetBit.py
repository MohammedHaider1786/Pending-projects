num = int(input("Enter a number: "))

if num == 0:
    print("No set bits (the number is 0).")
else:
    
    position = 1
    n = num

    while (n & 1) == 0:
        n = n >> 1  
        position += 1

    print(f"The rightmost set bit in {num} is at position {position}.")
