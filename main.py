def main ():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    word_count = count_words(book)
    letter_count = {}
    letter_count = count_letters(book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for key in letter_count:
        print(f"The '{key}' character was found {letter_count[key]} times")
    print("--- End report ---")


def get_book (book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(p):
    words = p.split()
    return len(words)

def count_letters(book):
    book_lower = book.lower()
    letter_dict = {}
    for char in book_lower:
        if char.isalpha():  # Consider only alphabetic characters
            if char not in letter_dict:
                letter_dict[char] = 0
            letter_dict[char] += 1
    return letter_dict
     




main()