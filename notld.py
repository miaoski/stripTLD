# -*- coding: utf8 -*-

import sys

try:
	import cPickle as pickle
except:
	import pickle
with open('tld.pkl', 'rb') as f:
	TLD_LIST = pickle.loads(f.read())


def isIP(s):
	import re
	IP_RE = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
	return IP_RE.match(s) is not None


def trimTLD(domain):
	"www.some-domain.com -> www.some-domain"
	global TLD_LIST
	if isIP(domain):
		return domain
	if domain.find('.') == -1:
		return domain
	xs = domain.split('.')
	cc = TLD_LIST
	while True:
		if xs[-1] not in cc.keys():
			return '.'.join(xs)
		ld = xs.pop()
		cc = cc[ld]


def midDomain(domain):
	"www.some-domain.com -> some-domain"
	n = trimTLD(domain)
	if n.find('.') == -1:
		return n
	else:
		return n.split('.')[-1]


def runSelfTest():
	testDomains = [
		'a.c.appier.net',
		'view.atdmt.com',
		'api.facebook.com',
		'class.ruten.com.tw',
		'ajax.googleapis.com',
		'test.co.uk',
		'dic.yahoo.jp',
		'www.test.bungaku.ac.jp',
		'test.1.bg',
		'secondlevel.bg',
		'myhotel.gonohe.aomori.jp',
		]
	for i in testDomains:
		print i + '\t' + trimTLD(i) + '\t' + midDomain(i)

if __name__ == '__main__':
	import sys
	for x in sys.stdin:
		i = x.strip()
		print i + '\t' + trimTLD(i) + '\t' + midDomain(i)
