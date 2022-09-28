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
Currently, the code is way too messy! The Documentation will be Published after Refactoring the existing code.

# Contribution
We Highly Apperciate Contributions, be it Nice Documentation, be it Translation of Documentation or contributing to actual source code.
But it wont take long to become too messy, so we highly apperiate following the Steps that we provide.
You can [Click Here](https://youtu.be/b_aF5zk22cA) to Get a Idea, how to.
### Steps for Contribution:
1. Fork this Repo
2. clone your Forked Repo to your local machhine
3. Do changes in your version of code and Continue Developing and Commits
4. When you think your changes can pe pulled by us in our repo, make a Pull Request. After Review, We will merge your code with us.
