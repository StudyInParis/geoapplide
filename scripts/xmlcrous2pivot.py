#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from pprint import pprint
from cinemas2xmlpivot import writeInFile

def getInfos(infilename):
	dic={}
	tree = ET.parse(infilename)
	root = tree.getroot()
	for child in root:
		# dic={}
		if 'Paris' in child.attrib["zone"] and child.attrib["zone"].split()[1] != "Denis":
			id=child.attrib["id"]
			nom=child.attrib["title"]
			lon=child.attrib["lon"]
			lat=child.attrib["lat"]
			arrondissement="750"+child.attrib["zone"].split()[1]
			dic[arrondissement]=dic.get(arrondissement,{})
			for grandchild in list(child):
				if grandchild.tag == "contact":
					adresse=grandchild.text.split("p>")[1].split("</")[0]
					dic[arrondissement][id]={"nom":nom, "adresse":adresse,"coordonnees":[lon, lat]}
	return dic

if __name__ == '__main__':
	fic="restauration_france_entiere.xml"
	dic=getInfos("../donnees_xml/"+fic)
	writeInFile(dic,"crous", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")