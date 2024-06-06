#! /usr/bin/python3
import subprocess
from os import listdir, path
from datetime import datetime

# personal settings, you'll wanna change these.
title = "flat's gemlog"
desc = "probably not so up to date."

# blog/technical settings, ignore tells the program which .gmi files to ignore.
timeformat = "%Y-%m-%d"
ignore = ["index.gmi",]
gemfeed = "True"
gemfeed_path = "../gemfeed.py"
url = "gemini://tilde.team/~flat"

f = open("index.gmi", "w")
f.write(f"# {title}\n## {desc}\n")
if gemfeed:
    f.write("=> atom.xml feed\n")

for post in listdir():
    if post[-4:] == ".gmi" and post not in ignore:
        f.write(f"\n=> {post} {datetime.fromtimestamp(path.getmtime(post)).strftime(timeformat)} - {post[:-4]}")

f.close()

if gemfeed:
    subprocess.call(["python", gemfeed_path, "-b", url, "-d", "."]) 
