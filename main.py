import sys
from stats import count_words, char_count, sort_chars_by_count

# Check if we have the right number of arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# If we get here, we have the right number of arguments
book_path = sys.argv[1]
# Now you can use book_path instead of a hard-coded path

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def main():
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_dict = char_count(book_text)
    sorted_chars = sort_chars_by_count(char_dict)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character count (only for alphabetic characters)
    for char_item in sorted_chars:
        char = char_item["char"]
        count = char_item["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()