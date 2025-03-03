def count_words(book_contents):
    word_list = book_contents.split()
    return len(word_list)

def count_characters(book_contents):
    to_lower_contents = book_contents.lower()

    all_characters_set = set()
    for c in to_lower_contents:
        all_characters_set.add(c)
    
    character_dict = {}
    for c in all_characters_set:
        character_count = 0
        for ch in to_lower_contents:
            if(ch == c):
                character_count += 1
        character_dict[c] = character_count

    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_character_dictionary(character_dict):
    dict_list = []
    for key in character_dict:
        new_dict = { "character": key,
                     "count": character_dict[key] }
        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list
