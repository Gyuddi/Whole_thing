def remove_all_before(items: list, border: int)
    for item in items:
        if item < border:
            del item
    return items

print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))