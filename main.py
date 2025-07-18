import sys
from stats import get_num_words, get_num_characters

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    text = get_book_text(book_location)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    num_characters = dict(sorted(num_characters.items(), key=lambda item: item[1]))

    #Report Printing
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in reversed(num_characters):
        if item.isalpha():
            print(f"{item}: {num_characters[item]}")
    print("============= END ===============")

main()
