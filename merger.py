import hotels
import schema
import jsonmerge
import json

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


def sanitize_merged_hotels(hotels):
    for hotel in hotels:
        hotel['amenities']['general'] = schema.remove_duplicates(hotel['amenities']['general'])
        hotel['amenities']['room'] = schema.remove_duplicates(hotel['amenities']['room'])
        set_of_jsons = {json.dumps(d) for d in hotel['images']['rooms']}
        hotel['images']['rooms'] = [json.loads(t) for t in set_of_jsons]


def merge_json(base, head, merger_schema):
    merger = jsonmerge.Merger(merger_schema)
    return merger.merge(base, head)


def merge_sources(source1, source2):
    merged_hotels = []
    for hotel_a in source1:
        can_merge = False
        for hotel_b in source2:
            if hotel_a['id'] == hotel_b['id']:
                recursive_merge(hotel_a.copy(), hotel_b.copy(), schema.key_dictionary['general'], '')
                merged_hotels.append(result)
                can_merge = True

        if not can_merge:
            merged_hotels.append(hotel_a)

    return merged_hotels


merged_sources = hotels.all_sources[0]
for i in range(1, len(hotels.all_sources)):
    merged_sources = merge_sources(merged_sources, hotels.all_sources[i])
sanitize_merged_hotels(merged_sources)

# for merged_hotel in merged_sources:
#     pprint(merged_hotel, width=150, sort_dicts=False)
