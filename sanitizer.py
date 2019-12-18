import re


def remove_duplicates(duplicated_list):
    result = []
    # Transform and split camel case words
    for word in duplicated_list:
        word = word.lstrip().rstrip()
        word = split_camel_case(word)
        result.append(word)

    result = list(set(result))
    result = remove_substrings(result)

    return result


def split_camel_case(camel_cased_word):
    words = re.findall('[A-Z][a-z]*', camel_cased_word)
    result = []
    if ''.join(words) != camel_cased_word or camel_cased_word == "WiFi" or camel_cased_word == "BathTub":
        result.append(camel_cased_word.lower())
    else:
        for word in words:
            word = word.lower()
            result.append(word)

    return ' '.join(result)


def remove_substrings(string_list):
    result = string_list.copy()
    for m in string_list:
        for n in string_list:
            if m != n and m in n and m in result:
                result.remove(m)

    return result
