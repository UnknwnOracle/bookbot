def word_count(text):
    sep_text = text.split()
    word_count = len(sep_text)
    return word_count
def char_count(text):
    char_count = {}
    for i in text:
        i = i.lower()
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1
    return char_count

def char_sort(characters):
    char_value_list = []

    for char, v in characters.items():
        dict_item = {}
        dict_item["char"] = char
        dict_item["num"] = v
        if char.isalpha() == True:
            char_value_list.append(dict_item)
        else: 
            continue
    return char_value_list
