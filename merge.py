# -*- coding: utf-8 -*-
import os.path
import json

CONTENT_DIR  = "./manual/"
INDEXES_FILE = CONTENT_DIR + "__indexes.json"
OUTPUT_FILE  = CONTENT_DIR + "__merged.md"
NEWPAGE_CODE = '<div style="page-break-before:always"></div>'

f = open(INDEXES_FILE, 'r')
json_array = json.load(f)
f.close()

document = ""

for json_data in json_array:

    # Get File Path and Validate
    if json_data.has_key("file") == False:
        continue

    filepath = CONTENT_DIR + json_data["file"]

    if os.path.exists(filepath) == False:
        print(filepath + " not found.")
        continue

    # Get Title
    title = json_data.get("title", "")

    # Conbine to document
    f = open(filepath)
    data = f.read()
    f.close()

    # Add title
    if title != "":
        document += "\n# " + title.encode("utf-8") + "\n"

    document += data
    document += "\n" + NEWPAGE_CODE + "\n"

f = open(OUTPUT_FILE, "w")
f.write(document)
f.close()
