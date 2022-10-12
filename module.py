#!/usr/bin/env python3
from instagram_private_api import Client
from datetime import datetime
import argparse
import folium
import json

__author__ = "NotoriousArnav"
__author_GitHub_profile__ = "https://github.com/NotoriousArnav"

def grab_user_feed(username, client):
    data_frames = []
    dt = client.username_feed(username)
    data_frames.append(dt)
    last_dt = data_frames[-1]
    while last_dt['more_available']:
        dt = client.username_feed(username, max_id=last_dt['next_max_id'])
        data_frames.append(dt)
        last_dt = data_frames[-1]

    items = list(sum([x['items'] for x in data_frames],[]))
    return items

def grab_user_location(post):
    location = {}
    if 'location' in post.keys():
        location['time'] = {'timestamp':post['taken_at'], 'simple':datetime.fromtimestamp(post['taken_at']).__str__()}
        try:
            location['coordinates'] = post['location']['lat'], post['location']['lng']
            location['abbr'] = post['location']['address'],post['location']['short_name']
        except:
            pass
        location['caption'] = post['caption']['text'] if post['caption'] else "No caption"
    else:
        return None
    return location

def pin_user_location(location, folium_map):
    try:
        folium.Marker(location['coordinates'], popup=f"{'-'.join([x for x in location['abbr']])}<br>{location['caption']}<br>{location['time']['simple']}").add_to(folium_map)
    except:
        pass

