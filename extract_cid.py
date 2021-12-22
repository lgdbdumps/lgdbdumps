import json
import sys

JSON_FILENAME = sys.argv[1]
OUTPUT_FILENAME = sys.argv[2]
INDEX = int(sys.argv[3])
f = open(JSON_FILENAME)
outf = open(OUTPUT_FILENAME, 'w')
json_data = json.loads(f.read())
l = list(json_data)
nl = ['/ipfs/' + el['cid'] + '\n' for el in l]
outf.write(nl[INDEX])
outf.close()
