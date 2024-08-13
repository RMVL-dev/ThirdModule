calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    if isinstance(string, str):
        return len(string), string.upper(), string.lower()
    else:
        return ()


def is_contains(string, list_to_search):
    count_calls()
    returned_value = False
    if isinstance(string, str) and isinstance(list_to_search, list):
        for word in list_to_search:
            if isinstance(word, str) and word.upper() == string.upper():
                return True
        return False
    else:
        return returned_value


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

