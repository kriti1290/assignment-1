import string

def remove_punctuation(input_string):
    """
    Remove all punctuation from the given string.
    
    Args:
    input_string (str): The string from which to remove punctuation.
    
    Returns:
    str: The string without any punctuation.
    """
    return input_string.translate(str.maketrans("", "", string.punctuation))

input_string = "Hello, world! This is a test string; with: various punctuations."
cleaned_string = remove_punctuation(input_string)

print("Original String: ", input_string)
print("String without punctuation: ", cleaned_string)
