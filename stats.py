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

def sort_on(dict):
    return dict["num"]

def get_chars_sorted(chars_dict):
    list_dictionaries = []
    
    for char in chars_dict:
        dict_row = {"char": char, "num": chars_dict[char]}
        list_dictionaries.append(dict_row)
    list_dictionaries.sort(reverse=True, key=sort_on)
    
    return list_dictionaries

