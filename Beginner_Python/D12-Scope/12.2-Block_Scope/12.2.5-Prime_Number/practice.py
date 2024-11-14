def is_prime(num):
    # Step 1: Exclude numbers less than or equal to 1
    if num == 1:
        return True
    if num == 2:
        return False

    # Step 2: Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
    
    return True

    # Step 3: If no divisors found, it's prime
    return True

print(is_prime(2))
print(is_prime(4))
print(is_prime(7))
print(is_prime(73))
print(is_prime(75))
