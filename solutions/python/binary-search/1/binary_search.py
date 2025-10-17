def find(search_list, value):
    izq = 0
    der = len(search_list) - 1
    while izq <= der:
        mid = (izq+der)//2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            izq = mid + 1
        else:
            der = mid - 1

    raise ValueError("value not in array")