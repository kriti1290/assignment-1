def is_substring_present(main_string, substring):
    """
    Check if the substring is present in the main string.
    
    Args:
    main_string (str): The string to search within.
    substring (str): The string to search for.
    
    Returns:
    bool: True if the substring is present, False otherwise.
    """
    return substring in main_string

# Example usage:
main_string = "Hello, world!"
substring = "world"

if is_substring_present(main_string, substring):
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")
