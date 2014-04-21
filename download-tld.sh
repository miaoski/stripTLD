#!/bin/bash
wget -O tld.dat 'http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1'
python makecc.py
echo "Generated tld.pkl"
