import sys
from stats import word_count, char_count, char_sort


     
def main():

    if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    total_words = word_count(text)
    character_count = char_count(text)
    sorted = char_sort(character_count)
    sorted.sort(key=lambda char: char["num"], reverse=True)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {book_path}")
    print("----------- Word Count ----------")
    print(f" Found {total_words} total words")
    print("--------- Character Count -------")
    for sort in sorted:
            print(f"{sort['char']}: {sort['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    

main()
