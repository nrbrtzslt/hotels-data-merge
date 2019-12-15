import hotels
import schema
import jsonmerge
from pprint import pprint

for hotel_a in hotels.hotel_from_a:
    for hotel_b in hotels.hotel_from_b:
        if hotel_a['id'] == hotel_b['id']:
            general_schema = schema.get_schema_with_strategies(hotel_a.copy(), hotel_b.copy(), schema.general_keys)
            location_schema = schema.get_schema_with_strategies(hotel_a['location'].copy(), hotel_b['location'].copy(),
                                                                schema.location_keys)
            merger = jsonmerge.Merger(general_schema)
            general_hotel = merger.merge(hotel_a.copy(), hotel_b.copy())
            merger = jsonmerge.Merger(location_schema)
            general_hotel['location'] = merger.merge(hotel_a['location'].copy(), hotel_b['location'].copy())
            pprint(general_hotel, width=150, sort_dicts=False)
