def recite(start, take=1):
    numbers = ["no","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
    crash = "And if one green bottle should accidentally fall,"
    final_verse = []
    for n_take in range(take):
        verse = f"green {'bottle' if start == 1 else 'bottles'} hanging on the wall"
        print(n_take)
        final_verse.append(f"{numbers[start]} {verse},")
        final_verse.append(f"{numbers[start]} {verse},")
        start -= 1
        verse = f"green {'bottle' if start == 1 else 'bottles'} hanging on the wall"
        final_verse.append(crash)
        final_verse.append(f"There'll be {numbers[start].lower()} {verse}.")
        final_verse.append("") if not n_take == take-1 else None
        
    return final_verse
