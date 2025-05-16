def get_word_counter(book_content):
    book_words = book_content.split()
    return len(book_words)
    
def get_character_counter(content):
    chars = {}
    for c in content:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
            
    return chars

def get_chars_sorted(char_dict):
    list_dictionaries = []
    dict_row = {}
    
    return