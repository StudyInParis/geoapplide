#!\C:\Users\marcel\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.5
#! coding:utf-8
import sys
import math
import geocoder
from pprint import pprint
"""
script pour traitement des bibliothèques
récupération des informations du fichier XML des bibliothèques pour mise au format du fichier XML pivot
"""
def open_2dico(url):
	fic = open(url,"r")
	dico = {}
	dico2 = {}
	num_l=0
	lines =fic.readlines()
	fic.close()
	for line in lines:
		num_l+=1
		if "<elem" in line:
			dico[line] = lines[num_l:num_l+8]
	for cle in dico:
		for balise in dico[cle]:
			if "750" in balise:
				if balise not in dico2:
					dico2[balise] = [dico[cle]]
				else:
					dico2[balise] += [dico[cle]]
	return (dico2)
def ecriture(url,url2):
	dico2 = open_2dico(url)
	out = open(url2,"w")
	out.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
	out.write("<root>\n")
	num_bib = 0
	for cle in dico2:
		clef = cle.split("<")[1].split(">")[1]
		out.write('\t<arrondissement num ="'+clef+'">\n')
		for item in dico2[cle]:
			num_bib +=1
			out.write('\t\t<element id="'+str(num_bib)+'" type="bibli">\n')
			for balise in item:
				if"Designation" in balise:
					name = balise.split("<")[1].split(">")[1]
					if 'DURAS' in name:
						name ='BIBLIOTHEQUE MEDIATHEQUE MARGUERITE DURAS'
					out.write("\t\t\t<nom>"+name.lower()+"</nom>\n")
				if "voie" in balise:
					for bal in item:
						if "num" in bal:
							balises = balise.split("<")[1].split(">")[1]
							bals = bal.split("<")[1].split(">")[1]
							adresse = bals+", "+balises.lower()
							out.write("\t\t\t<adresse>"+adresse+"</adresse>\n")
							g=geocoder.google(adresse)
							out.write("\t\t\t<longitude>"+str(g.lng)+"</longitude>\n")	
							out.write("\t\t\t<latitude>"+str(g.lat)+"</latitude>\n")
			out.write("\t\t</element>\n")
		out.write("\t</arrondissement>\n")
	out.write("</root>")
	out.close()

if __name__ == '__main__':
	ecriture("../donnees_xml/Bibliotheque.xml","../xml_formattes_pivot2/Bibliotheque_pivot.xml")


	