from webapi import get_filtered_hotels
import asyncio
import json


def test_webapi_happy_path():
    hotels_json = json.loads(asyncio.run(get_filtered_hotels()))
    assert len(hotels_json) != 0


def test_webapi_empty_list():
    hotels_json = json.loads(asyncio.run(get_filtered_hotels('asdf', 'asdf')))
    assert len(hotels_json) == 0
