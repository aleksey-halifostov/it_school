values = [1, 2, '3', 'forth', 'end', 99, True, None]

new_values = list(map(lambda elem: str(elem) if isinstance(elem, int) and elem != True else elem, values))
print(new_values)
