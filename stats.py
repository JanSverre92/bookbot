def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def char_count(book_text):
    # Step 1: Initialize an empty dictionary to store characters and their counts
    char_dict = {}
    
    # Step 2: Loop through each character in the text string
    for char in book_text:
        # Step 3: Convert the character to lowercase
        char = char.lower()
        
        # Step 4: Check if the character is already in our dictionary
        if char in char_dict:
            # Step 5a: If it is, increment its count by 1
            char_dict[char] += 1
        else:
            # Step 5b: If it's not, add it to the dictionary with a count of 1
            char_dict[char] = 1
    
    # Step 6: Return the dictionary containing all characters and their counts
    return char_dict

def sort_chars_by_count(char_dict):
    # Create an empty list to store our dictionaries
    chars_list = []
    
    # Convert each character and count into a dictionary and add to the list
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list based on count, from greatest to least
    # The key parameter takes a function that tells sort() which value to use
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list