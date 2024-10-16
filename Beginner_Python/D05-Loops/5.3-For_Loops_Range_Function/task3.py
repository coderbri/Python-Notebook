# * Range Function
# for number in range(a, b):
#     print(number)

for number in range(1, 10): # 1 (inclusive) -> 10 (exclusive)
    print(number)
# 1 2 3 4 5 6 7 8 9

for number in range(1, 11): # 1 (inclusive) -> 10 (inclusive)
    print(number)
# 1 2 3 4 5 6 7 8 9 10

# ? Adding a Step
for number in range(1, 13, 3):
    print(number)
# 1 4 7 10

# * Gauss Challenge
total = 0
for number in range(1, 101):
    total += number

print(total)		# 5050
