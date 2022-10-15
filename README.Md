# Instagram Geo Timeline
A Simple Script to Parse location data of a Public Instagram Account to a Map and JSON document for Further analysis.

# API and Dashboard Usage
Just run main.py using default Python Install or using gunicorn, and then your dashboard should startup at 0.0.0.0:8000 or 0.0.0.0:5000.

# Dashboard Usage
The Dashboard is made using Alpine and Tailwind CSS.
The UI is self Explanatory, so no need to Elaborate that, but if you want more Info then click on API Call to get a JSON Output, that has every Info.

# API Usage
## Endpoint : /api/v1/target
This Endpoint takes a param username, and returns user's
1. feed
2. location
3. location_map > html

# Script Installation
```bash
git clone https://github.com/NotoriousArnav/InstagramTimelineAnalyzer.git insta_mapper
cd insta_mapper
pip3 install -r requirements.txt
python3 app.py --help
```

# Basic Script Usage
```bash
$ ./app.py --help
usage: app.py [-h] [--credentialFile CREDENTIALFILE] [--username USERNAME]
              [--outname OUTNAME]

This Program is to Designed to Scrape Instagram User's Map Timeline with a
Proper Geotag, Timestamp, and Media (or Media Abbriviation)

options:
  -h, --help            show this help message and exit
  --credentialFile CREDENTIALFILE
                        The Program Uses this JSON file to Login to Instagram
                        and Fetch Data. Use JSON files with structure: {
                        "username":"foo",
                        "password":"foobar'sSecretPassword123$" }
  --username USERNAME   Username of the the Target.
  --outname OUTNAME     Dump file(s) for Target Info. [ (filename.html -- Map
                        Timeline) (filename.json -- Address and Coordinate
                        Dump based on timestamp.) ] Default Filename is the
                        username provided

```

## NOTE : credentialsFile is Important! It is used to Login to to Private Instagram API
The format for credentialsFile.json is:
```json
{
	"username":"foo",
	"password":"bar"
}
```
##### --outname can be used to Override Default Setting of saving the file with username.json and username.html to outfile.json and outfile.html
##### {}.html file Contains a Map to view in Browser, and Contains all Markers where user have been along with all the Captions and TimeStamp

# Documentation
Looking Carefully at the code, we find 3 Functions:
```python
grab_user_feed
grab_user_location
pin_user_location
```
#### grab_user_feed
Persequites:<br>
	- username : str <br>
	- client : instagram_private_api.Client <br>

Example:
```python
from instagram_private_api import Client
from pprint import pprint # <-- Well You don't ned it, but The console output looks pretty with this 
import app
c = Client(
		username = "foo",
		password = "bar"
	) #Logs in to foo's account with password "bar"
user_posts = app.grab_user_feed("spam_eggs69", c) #Gets most of the Posts
for x in user_posts:
	pprint(x) #print all of them one by one, pretty. (use print for standard print)
```
#### grab_user_location
Persequites:<br>
	- post : dict

Example:
```python3
#Code from previous Example
#Continues here ...
dt = app.grab_user_location(user_posts[0]) # Provide the function with a User Post and it will try to grab the geotag
pprint(dt)
print(f"{isinstance(dt,dict)=}")
```
#### pin_user_location
Persequits:<br>
	- location : data<br>
	- folium_map: folium.Map<br>
Example:
```python3
#Code from Previous Examples Continue here too...
import folium
m = folium.Map()
pin_user_location(dt, m) # Provide the location Data and the map to pin it where.
```
# Features that I will Never Implement (who knows I might Change my mind)
1. Telemetry (Like why?)
2. Batch Processing via cli ( B*tch you can use this as a module now)

# Contribution
We Highly Apperciate Contributions, be it Nice Documentation, be it Translation of Documentation or contributing to actual source code.
But it wont take long to become too messy, so we highly apperiate following the Steps that we provide.
You can [Click Here](https://youtu.be/b_aF5zk22cA) to Get a Idea, how to.
### Steps for Contribution:
1. Fork this Repo
2. clone your Forked Repo to your local machhine
3. Do changes in your version of code and Continue Developing and Commits
4. When you think your changes can pe pulled by us in our repo, make a Pull Request. After Review, We will merge your code with us.
