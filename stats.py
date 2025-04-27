def word_count_string(file_content): 
    num_words = len(file_content.split())
    return num_words

def character_count(file_content):
    character_count_dict = {}
    lowercase_text = file_content.lower()
    for char in lowercase_text:
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1
    return character_count_dict

def dict_to_list(character_count_dict):
   list = [{"char": char, "num": count} for char,count in character_count_dict.items()]
   return list









    





