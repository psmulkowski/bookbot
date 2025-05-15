def word_counter(book_content):
    book_words = book_content.split()
    num_words = len(book_words)
    print(f"{num_words} words found in the document")
    
def character_counter(content):
    content_lower = content.lower()
    char = list(content_lower)
    char_unique = set()
    char_counter = {}
    
    for c in char:
        char_unique.add(c)
        
 #   print(len(char))
 #   print(len(char_unique))
    
    char_size = len(char)
    
    for c in sorted(char_unique):
        temp = 0
        i = 0
        while (i < char_size):
            if c == char[i]:
                temp += 1
            i += 1
        char_counter[c] = temp
           
    return char_counter