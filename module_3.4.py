def single_root_words(root_word,*other_words):
    same_words = []
    if isinstance(root_word, str) and isinstance(other_words,tuple):
        lower_case_word = root_word.lower()
        for word in other_words:
            if isinstance(word, str):
                tuple_word_lower_case = word.lower()
                if lower_case_word in tuple_word_lower_case or tuple_word_lower_case in lower_case_word:
                    same_words.append(word)
    return same_words



print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))