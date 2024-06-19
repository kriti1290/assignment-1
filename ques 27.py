def string_to_list_of_characters(input_string):
    return list(input_string)

if __name__ == "__main__":
    input_string = input("Enter a string: ")

    characters_list = string_to_list_of_characters(input_string)

    print(f"The string '{input_string}' converted to a list of characters is:")
    print(characters_list)
