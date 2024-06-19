def are_anagrams(string1, string2):
    """
    Check if the two given strings are anagrams of each other.
    
    Args:
    string1 (str): The first string.
    string2 (str): The second string.
    
    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    return sorted(string1) == sorted(string2)

string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
