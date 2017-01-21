#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from pprint import pprint

def getInfosCrous(infilename):
	"""
	fonction qui parse un fichier XML et renvoie son contenu sous forme d'un dictionnaire
	entree : nom de fichier
	sortie : dictionnaire {id:[nom, adresse, coordonnees]}
	"""
	print(infilename)
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

def getInfos(infilename, arrond="arrondissement", nom="nom", adresse="adresse", coordinates="coordonnees"):
	"""
	entree : fichier XML
	sortie : dictionnaire
	"""
	arrondissement = ""
	dic={}
	tree = ET.parse(infilename)
	root = tree.getroot()
	for child in root:
		id=child.tag
		dic_prov={}
		dic_prov[id]={}
		for granchild in list(child):
			if "'" in arrond:
				arrondissement=getArrondFromAdress(arrond.split("'")[1])
			else:
				if granchild.tag == arrond:
					arrondissement=granchild.text
			if granchild.tag in [adresse,nom]:
				dic_prov[id].update({granchild.tag.replace(adresse,"adresse").replace(nom,"nom"):granchild.text})
				# print(dic_prov)
			if coordinates:
				if granchild.tag == coordinates:
					dic_prov[id].update({granchild.tag.replace(coordinates,"coordonnees"):[coordonnees.text for coordonnees in granchild]})
					# print(dic_prov)
		dic[arrondissement]=dic.get(arrondissement,{})
		dic[arrondissement].update(dic_prov)
		dic_prov={}
	return dic

def getArrondFromAdress(adresse):
	"""
	fonction qui détermine le numéro d'arrondissement
	entree: adresse
	sortie : numéro d'arrondissement
	"""
	for elem in adresse.split():
		if elem.startswith("750"):
			return elem

def writeInFile(dic, typeLieu, outfilename):
	"""
	entree :
	sortie : 
	"""
	with open(outfilename, 'w') as f:
		f.write("""<?xml version="1.0" encoding="UTF-8" ?>\n<root>\n""")
		i=0
		for arrondissement in sorted(list(dic.keys())):
			f.write("""\t<arrondissement num="{}">\n""".format(arrondissement))
			for elemnum in dic[arrondissement]:
				i +=1
				# print(elemnum)
				infos=dic[arrondissement][elemnum]
				if len(infos) == 3:
					f.write("""\t\t<element id="{id}" type="{type}">\n""".format(id=i,type=typeLieu))
					for coord in infos["coordonnees"]:
						if float(coord) < 10:
							f.write("""\t\t\t<longitude>{}</longitude>\n""".format(coord))
						else:
							f.write("""\t\t\t<latitude>{}</latitude>\n""".format(coord))
					# f.write("""\t\t\t</coordonnees>\n""")
					f.write("""\t\t\t<adresse>{}</adresse>\n""".format(infos["adresse"]))
					f.write("""\t\t\t<nom>{}</nom>\n""".format(infos["nom"]))
					# f.write("""\t\t\t<coordonnees>\n""")
					f.write("""\t\t</element>\n""")
				else:
					print("node number", elemnum, "is uncomplete. removed from final file.")
			f.write("""\t</arrondissement>\n""")
		f.write("""</root>\n""")


if __name__ == '__main__':
	fic="cinemas-a-paris.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="nom_etablissement", adresse="adresse", coordinates="coordonnees")
	print(fic)
	writeInFile(dic, "cinema", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")
	
	fic="liste_des_marches_de_quartier_a_paris.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="marche", adresse="adresse_complete_poi_approchant", coordinates="geo_coordinates")
	print(fic)
	writeInFile(dic, "marche", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic = "liste-des-cafes-a-un-euro.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="nom_du_cafe", adresse="adresse", coordinates="geoloc")
	print(fic)
	writeInFile(dic,"cafe", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic="distributeurspreservatifsmasculinsparis2012.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="arrond", nom="site", adresse="adresse", coordinates="xy")
	print(fic)
	writeInFile(dic,"preservatifs", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic="restauration_france_entiere.xml"
	dic=getInfosCrous("../donnees_xml/"+fic)
	print(fic)
	writeInFile(dic,"crous", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")