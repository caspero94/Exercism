import re
from collections import Counter
def count_words(sentence):
    sentence = sentence.replace("_"," ")
    words = re.findall(r"\b(?:\w+(?:'\w+)?(?:_\w+)?|\w+)\b", sentence.lower())
    word_counts = Counter(words)
    return word_counts

