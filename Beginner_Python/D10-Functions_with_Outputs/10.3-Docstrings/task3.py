def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

# It is generally more accepted
# by the Python guidelines to write
# multi-line comments like this

"""Whereas documentation for our functions or other
pieces of code is commonly written like this."""
