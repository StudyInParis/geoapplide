#! /usr/bin/python
#! coding: utf-8

import os

def addDTD(xmlfile,dtdpath):
	f=open(xmlfile, "r").read()
	try:
		content=f.split("""<?xml version="1.0" encoding="UTF-8" ?>""")[1]
		xmldecl="""<?xml version="1.0" encoding="UTF-8" ?>"""
	except IndexError:
		print("*********************",xmlfile,"*************************")
		content=f
		xmldecl="""<?xml version="1.0" encoding="UTF-8" ?>"""
	f=open(xmlfile, "w")
	f.write(xmldecl+'\n')
	f.write("<!DOCTYPE root SYSTEM "+'"'+dtdpath+'"'+">\n")
	f.write(content)
	f.close()

if __name__ == '__main__':
	addDTD("../donnees_xml/OpenBeerMap_IDF.xml","../grammaires/OpenBeerMap_IDF.dtd")
	addDTD("../xml_formattes_pivot/openbeermap_pivot.xml","../grammaires/dtd_fomat_pivot.dtd")