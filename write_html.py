import csv

MAIN_CSV_OUTPUT = 'main_csv_output'
COMPACT_CSV_OUTPUT = 'compact_csv_output'
WEB_PAGE_OUTPUT = 'output.html'

prefix = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Library Genesis (LibGen.rs) Index of /dbdumps</title>
 </head>
 <body>
<h1>Library Genesis (LibGen.rs) Index of /dbdumps</h1>
  <table>
   <tbody><tr><th>Name</th><th>Last modified</th><th>Size</th><th>Description</th></tr>
   <tr><th colspan="4"><hr></th></tr>'''
line = '<tr><td><a href="{IPFS_GATEWAY:s}{IPFS_HASH:s}?filename={FILENAME:s}">{FILENAME:s}</a></td><td align="right">{DATE:s}</td><td align="right">{SIZE:s}</td><td>main (non-fiction) database dump (generated daily)</td></tr>'
line2 = '<tr><td><a href="{IPFS_GATEWAY:s}{IPFS_HASH:s}?filename={FILENAME:s}">{FILENAME:s}</a></td><td align="right">{DATE:s}</td><td align="right">{SIZE:s}</td><td>main (non-fiction) database compact dump (no record history, hashes, descriptions; generated daily)</td></tr>'
suffix = '''   <tr><th colspan="4"><hr></th></tr>
</tbody></table>

</body></html>'''

html = ''
html += prefix

#main
finput = open(MAIN_CSV_OUTPUT)

lines = [ l for l in list(csv.reader(finput)) ]
finput.close()
l_rev = lines[::-1]
rows = ''
for rec in l_rev:
    rows += line.format(IPFS_GATEWAY="https://ipfs.io", IPFS_HASH=rec[3], FILENAME=rec[0], DATE=rec[1], SIZE=rec[2]) + '\n'

html += rows    

#compact
finput = open(COMPACT_CSV_OUTPUT)
lines = [ l for l in list(csv.reader(finput)) ]
finput.close()
l_rev = lines[::-1]
rows = ''
for rec in l_rev:
    rows += line2.format(IPFS_GATEWAY="https://ipfs.io", IPFS_HASH=rec[3], FILENAME=rec[0], DATE=rec[1], SIZE=rec[2]) + '\n'

html += rows
html += suffix

foutput = open(WEB_PAGE_OUTPUT, 'w')
foutput.write(html)
foutput.close()
