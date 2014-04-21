# -*- coding: utf8 -*-
# Run ./download-tld.sh first

f = open('tld.dat', 'r')

CC = {}

for l in f:
	x = l.strip()
	# ignore empty lines, comments, !city.*.jp-like, and unicode
	if x == '' or x[0] == '/' or x[0] == '!' or x[0] > 'z':
		continue
	if x.startswith('*.'):
		x = x[2:]
		if x not in CC: CC[x] = {}
		for sld in ['com', 'gov', 'org', 'edu', 'net', 'biz', 'name', 'info']:
			CC[x][sld] = {}
		continue
	if x.find('.') == -1:
		if x not in CC: CC[x] = {}
		continue
	cc = CC
	for ld in x.split('.')[::-1]:
		if ld not in cc: cc[ld] = {}
		cc = cc[ld]

f.close()

try:
	import cPickle as pickle
except:
	import pickle
with open('tld.pkl', 'wb') as f:
	pickle.dump(CC, f)

#import pprint
#pprint.pprint(CC)
