def main():

    book_path = './books/frankenstein.txt'
    frankenstein_text = get_book_text(book_path)
    frankenstein_words_count = word_count(frankenstein_text)
    frankenstein_char_count = count_characters(frankenstein_text)
    char_report = produce_char_report(frankenstein_char_count, frankenstein_words_count)
    print(char_report)

def get_book_text(path):
        with open(path) as f:
            return f.read()

def word_count(string):
        words = string.split()
        return(len(words))

def count_characters(string):
        char_hash = {}
        lowercase_string = string.lower()
        for char in lowercase_string:
            if(char in char_hash):
                char_hash[char] += 1
            else:
                char_hash[char] = 1
        return char_hash

def sort_on(dict):
    return dict["count"]

def sort_by_character_count(char_dict):
    char_map = []
    for char in char_dict:
        char_map.append({
            "char": char,
            "count": char_dict[char]
        })

    char_map.sort(reverse=True, key=sort_on)
    return char_map
    

def produce_char_report(character_dictionary, word_count):
    print(f"{word_count} words found in the document")

    sorted_dictionary = sort_by_character_count(character_dictionary)
    for char in character_dictionary:
        if char.isalpha():
            count = character_dictionary[char]
            print(f"The character '{char}' was found {count} times")
    print("--- End report ---")
main()