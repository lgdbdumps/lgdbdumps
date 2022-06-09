import json
import sys

INPUT_FILENAME=sys.argv[1]
f = open(INPUT_FILENAME)
json_data = json.loads(f.read())
print(json_data['cid'])
