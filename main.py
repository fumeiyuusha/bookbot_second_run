def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def count_words(text):
    wordlist = text.split()
    return len(wordlist)

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

main()
