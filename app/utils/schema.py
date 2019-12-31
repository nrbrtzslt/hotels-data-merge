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
        elif target[key] == "" or target[key] is None:
            schema['properties'][key] = {"mergeStrategy": "discard"}
        elif isinstance(source[key], list) or isinstance(target[key], list):
            schema['properties'][key] = {"mergeStrategy": "append"}
        elif source[key] < target[key]:
            schema['properties'][key] = {"mergeStrategy": "overwrite"}
        else:
            schema['properties'][key] = {"mergeStrategy": "discard"}

    return schema
