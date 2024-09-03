import numbers

sum = 0

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def cycle(data):
    global sum
    if isinstance(data, numbers.Number):
        sum += data
    elif isinstance(data, str):
        sum += len(data)
    elif isinstance(data, dict):
        for value in data.values():
            cycle(value)
        for key in data.keys():
            cycle(key)
    else:
        for item in data:
            cycle(item)



cycle(data_structure)
print(sum)
