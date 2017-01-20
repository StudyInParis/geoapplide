#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from pprint import pprint
from jsonxml2xmlpivot import writeInFile

"""
script pour récupérer les infos du fichier CROUS et renvoyer un dictionnaire pour impression dans un fichier de sortie au format XML
utilisation de la fonction writeInFile du fichier jsonxml2xmlpivot pour impression du fichier de sortie
"""

def getInfos(infilename):
	"""
	parcours le fichier XML et renvoie un dictionnaire poru permettre la création du fichier XML formatés
	entree : nom du fichier
	sortie : dictionnaire {arrondissement : {id : {adresse:value, coordonnees : [lat, lon], nom:value}}}
	"""
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