# Instagram Map Timeline Analyzer
A Simple Script to Parse location data of a Public Instagram Account to a Map and JSON document for Further analysis.

# Installation
```bash
git clone https://github.com/NotoriousArnav/InstagramTimelineAnalyzer.git insta_mapper
cd insta_mapper
pip3 install -r requirements.txt
python3 app.py --help
```

# Basic Usage
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
