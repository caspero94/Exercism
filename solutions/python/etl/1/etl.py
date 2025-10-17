def transform(legacy_data):
    res = {l.lower():k for k,v in legacy_data.items() for l in v}
    return res