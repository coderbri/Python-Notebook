##############################################################
# Project:        Catching Exceptions
# Description:    Comprehensive guide to the try-except-else-finally 
#                 control flow. Demonstrates file I/O handling, 
#                 KeyError catching, and the execution order of 
#                 success vs. failure blocks.
##############################################################

"""
# The Try - Except - Else - Finally Block

try:
    # ATTEMPT: Code that might raise an exception (like opening a missing file)

except:
    # FALLBACK: Execute this block only if an exception occurred in the 'try' block

else:
    # SUCCESS: Execute this block only if the 'try' block ran without any errors

finally:
    # ALWAYS: Execute this block no matter what, whether an error occurred or not
"""

# Handling File and Dictionary errors
try:
    # This will raise FileNotFoundError if 'a_file.txt' doesn't exist
    file = open("a_file.txt", "r")
    a_dictionary = {"key": "value"}
    # This would raise a KeyError if the file opening didn't fail first
    print(a_dictionary["something"])

except FileNotFoundError:
    # If the file isn't there, we create it
    file = open("a_file.txt", "w")
    file.write("Created a new file because the original was missing.")
    print("File was not found, so a new one was created.")

except KeyError as error_message:
    # If the file exists but the key is wrong, we catch this specifically
    print(f"That key, {error_message}, does not exist.")

else:
    # This runs ONLY if the 'try' block was 100% successful
    content = file.read()
    print("File content read successfully:", content)

finally:
    # This runs at the very end, usually for cleanup (like closing files)
    # Note: Raising a manual error here will override any previous logic
    raise TypeError("This is my custom error message triggered at the end.")