# * Testing *args
def args_test(*args):
    # 'args' will be a tuple containing all positional arguments passed to the function.
    print(args)
    # This will confirm that 'args' is indeed a tuple.
    print(type(args))

args_test(6, 12, 18)
# Output: (6, 12, 18)  (A tuple containing the passed arguments)
# Output: <class 'tuple'>

def args_loop(*args):
    # Iterate through each item in the 'args' tuple.
    for n in args:
        print(n)

    # Access an element from the 'args' tuple using its index.
    print(args[1])

args_loop(1, 2, 3)        # Prints: 1, 2, 3 (each on a new line), then prints: 2
args_loop(2, 4, 6, 8)     # Prints: 2, 4, 6, 8 (each on a new line), then prints: 4


# * Using *args for summation
def add(*args):
    sum = 0
    # Loop through each number in the 'args' tuple and add it to the sum.
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3))        # Output: 6
print(add(2, 4, 6, 8))     # Output: 20
