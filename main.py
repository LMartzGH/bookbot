from stats import get_num_words
from stats import get_char_counts
from stats import sort_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    wordcount = get_num_words(filepath)
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    charcounts = get_char_counts(filepath)
    charcounts = sort_list(charcounts)
    while len(charcounts) > 0:
        out = charcounts.pop()
        print(f"{out["char"]}: {out["num"]}")
    print("============= END ===============")
    return

main()
