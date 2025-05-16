import os
from stats import get_word_counter, get_character_counter, get_chars_sorted, sort_on

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
    chars = get_chars_sorted(character_counter)
    print_report(data_path, word_counter, chars)
    
    
def print_report(data_path, word_counter, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {data_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")
    
    
main()