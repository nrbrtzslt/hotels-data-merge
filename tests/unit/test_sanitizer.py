import pytest
from app.utils.sanitizer import Sanitizer


class TestSanitizer:
    def test_camel_case_happy_path(self):
        input_word = 'ThisIsACamelCasedWord'
        exp_result = 'this is a camel cased word'
        output_word = Sanitizer.split_camel_case(input_word)
        assert output_word == exp_result

    @pytest.mark.parametrize('input_word', ['WiFi', 'BathTub'])
    def test_camel_case_exceptions(self, input_word):
        output_word = Sanitizer.split_camel_case(input_word)
        assert output_word == str(input_word).lower()

    @pytest.mark.parametrize('input_word', ['indoor pool', 'pool', 'Iron', ''])
    def test_camel_case_unchanged(self, input_word):
        output_word = Sanitizer.split_camel_case(input_word)
        assert output_word == str(input_word).lower()

    def test_camel_case_wrong_type(self):
        input_word = 12
        with pytest.raises(TypeError) as ex:
            Sanitizer.split_camel_case(input_word)
            assert 'The type of the input must be a string.' == str(ex)

    def test_remove_substrings_happy_path(self):
        input_list = ['bath tub', 'pool', 'hair iron', 'indoor pool', 'iron', 'tub']
        exp_list = ['hair iron', 'indoor pool', 'bath tub']
        assert sorted(Sanitizer.remove_substrings(input_list)) == sorted(exp_list)

    def test_remove_substrings_empty_list(self):
        input_list = []
        exp_list = []
        assert Sanitizer.remove_substrings(input_list) == exp_list

    def test_remove_duplicates_happy_path(self):
        input_list = ["Pool", "BusinessCenter", "WiFi ", "DryCleaning", " Breakfast", "outdoor pool", "indoor pool",
                      "business center", "childcare", "Aircon", "Tv", "Coffee machine", "Kettle", "Hair dryer", "Iron",
                      "Tub"]
        exp_list = ['business center', 'wifi', 'dry cleaning', 'breakfast', 'outdoor pool', 'indoor pool', 'childcare',
                    'aircon', 'tv', 'coffee machine', 'kettle', 'hair dryer', 'iron', 'tub']
        assert sorted(Sanitizer.remove_duplicates(input_list)) == sorted(exp_list)
