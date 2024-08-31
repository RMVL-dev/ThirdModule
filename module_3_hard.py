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
    if isinstance(data, numbers.Number):
        number_sum(data)
    elif isinstance(data, str):
        length_string_sum(data)
    elif isinstance(data, dict):
        calculating_dict(data)
    else:
        for item in data:
            cycle(item)


def calculating_dict(dictionary):
    if isinstance(dictionary, dict):
        for value in dictionary.values():
            cycle(value)
        for key in dictionary.keys():
            cycle(key)


def number_sum(number):
    global sum
    sum += number


def length_string_sum(string):
    global sum
    sum += len(string)


cycle(data_structure)
print(sum)
