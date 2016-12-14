#!/usr/bin/python3
#! coding: utf-8

import csv
import codecs, sys
from xml.sax.saxutils import escape

def conversion(infilename, file_encoding):
	print(infilename[:-4]+".xml")
	xmlfile=codecs.open(infilename[:-4]+".xml", 'w', 'utf-8')
	xmlfile.write("""<?xml version="1.0" encoding="utf-8"?>\n<root>\n""")
	with open(infilename) as csvfile:
		reader = csv.DictReader(csvfile)
		i=1
		for row in reader:
			xmlfile.write("""\t<element id="{}">\n""".format(str(i)))
			for data in row:
				content=prepare(row[data])
				xmlfile.write("\t\t<"+data+">"+content.decode(file_encoding)+"</"+data+">\n")
			xmlfile.write("\t</element>\n")
			i+=i
	xmlfile.write("""</root>""")

def prepare(string):
	metachars=["<","&",">"]
	for char in metachars:
		if char in string:
			string=escape(string)
			print(char)
			print(string)
	return string


if __name__ == '__main__':
	print(sys.argv)
	conversion(sys.argv[1], sys.argv[2])