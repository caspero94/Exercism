def find_anagrams(word, candidates):
    new_list = []
    for c in candidates:
        if c.lower() == word.lower():
            candidates.remove(c)
    w_sorted = "".join(sorted(word.lower()))
    for candi in candidates:
        c_sorted = "".join(sorted(candi.lower()))
        if w_sorted == c_sorted:
            new_list.append(candi)
    return new_list
