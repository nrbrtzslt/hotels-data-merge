import re

key_dictionary = {
    'location': ['lat', 'lng', 'address', 'city', 'country'],
    'images': ['rooms', 'site', 'amenities'],
    'amenities': ['room', 'general'],
    'general': ['name', 'description', 'booking_conditions']
}


def get_schema_with_strategies(source, target, json_keys):
    schema = {'properties': {}}
    for key in json_keys:
        if source[key] == "" or source[key] is None:
            schema['properties'][key] = {"mergeStrategy": "overwrite"}
            continue

        if target[key] == "" or target[key] is None:
            schema['properties'][key] = {"mergeStrategy": "discard"}
            continue

        if isinstance(source[key], list):
            schema['properties'][key] = {"mergeStrategy": "append"}
            continue

        if source[key] < target[key]:
            schema['properties'][key] = {"mergeStrategy": "overwrite"}
        else:
            schema['properties'][key] = {"mergeStrategy": "discard"}

    return schema


def remove_duplicates(input):
    result = []
    for word in input:
        word = word.lstrip().rstrip()
        word = put_space(word)
        result.append(word)

    result = list(set(result))
    result = remove_substrings(result)

    return result


def put_space(input):
    words = re.findall('[A-Z][a-z]*', input)
    result = []
    if ''.join(words) != input or input == "WiFi":
        result.append(input.lower())
    else:
        for word in words:
            word = word.lower()
            result.append(word)

    return ' '.join(result)


def remove_substrings(input):
    result = input.copy()
    for m in input:
        for n in input:
            if m != n and m in n and m in result:
                result.remove(m)

    return result


removed = remove_duplicates(['tv',
                             'coffee machine',
                             'kettle',
                             'hair dryer',
                             'iron',
                             'Aircon',
                             'Tv',
                             'Coffee machine',
                             'Kettle',
                             'Hair dryer',
                             'Iron',
                             'Tub'])
print(removed)
