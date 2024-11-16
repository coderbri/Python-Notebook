from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# dice_num = 6 # ? This value is the cause of the IndexError
dice_num = randint(0, 5)
print(dice_images[dice_num])

# Bug to be Resolved:
# ! Traceback (most recent call last):
# !     print(dice_images[dice_num])
# !           ~~~~~~~~~~~^^^^^^^^^^
# ! IndexError: list index out of range
