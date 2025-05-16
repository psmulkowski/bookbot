import os
from stats import get_word_counter, get_character_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    data_path = os.path.join(os.path.dirname(__file__), "books", "frankenstein.txt")
  #  print(data_path)
    book_content = get_book_text(data_path)
    word_counter = get_word_counter(book_content)
    character_counter = get_character_counter(book_content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{word_counter} words found in the document")
    print("--------- Character Count -------")
    print(character_counter)
    
    
main()