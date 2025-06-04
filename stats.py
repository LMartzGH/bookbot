def get_num_words (filepath):
    with open(filepath) as f:
        filetext = f.read()
    wordcount = len(filetext.split())
    return wordcount

def get_char_counts(filepath):
    chars = {}
    with open(filepath) as f:
        filetext = f.read()
    for c in filetext:
        lowchr = c.lower()
        if lowchr in chars:
            chars[lowchr] += 1
        else:
            chars[lowchr] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_list(listing):
    char_list = []
    for char in listing:
        i = listing[char]
        if char.isalpha():
            char_list.append({"char": char, "num": i})
    char_list.sort(reverse=False, key=sort_on)
    return char_list
