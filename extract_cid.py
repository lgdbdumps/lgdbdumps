import json
import sys

MAIN_CSV_OUTPUT = 'main_csv_output'
COMPACT_CSV_OUTPUT = 'compact_csv_output'

JSON_FILENAME = sys.argv[1]
f = open(JSON_FILENAME)
outf = open(MAIN_CSV_OUTPUT, 'w')
outf2 = open(COMPACT_CSV_OUTPUT, 'w')
json_data = json.loads(f.read())
dict_lst = list(json_data)
length=len(dict_lst)
fnames=[]
cids = ['/ipfs/' + el['cid'] + '\n' for el in dict_lst]
sizes = [ el['dagSize'] for el in dict_lst]
dates = [el['created'].split('T')[0] for el in dict_lst]
limit = 1024 ** 3
limit2 = 100 * 1024 * 1024 
for i in range(length):
  if int(sizes[i]) > limit:
    name='libgen_'
  elif int(sizes[i]) > limit2:
    name='libgen_compact_'
  else:
    name=None
  fnames.append(name)
for i in range(length):
  if int(sizes[i]) > limit and fnames[i] not None:
    outf.write("%s,%s,%s,%s" % (fnames[i]+dates[i]+'.rar', str(int(sizes[i] / (1024 * 1024) ))+'M', dates[i], cids[i]))
  elif int(sizes[i]) > limit2 and fnames[i] not None:
    outf2.write("%s,%s,%s,%s" % (fnames[i]+dates[i]+'.rar', str(int(sizes[i] / (1024 * 1024)))+'M', dates[i], cids[i]))
outf.close()
outf2.close()
