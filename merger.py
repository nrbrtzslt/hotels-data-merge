import hotels
import schema
import jsonmerge
from pprint import pprint

result = {}


def recursive_merge(source, target, sub_schema, structure_key):
    global result
    structure_schema = schema.get_schema_with_strategies(source.copy(), target.copy(), sub_schema)

    if not structure_key:
        result = merge_json(source, target, structure_schema)
    else:
        result[structure_key] = merge_json(source, target, structure_schema)

    for key, value in source.items():
        if isinstance(value, dict):
            recursive_merge(source[key], target[key], schema.key_dictionary[key], key)


def merge_json(base, head, merger_schema):
    merger = jsonmerge.Merger(merger_schema)
    return merger.merge(base, head)


def merge_sources(source1, source2):
    merged_hotels = []
    for hotel_a in source1:
        for hotel_b in source2:
            if hotel_a['id'] == hotel_b['id']:
                recursive_merge(hotel_a.copy(), hotel_b.copy(), schema.key_dictionary['general'], '')
                merged_hotels.append(result)

    return merged_hotels


merged_hotels = hotels.all_sources[0]
for i in range(1, len(hotels.all_sources)):
    merged_hotels = merge_sources(merged_hotels, hotels.all_sources[i])

for merged_hotel in merged_hotels:
    pprint(merged_hotel, width=150, sort_dicts=False)
