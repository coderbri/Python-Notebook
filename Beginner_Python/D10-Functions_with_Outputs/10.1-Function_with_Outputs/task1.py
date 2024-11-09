# TODO: Create a function called format_name() that takes two inputs: f_name and `l_name'.

def format_name(f_name, l_name):
    # TODO: Use the title() function to modify the f_name and l_name parameters into Title Case.
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("jAnE", "DOE"))   # Jane Doe
