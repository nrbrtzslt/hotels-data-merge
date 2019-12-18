from flask import Flask, request
import merger
import json

app = Flask("yolo")


@app.route('/data')
def hello_world():
    hotel_id = request.args.get('id')
    location_id = request.args.get('destination_id')
    if not hotel_id and not location_id:
        return json.dumps(merger.merged_sources)
    elif hotel_id:
        return json.dumps([x for x in merger.merged_sources if x['id'] == hotel_id])
    elif location_id:
        return json.dumps([x for x in merger.merged_sources if x['destination_id'] == int(location_id)])
    else:
        return json.dumps([x for x in merger.merged_sources if
                           x['id'] == hotel_id and x['destination_id'] == int(location_id)])
