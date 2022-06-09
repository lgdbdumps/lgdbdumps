import json
import sys

JSON_FILENAME = sys.argv[1]
OUTPUT_FILENAME = sys.argv[2]
f = open(JSON_FILENAME)
outf = open(OUTPUT_FILENAME, 'w')
json_data = json.loads(f.read())
dict_lst = list(json_data)
length=len(dict_lst)
fnames=[]
cids = ['/ipfs/' + el['cid'] + '\n' for el in dict_lst]
sizes = [ el['dagSize'] / (1024 * 1024) for el in dict_lst]
dates = [el['created'].split('T')[0] for el in dict_lst]
for i in range(length):
  if i % 2 == 0:
    name='libgen_'
  else:
    name='libgen_compact_'
  fnames.append(name)
for i in range(length): 
  outf.write("%s,%s,%s,%s" % (fnames[i]+dates[i]+'.rar' sizes[i], dates[i], cids[i]))  
outf.close()
