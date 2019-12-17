import json

import requests


def get_hotel_dictionary():
    return {
        "id": "",
        "destination_id": "",
        "name": "",
        "location": {
            "lat": "",
            "lng": "",
            "address": "",
            "city": "",
            "country": ""
        },
        "description": "",
        "amenities": {
            "general": "",
            "room": ""
        },
        "images": {
            "rooms": "",
            "site": "",
            "amenities": ""
        },
        "booking_conditions": ""
    }


def transform_hotel_1(api_hotel):
    hotel_from_source_1 = []
    for hotel in api_hotel:
        hotel_dictionary = get_hotel_dictionary()
        hotel_dictionary['id'] = hotel['Id']
        hotel_dictionary['destination_id'] = hotel['DestinationId']
        hotel_dictionary['name'] = hotel['Name']
        hotel_dictionary['location']['lat'] = hotel['Latitude']
        hotel_dictionary['location']['lng'] = hotel['Longitude']
        hotel_dictionary['location']['address'] = hotel['Address']
        hotel_dictionary['location']['city'] = hotel['City']
        hotel_dictionary['location']['country'] = hotel['Country']
        hotel_dictionary['description'] = hotel['Description']
        hotel_dictionary['amenities']['general'] = hotel['Facilities']
        hotel_from_source_1.append(hotel_dictionary)

    return hotel_from_source_1


def transform_hotel_2(api_hotel):
    hotel_from_source_2 = []
    for hotel in api_hotel:
        hotel_dictionary = get_hotel_dictionary()
        hotel_dictionary['id'] = hotel['hotel_id']
        hotel_dictionary['destination_id'] = hotel['destination_id']
        hotel_dictionary['name'] = hotel['hotel_name']
        hotel_dictionary['location']['address'] = hotel['location']['address']
        hotel_dictionary['location']['country'] = hotel['location']['country']
        hotel_dictionary['description'] = hotel['details']
        hotel_dictionary['amenities']['general'] = hotel['amenities']['general']
        hotel_dictionary['amenities']['room'] = hotel['amenities']['room']
        hotel_dictionary['images']['rooms'] = hotel['images']['rooms']
        hotel_dictionary['images']['site'] = hotel['images']['site']
        hotel_dictionary['booking_conditions'] = hotel['booking_conditions']
        hotel_from_source_2.append(hotel_dictionary)

    return hotel_from_source_2


def transform_hotel_3(api_hotel):
    hotel_from_source_3 = []
    for hotel in api_hotel:
        hotel_dictionary = get_hotel_dictionary()
        hotel_dictionary['id'] = hotel['id']
        hotel_dictionary['destination_id'] = hotel['destination']
        hotel_dictionary['name'] = hotel['name']
        hotel_dictionary['location']['lat'] = hotel['lat']
        hotel_dictionary['location']['lng'] = hotel['lng']
        hotel_dictionary['location']['address'] = hotel['address']
        hotel_dictionary['description'] = hotel['info']
        hotel_dictionary['amenities']['room'] = hotel['amenities']
        hotel_dictionary['images']['rooms'] = hotel['images']['rooms']
        hotel_dictionary['images']['amenities'] = hotel['images']['amenities']
        hotel_from_source_3.append(hotel_dictionary)

    return hotel_from_source_3


hotel_from_a = transform_hotel_1(json.loads(requests.get("https://api.myjson.com/bins/gdmqa").text))
hotel_from_b = transform_hotel_2(json.loads(requests.get("https://api.myjson.com/bins/1fva3m").text))
hotel_from_c = transform_hotel_3(json.loads(requests.get("https://api.myjson.com/bins/j6kzm").text))

all_sources = []
all_sources.append(hotel_from_a)
all_sources.append(hotel_from_b)
all_sources.append(hotel_from_c)

