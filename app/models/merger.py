import json

from jsonmerge import Merger

from app.utils import schema
from app.utils.sanitizer import Sanitizer
from hotels import get_hotels_from_api


class HotelMerger:
    def __init__(self):
        self._hotels = get_hotels_from_api()
        self._result = dict()

    @staticmethod
    def merge_json(base, head, merger_schema):
        merger = Merger(merger_schema)
        return merger.merge(base, head)

    def recursive_merge(self, source, target, sub_schema, structure_key):
        structure_schema = schema.get_schema_with_strategies(source.copy(), target.copy(), sub_schema)

        if not structure_key:
            self._result = HotelMerger.merge_json(source, target, structure_schema)
        else:
            self._result[structure_key] = HotelMerger.merge_json(source, target, structure_schema)

        for key, value in source.items():
            if isinstance(value, dict):
                self.recursive_merge(source[key], target[key], schema.key_dictionary[key], key)

    def merge_sources(self, source1, source2):
        merged_hotels = []
        for hotel_a in source1:
            can_merge = False
            for hotel_b in source2:
                if hotel_a['id'] == hotel_b['id']:
                    self.recursive_merge(hotel_a.copy(), hotel_b.copy(), schema.key_dictionary['general'], '')
                    merged_hotels.append(self._result)
                    can_merge = True

            if not can_merge:
                merged_hotels.append(hotel_a)

        return merged_hotels

    @classmethod
    def sanitize_merged_hotels(cls, merged_hotels):
        for hotel in merged_hotels:
            # Deal with duplicated list items
            hotel['amenities']['general'] = Sanitizer.remove_duplicates(hotel['amenities']['general'])
            hotel['amenities']['room'] = Sanitizer.remove_duplicates(hotel['amenities']['room'])
            # Deal with duplicated urls
            set_of_json = {json.dumps(d) for d in hotel['images']['rooms']}
            hotel['images']['rooms'] = [json.loads(t) for t in set_of_json]

    def merge(self):
        merged_sources = self._hotels[0]

        for i in range(1, len(self._hotels)):
            merged_sources = self.merge_sources(merged_sources, self._hotels[i])

        HotelMerger.sanitize_merged_hotels(merged_sources)

        return merged_sources
