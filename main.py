import os

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(book_content):
    book_words = book_content.split()
    num_words = len(book_words)
    print(f"{num_words} words found in the document")

def main():
    data_path = os.path.join(os.path.dirname(__file__), "books", "frankenstein.txt")
  #  print(data_path)
    book_content = get_book_text(data_path)
    word_counter(book_content)
    
main()