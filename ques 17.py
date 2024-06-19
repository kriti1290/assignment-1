def to_title_case(input_string):
    """
    Convert the given string to title case.
    
    Args:
    input_string (str): The string to convert.
    
    Returns:
    str: The title-cased string.
    """
    return input_string.title()

input_string = "this is a sample string to be converted to title case"
title_cased_string = to_title_case(input_string)

print("Original String: ", input_string)
print("Title Cased String: ", title_cased_string)
