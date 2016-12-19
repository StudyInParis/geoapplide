#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET

def getInfos(infilename):
	dic={}
	tree = ET.parse(infilename)
	root = tree.getroot()
	for child in root:
		for granchild in list(child):
			if granchild.tag == "arrondissement":
				arrondissement=granchild.text
			if granchild.tag in ["adresse","nom_etablissement"]:
				print(arrondissement)
				# dic[arrondissement]=dic.get(granchild.text,{})
				print(granchild.tag, granchild.text)
			elif granchild.tag == "coordonnees":
				print([coordonnees.text for coordonnees in granchild])

"""
TODO :
	pour chaque enfant de root:
		récuperer arrondissement = cle
			sous clé = i
			en faire cle de dic
			récuperer ses frères ssi == "adresse","nom_etablissement", "coordonnees"
			si "coordonnees" => list
				pour chaque coordonnee si float(coordonnee) > 10 :
					lat
				sinon:
					long

"""

if __name__ == '__main__':
	getInfos("../donnees_xml/cinemas-a-paris.xml")