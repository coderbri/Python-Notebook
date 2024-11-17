import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)  # Fixed: Appending inside the loop ensures each item is added.
    # b_list.append(new_item)  # ! Bug: Only the last item was appended since this was outside the loop.
    print(b_list)  # Correctly prints all transformed values.

# ? Issue: Original code appended only the final transformed value.
# * Fix: Move `b_list.append(new_item)` inside the `for` loop to add each transformed item.

mutate([1, 2, 3, 5, 8, 13])
# Output: [4, 9, 12, 18, 25, 42]
