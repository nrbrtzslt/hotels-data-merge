from quart import Quart, request
from hotels import get_hotels_from_api
from app.models.merger import HotelMerger
import json

app = Quart(__name__)

@app.route('/')
async def print_hotels():
    hotel_id = request.args.get('id')
    location_id = request.args.get('destination_id')

    return await get_filtered_hotels(hotel_id, location_id)


async def get_filtered_hotels(hotel_id=None, location_id=None):
    hotels = await get_hotels_from_api()
    hotel_merger = HotelMerger(hotels)

    if not hotel_id and not location_id:
        return json.dumps(hotel_merger.merge())
    elif hotel_id:
        return json.dumps([x for x in hotel_merger.merge() if x['id'] == hotel_id])
    elif location_id:
        return json.dumps([x for x in hotel_merger.merge() if x['destination_id'] == location_id])
    else:
        return json.dumps([x for x in hotel_merger.merge() if
                           x['id'] == hotel_id and x['destination_id'] == location_id])


if __name__ == '__main__':
    app.run()
