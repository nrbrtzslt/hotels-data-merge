from flask import Flask, request
from app.models.merger import HotelMerger
import json

app = Flask("hotels-data-merge")


@app.route('/data')
def hello_world():
    hotel_id = request.args.get('id')
    location_id = request.args.get('destination_id')
    hotel_merger = HotelMerger()

    if not hotel_id and not location_id:
        return json.dumps(hotel_merger.merge())
    elif hotel_id:
        return json.dumps([x for x in hotel_merger.merge() if x['id'] == hotel_id])
    elif location_id:
        return json.dumps([x for x in hotel_merger.merge() if x['destination_id'] == int(location_id)])
    else:
        return json.dumps([x for x in hotel_merger.merge() if
                           x['id'] == hotel_id and x['destination_id'] == int(location_id)])
