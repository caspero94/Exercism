def recite(start_verse, end_verse):
    verses = [
        "the house that Jack built.",
        "the malt that lay in",
        "the rat that ate",
        "the cat that killed",
        "the dog that worried",
        "the cow with the crumpled horn that tossed",
        "the maiden all forlorn that milked",
        "the man all tattered and torn that kissed",
        "the priest all shaven and shorn that married",
        "the rooster that crowed in the morn that woke",
        "the farmer sowing his corn that kept",
        "the horse and the hound and the horn that belonged to"
    ]
    
    if start_verse < 1 or end_verse > 12 or start_verse > end_verse:
        raise ValueError("Invalid verse numbers")
    
    result = []
    for i in range(start_verse, end_verse + 1):
        verse = "This is " + verses[i - 1] + " "
        for j in range(i - 1, 0, -1):
            verse += verses[j - 1] + " "
        result.append(verse.strip())
    
    return result