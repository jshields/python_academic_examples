#!/usr/bin/python
"""shields.util.web web module - basic http requests"""
# https://docs.python.org/2/library/htmlparser.html
# https://docs.python.org/2/howto/urllib2.html
import sys
import os
import re
import json
#import urllib
import urllib2
import requests
#import cookielib
#import types

from HTMLParser import HTMLParser
from requests.auth import HTTPBasicAuth
from getpass import getpass

print "Testing web module"

response = urllib2.urlopen('http://python.org/')
html = response.read()
#'<html><head><title>Test</title></head>'
#'<body><h1>Parse me!</h1></body></html>'

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	"""Basic exampple of an HTMLParser subclass"""
	def handle_starttag(self, tag, attrs):
		print "Encountered a start tag:", tag
	def handle_endtag(self, tag):
		print "Encountered an end tag :", tag
	def handle_data(self, data):
		print "Encountered some data  :", data

# instantiate the parser and feed it some HTML
#parser = MyHTMLParser()
#parser.feed(html)


# requests
session = requests.session()

def get(url):
	return session.get(url).json()

resp = get('http://jsonplaceholder.typicode.com/posts/1')

for i in resp:
	print(i, resp[i])

print(resp['title'])
resp['title'] = 'Lorem Ipsum'
print(resp['title'])

