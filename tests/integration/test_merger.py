from app.models.merger import get_dict_for_web_api
import hotels
import json


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def test_merge_hotels(monkeypatch):
    def mock_hotel_sources():
        with open('C:\\Users\\i334330\\IdeaProjects\\hotels-data-merge\\tests\\integration\\mock_data_source_1') as mock_data:
            return json.loads(mock_data.read())

    monkeypatch.setattr(hotels, 'get_hotels_from_api', mock_hotel_sources)

    result = get_dict_for_web_api()

    with open('C:\\Users\\i334330\\IdeaProjects\\hotels-data-merge\\tests\\integration\\exp_result') as expected_result:
        exp_result = json.loads(expected_result.read())

    assert ordered(result) == ordered(exp_result)
