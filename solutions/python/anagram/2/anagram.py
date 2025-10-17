def find_anagrams(word, pool):
    return [i for i in pool if sorted(i.lower()) == sorted(word.lower())
        and i.lower() != word.lower()]
