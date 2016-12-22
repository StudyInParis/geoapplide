#!/usr/bin/python3
# coding: utf-8
import glob,re
from pprint import pprint
def open_and_dic(fichier,dic):
	fic = open(fichier,'r')
	lines = fic.readlines()
	num_l=0
	for line in lines:
		num_l +=1
		#print(num_l)
		if "<arron" in line:
			arr = line.split('"')[1]
			for ligne in lines[num_l:]:
				if "</arr" in ligne:
					break
				if arr not in dic:
					dic[arr] = []
				dic[arr] += [ligne]
	return dic
def out_xml(dico):
	fic = open("../xml_formattes_pivot/xml_pivot.xml",'w')
	fic.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\n<root>\n")
	compteur = 0
	for cle in sorted(dico):
		fic.write("\t<arrondissement num=\""+cle+"\">\n")
		for ligne in dico[cle]:
			if "<elem" in ligne:
				compteur +=1
				ligne = re.sub(r"[0-9]+",str(compteur),ligne)
			if "&" in ligne:
				ligne =ligne.replace('&',"&amp;")
			fic.write(ligne)
		fic.write("\t</arrondissement>\n")
	fic.write("</root>")
if __name__=='__main__':
	dic = {}
	for fic in glob.glob("../xml_formattes_pivot/*.xml"):
		dic = open_and_dic(fic,dic)
	#pprint(dic)
	out_xml(dic)
