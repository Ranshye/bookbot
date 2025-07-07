from stats import wordNum, characterCount, sortedCharacters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if (len(sys.argv) <=1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    length = wordNum(text)
    #print(f"{length} words found in the document")
    character_dict = characterCount(text)
    #print(character_dict)
    sorted_dict = sortedCharacters(character_dict)
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {filepath}\n" \
    "----------- Word Count ----------\n" \
    f"Found {length} total words\n" \
    "--------- Character Count -------")
    for i in sorted_dict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()