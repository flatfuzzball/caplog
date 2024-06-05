from os import listdir, path
from datetime import datetime

# personal settings, you'll wanna change these.
title = "boblog"
author = "bob"
desc = "bobs awesome gemlog!"
url = "gemini://geminiprotocol.net/"

# blog/technical settings, ignore tells the program which .gmi files to ignore.
timeformat = "%Y-%m-%d"
ignore = ["index.gmi",]

f = open("index.gmi", "w")
f.write(f"# {title}\n## {desc}\n")


for post in listdir():
    if post[-4:] == ".gmi" and post not in ignore:
        f.write(f"\n=> {post} {datetime.fromtimestamp(path.getmtime(post)).strftime(timeformat)} - {post[:-4]}")

f.close()
