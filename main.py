import os
from stats import word_counter
from stats import character_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    data_path = os.path.join(os.path.dirname(__file__), "books", "frankenstein.txt")
  #  print(data_path)
    book_content = get_book_text(data_path)
    word_counter(book_content)
    print(character_counter(book_content))
    
main()