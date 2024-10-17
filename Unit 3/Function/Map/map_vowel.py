word = ["a","b","c","d","e","i","o","z"]

def vowel(word):
    v_word = []
    if  word in  "aeiou":
        v_word.append(word)
    return v_word



mapped_object = map(vowel,word)
print(list(mapped_object))


