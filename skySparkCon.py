import hszinc
hszinc.MODE_ZINC
from pyhaystack.client.skyspark import SkysparkHaystackSession

import logging
logging.getLogger().setLevel(logging.INFO)      # or DEBUG

import certifi
certifi.where()

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import requests.packages.urllib3
from requests.packages.urllib3.exceptions import SubjectAltNameWarning
requests.packages.urllib3.disable_warnings(SubjectAltNameWarning)

import datetime

import pyhaystack
session = pyhaystack.connect(implementation='skyspark',
                                uri='http://54.153.123.192:8080',
                                username='su',
                                password='energydude',
                                project='kW_Link', 
                                pint=True)

#session results
op = session.about()
op.wait()
outputSession = op.result
