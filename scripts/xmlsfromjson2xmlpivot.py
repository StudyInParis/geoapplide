#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from pprint import pprint


def getInfosCinema(infilename):
	dic={}
	tree = ET.parse(infilename)
	root = tree.getroot()
	for child in root:
		id=child.tag
		dic_prov={}
		dic_prov[id]={}
		liste=[]
		for granchild in list(child):
			if granchild.tag == "arrondissement":
				arrondissement=granchild.text
			if granchild.tag in ["adresse","nom_etablissement"]:
				dic_prov[id].update({granchild.tag:granchild.text})
			elif granchild.tag == "coordonnees":
				dic_prov.get(id,{}).update({granchild.tag:[coordonnees.text for coordonnees in granchild]})
				dic[arrondissement]=dic.get(arrondissement,{})
				dic[arrondissement].update(dic_prov)
				dic_prov={}
	return dic

def getInfosCafe(infilename):
	dic={}
	tree = ET.parse(infilename)
	root = tree.getroot()
	for child in root:
		id=child.tag
		dic_prov={}
		dic_prov[id]={}
		for granchild in list(child):
			if granchild.tag == "arrondissement":
				arrondissement=granchild.text
			if granchild.tag in ["adresse","nom_du_cafe"]:
				dic_prov[id].update({granchild.tag:granchild.text})
				# print(dic_prov)
			elif granchild.tag == "geoloc":
				dic_prov[id].update({granchild.tag:[coordonnees.text for coordonnees in granchild]})
				print(dic_prov)
		dic[arrondissement]=dic.get(arrondissement,{})
		dic[arrondissement].update(dic_prov)
		dic_prov={}
	return dic

def getInfosMarche(infilename):
	dic={}
	tree = ET.parse(infilename)
	root = tree.getroot()
	for child in root:
		id=child.tag
		dic_prov={}
		dic_prov[id]={}
		for granchild in list(child):
			if granchild.tag == "arrondissement":
				arrondissement=granchild.text
			if granchild.tag in ["adresse_complete_poi_approchant","marche"]:
				dic_prov[id].update({granchild.tag:granchild.text})
				# print(dic_prov)
			elif granchild.tag == "geo_coordinates":
				dic_prov[id].update({granchild.tag:[coordonnees.text for coordonnees in granchild]})
				print(dic_prov)
		dic[arrondissement]=dic.get(arrondissement,{})
		dic[arrondissement].update(dic_prov)
		dic_prov={}
	return dic

def getInfos(infilename, arrond="arrondissement", nom="nom", adresse="adresse", coordinates="coordonnees"):
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
	for elem in adresse.split():
		if elem.startswith("750"):
			return elem

def writeInFile(dic, outfilename):
	with open(outfilename, 'w') as f:
		f.write("""<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<root>\n""")
		for arrondissement in sorted(list(dic.keys())):
			f.write("""\t<arrondissement num="{}">\n""".format(arrondissement))
			i=0
			for elemnum in dic[arrondissement]:
				# print(elemnum)
				infos=dic[arrondissement][elemnum]
				if len(infos) == 3:
					i+=1
					f.write("""\t\t<element id="{id}" type="{type}">\n""".format(id=i,type="cinema"))
					f.write("""\t\t\t<adresse>{}</adresse>\n""".format(infos["adresse"]))
					f.write("""\t\t\t<nom>{}</nom>\n""".format(infos["nom"]))
					# f.write("""\t\t\t<coordonnees>\n""")
					for coord in infos["coordonnees"]:
						if float(coord) < 10:
							f.write("""\t\t\t<longitude>{}</longitude>\n""".format(coord))
						else:
							f.write("""\t\t\t<latitude>{}</latitude>\n""".format(coord))
					# f.write("""\t\t\t</coordonnees>\n""")
					f.write("""\t\t</element>\n""")
				else:
					print("node number", elemnum, "is uncomplete. removed from final file.")
			f.write("""\t</arrondissement>\n""")
		f.write("""</root>\n""")


if __name__ == '__main__':
	fic="cinemas-a-paris.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="nom_etablissement", adresse="adresse", coordinates="coordonnees")
	print(fic)
	writeInFile(dic, "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")
	
	fic="liste_des_marches_de_quartier_a_paris.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="marche", adresse="adresse_complete_poi_approchant", coordinates="geo_coordinates")
	print(fic)
	writeInFile(dic, "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic = "liste-des-cafes-a-un-euro.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="nom_du_cafe", adresse="adresse", coordinates="geoloc")
	print(fic)
	writeInFile(dic, "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic="distributeurspreservatifsmasculinsparis2012.xml"
	dic=getInfos("../donnees_xml/"+fic, arrond="from_'adresse_complete'", nom="site", adresse="adresse", coordinates="xy")
	print(fic)
	writeInFile(dic, "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")