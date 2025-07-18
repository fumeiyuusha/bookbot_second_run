def get_num_words(text):
    wordlist = text.split()
    return len(wordlist)

def get_num_characters(text):
    txt = text.lower()
    results = dict()
    for character in txt:
        if character in results:
            results[character] = results[character]+1
        else:
            results[character] = 1
    return results
