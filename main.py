from stats import count_words, count_characters, sort_character_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if(len(sys.argv) != 2):
        print("sage: python3 main.py <path_to_book>")
        return sys.exit(1)

    file_path = sys.argv[1]    
    frankenstein_contents = get_book_text(file_path)
    num_words = count_words(frankenstein_contents)
    character_dict = count_characters(frankenstein_contents)
    sorted_dict = sort_character_dictionary(character_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_dict:
        if(d["character"].isalpha()):
            print(f"{d["character"]}: {d["count"]}")
    print("============= END ===============")

main()

