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
        location['coordinates'] = post['location']['lat'], post['location']['lng']
        location['abbr'] = post['location']['address'],post['location']['short_name']
        location['caption'] = post['caption']['text'] if post['caption'] else "No caption"
    else:
        return None
    return location

def pin_user_location(location, folium_map):
    folium.Marker(location['coordinates'], popup=f"{'-'.join([x for x in location['abbr']])}<br>{location['caption']}<br>{location['time']['simple']}").add_to(folium_map)

if __name__ == "__main__":
    m = folium.Map()
    parser = argparse.ArgumentParser(
            description = """
            This Program is to Designed to Scrape Instagram User's Map Timeline with a Proper Geotag, Timestamp, and Media (or Media Abbriviation)
            """
        )
    parser.add_argument(
            "--credentialFile",
            help="""
            The Program Uses this JSON file to Login to Instagram and Fetch Data. 
            Use JSON files with structure:
            {
                "username":"foo",
                "password":"foobar'sSecretPassword123$"
            }
            """,
            type=argparse.FileType('r')
        )
    parser.add_argument(
            "--username",
            help="""
            Username of the the Target.
            """
        )
    parser.add_argument(
            "--outname",
            help="""
            Dump file(s) for Target Info.
            [
            (filename.html -- Map Timeline)
            (filename.json -- Address and Coordinate Dump based on timestamp.)
            ]
            Default Filename is the username provided
            """
        )
    args = parser.parse_args()
    if (args.credentialFile is None) and (args.username is None):
        print("Required Information not Provided")
    creds = json.load(args.credentialFile)
    client = Client(**creds)
    print(f"Logged in as {creds['username']}")
    print(f"Target is {args.username}")
    dt = grab_user_feed(args.username, client)
    print("Grabbing Posts")
    filenameJSON = f"{args.outname}.json" if args.outname else f"{args.username}.json"
    filenameHTML = f"{args.outname}-Map_LocationTimeline.html" if args.outname else f"{args.username}-Map.html"
    print("Grabbing Location Timeline")
    location_timeline = [x for x in list(map(grab_user_location, dt)) if x]
    json.dump(
                location_timeline, 
                open(filenameJSON, 'w')
            )
    print(f"Dumping {filenameJSON}")
    for x in location_timeline:
        pin_user_location(x, m)
    m.save(filenameHTML)
    print(f"Dumping {filenameHTML}")
