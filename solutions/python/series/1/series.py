def slices(series, length):
    result = []
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    for i in range(len(series)):
        if i+length <= len(series):
            result.append(series[i:i+length])
    return result