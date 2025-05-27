from stats import get_num_words, get_num_chars
import sys

def get_book_text(filepath):
    with open(filepath) as fp:
        file_contents = fp.read()
        return file_contents

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    relpath = sys.argv[1]
    num_words = get_num_words(get_book_text(relpath))
    num_chars = get_num_chars(get_book_text(relpath))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in num_chars:
        if pair[0].isalpha():
            print(f"{pair[0]}: {pair[1]}")
    print("============= END ===============")


main()