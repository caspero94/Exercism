def flatten(e):
    if isinstance(e, list):
        r = []
        for item in e:
            if item is not None:
                r.extend(flatten(item))
        return r
    else:
        return [e]