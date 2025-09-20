from stats import get_book_text, get_character_count, character_sort
import sys

def main():
    

    if len(sys.argv) != 2:
        msg = "Usage: python3 main.py <path_to_book>"
        sys.exit(msg)
    else:
        book_path = str(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        get_book_text ("./books/frankenstein.txt")
        print("--------- Character Count -------")
        character_sort(get_character_count (book_path))



main()
