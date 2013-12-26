#!/usr/bin/python

'''
Created on Dec 23, 2013


Author Sukhvinder Singh | karramsos@gmail.com | @karramsos

'''

import urllib2

page = urllib2.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
text = page.read().decode("utf8")

#print(text)

price = text[250:255]
print(price)