general_keys = ['name', 'description', 'booking_conditions']
location_keys = ['lat', 'lng', 'address', 'city', 'country']
image_keys = ['rooms', 'site', 'amenities']
amenity_keys = ['room', 'site']


def get_schema_with_strategies(source, target, json_keys):
    schema = {'properties': {}}
    for key in json_keys:
        if source[key] == "":
            schema['properties'][key] = {"mergeStrategy": "overwrite"}
            continue

        if target[key] == "":
            schema['properties'][key] = {"mergeStrategy": "discard"}
            continue

        if source[key] < target[key]:
            schema['properties'][key] = {"mergeStrategy": "overwrite"}
        else:
            schema['properties'][key] = {"mergeStrategy": "discard"}

    return schema
