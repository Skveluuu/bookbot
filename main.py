import sys
from stats import word_count_string
from stats import character_count
from stats import dict_to_list

def get_book_text(file_path):
    print(f"Attempting to open file: {file_path}")
    with open(file_path) as file:
        file_content = file.read()
        return file_content


   

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_content = get_book_text(sys.argv[1])
    num_words = word_count_string(file_content)
    character_count_dict = character_count(file_content)
    character_count_list = dict_to_list(character_count_dict)
    sorted_list = character_count_list.sort(reverse=True, key=lambda x: x["num"])
                
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}..")
    file_content = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character_count_dict in character_count_list:
        char = character_count_dict["char"]
        if char.isalpha():
            count = character_count_dict["num"]
            print(f"{char}: {count}")
    print("============= END ===============")





    

main()
      
      