import pytest
from app.utils.schema import get_schema_with_strategies


class TestSchema:
    @pytest.fixture
    def get_source_struct(self):
        return {
            "lat": 1.264751,
            "lng": 103.824006,
            "address": "An address that is short",
            "city": "SG",
            "country": "SG"
        }

    @pytest.fixture
    def get_custom_value(self, value):
        return {
            "lat": value
        }

    @pytest.fixture
    def get_target_struct(self):
        return {
            "lat": 1.264751,
            "lng": 103.824006,
            "address": "8 Sentosa Gateway, Beach Villas, 098269",
            "city": "Singapore",
            "country": "Singapore"
        }

    def create_struct(self, value):
        return {
            "lat": value
        }

    def create_result(self, value):
        return {
            'properties': {
                'lat': {
                    'mergeStrategy': value
                }
            }
        }

    @pytest.fixture
    def get_struct_keys(self):
        return ['lat', 'lng', 'address', 'city', 'country']

    @pytest.mark.parametrize('source_value,target_value,expected', [(123.23, 144.44, 'overwrite'),
                                                                    (144.44, 123.23, 'discard'),
                                                                    (None, 123.23, 'overwrite'),
                                                                    (144.44, None, 'discard'),
                                                                    ("", 144.44, 'overwrite'),
                                                                    (144.44, "", 'discard'),
                                                                    (144.44, [1, 2, 3], 'append'),
                                                                    ([1, 2, 3], 144.44, 'append')])
    def test_schema_happy_path_short(self, source_value, target_value, expected):
        source = self.create_struct(source_value)
        target = self.create_struct(target_value)
        struct_keys = ['lat']
        assert get_schema_with_strategies(source, target, struct_keys) == self.create_result(expected)

    def test_schema_happy_path(self, get_source_struct, get_target_struct, get_struct_keys):
        result_schema = {
            'properties': {
                'lat': {
                    'mergeStrategy': 'discard'
                },
                'lng': {
                    'mergeStrategy': 'discard'
                },
                'address': {
                    'mergeStrategy': 'discard'
                },
                'city': {
                    'mergeStrategy': 'overwrite'
                },
                'country': {
                    'mergeStrategy': 'overwrite'
                }
            }
        }
        assert get_schema_with_strategies(get_source_struct, get_target_struct, get_struct_keys) == result_schema
