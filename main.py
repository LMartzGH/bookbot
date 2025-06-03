from stats import get_num_words
from stats import get_char_counts

def main(filepath):
    wordcount = get_num_words(filepath)
    print(f"{wordcount} words found in the document")
    charcounts = get_char_counts(filepath)
    print(charcounts)

main('books/frankenstein.txt')
