#! usr/bin/python3
#! coding: utf-8

#todo : finir

import json
import xml.etree.ElementTree as ET

def readXML(infilename):
	tree = ET.parse(infilename)
	root = tree.getroot()
	for child in root:
		print(child)

if __name__ == '__main__':
	readXML("../xml_formattes_pivot/xml_pivot.xml")