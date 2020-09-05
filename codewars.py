def duplicate_encode(word):
    """
    Description: The goal of this exercise is to convert a string to a new string where each character in the
    new string is "(" if that character appears only once in the original string, or ")" if
    that character appears more than once in the original string. Ignore capitalization when determining if
    a character is a duplicate.
    """
    word = word.lower()
    result = ''
    duplicated_chars = []
    word_remain = word
    for ch in word_remain:
        word_remain = word_remain[1::]
        stop_flag = False
        if ch not in duplicated_chars and not stop_flag:
            for other_ch in word_remain:
                if ch == other_ch:
                    duplicated_chars += ch
                    stop_flag = True
    for ch in word:
        result += '(' if ch not in duplicated_chars else ')'
    return result


print(duplicate_encode("din"))  # (((
print(duplicate_encode("recede"))  # ()()()
print(duplicate_encode("Success"))  # )())())
print(duplicate_encode("(( @"))  # ))((
