def get_book_text (filepath):
    with open(filepath) as f:
        filetext = f.read()
    return filetext

def get_num_words (filepath):
    filetext = get_book_text(filepath)
    wordcount = len(filetext.split())
    return wordcount

def main(filepath):
    wordcount = get_num_words(filepath)
    print(f"{wordcount} words found in the document")

main('books/frankenstein.txt')
