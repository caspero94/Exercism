VERSES = [
    "house that Jack built.",
    "malt that lay in",
    "rat that ate",
    "cat that killed",
    "dog that worried",
    "cow with the crumpled horn that tossed",
    "maiden all forlorn that milked",
    "man all tattered and torn that kissed",
    "priest all shaven and shorn that married",
    "rooster that crowed in the morn that woke",
    "farmer sowing his corn that kept",
    "horse and the hound and the horn that belonged to"
]


def recite(start_verse:int, end_verse:int):
    """_summary_

    Args:
        start_verse (int): Number of start verse
        end_verse (int): Number of end verse

    Raises:
        ValueError: Check if is invalid verse numbers

    Returns:
        result (list): Verses of track
    """
    if not 1 <= start_verse <= end_verse <= 12:
        raise ValueError("Invalid verse numbers")

    result = []
    for i in range(start_verse-1, end_verse):
        verse = f"This is the {VERSES[i]}"
        verse += ''.join([f" the {VERSES[j-1]}" for j in range(i, 0, -1)])
        result.append(verse)

    return result
