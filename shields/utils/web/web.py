#!/bin/python
# https://docs.python.org/2/library/htmlparser.html
# https://docs.python.org/2/howto/urllib2.html
from HTMLParser import HTMLParser
import urllib2

print "Testing web module"

response = urllib2.urlopen('http://python.org/')
html = response.read()
#'<html><head><title>Test</title></head>'
#'<body><h1>Parse me!</h1></body></html>'

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and feed it some HTML

parser = MyHTMLParser()
parser.feed(html)