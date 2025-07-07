def wordNum(text):
    text_list = text.split()
    length = len(text_list)
    return length

def characterCount(text):
    new_text = text.lower()
    character_dict = {}
    for i in new_text:
        if i not in character_dict:
            character_dict[i] = 1
        else:
            character_dict[i] += 1
    return character_dict

def sortedCharacters(char_dict):
    new_dict_list = []
    for i in char_dict.keys():
        new_dict_list.append({"char":i,"num":char_dict[i]})
    new_dict_list.sort(reverse=True,key=sortByNum)
    return new_dict_list

def sortByNum(items):
    return items["num"]

