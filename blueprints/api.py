from flask import Blueprint, request
from module import *

app = Blueprint('api','api', url_prefix="/api/v1")
with open('InstagramCreds.json', 'r') as f:
        data = json.load(f)

@app.route('/')
def index():
    return '1'

@app.route('/target')
def get_target():
    target = request.args.get('username')
    client = Client(**data)
    feed = grab_user_feed(target, client)
    location = map(grab_user_location, feed)
    m = folium.Map()
    list(map(lambda x: pin_user_location(x, m), location))
    if target:
        return {
            'feed':feed, 
            'location':list(location),
            'map':{
                    'html':m._repr_html_()
                }
            }
    else: 
        return 'Please Provide a Username'
