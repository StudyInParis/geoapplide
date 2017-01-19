#! /usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import geocoder

# sudo pip3 install dicttoxml nécessaire avant

# Import des modules faits maison
import bibliotheque2xml
import cinemas2xmlpivot
import crous2xml
import json2xml
import loyers
import openbeermap2xml
import openbeermap_pivot
import creation_xml_pivot
import xmlcrous2pivot

if __name__ == '__main__':
	print("Création du fichier xml des bibliothèques")
	bibliotheque2xml.get_data("../donnees_brutes/equipements_de_proximite.csv", "Bibliothèque")

	print("Création des fichiers xml à partir des fichiers json")
	liste=["annuaire_immobilier_de_l_enseignement_superieur","quartier_paris", "liste_des_marches_de_quartier_a_paris","cinemas-a-paris", "distributeurspreservatifsmasculinsparis2012", "liste-des-cafes-a-un-euro"]

	print("Traitement du fichier : ")
	for fichier in liste:
		infile="../donnees_brutes/"+fichier+".json"
		outfile="../donnees_xml/"+fichier+".xml"
		print("\t"+fichier)
		json2xml.main(infile, outfile)

	print("Traitement du fichier OpenBeerMap")
	infile = open('../donnees_brutes/OpenBeerMap_IDF.csv','r')
	outfile = open('../donnees_xml/OpenBeerMap.xml','w')
	openbeermap2xml.fromcsv2xml(infile, outfile)

	print("Traitement du fichier des CROUS")
	crous2xml.clean_crous('../donnees_brutes/restauration_france_entiere.xml')


	print("Création du fichier xml_pivot")
	# première étape, formalisation des xml vers un format xml_pivot

	print("Formalisation du fichier OpenBeerMap")
	soup = BeautifulSoup(open("../donnees_xml/OpenBeerMap.xml"), "xml")
	liste_noms = []
	for nom in soup.find_all('name'):
		nom = str(nom)
		nom = re.sub('<name>','',nom)
		nom = re.sub('</name>','',nom)
		print (nom)
		liste_noms.append(nom)
	liste_osm = []
	for osm_id in soup.find_all('osm_id'):
		osm_id = str(osm_id)
		osm_id = re.sub('<osm_id>','',osm_id)
		osm_id = re.sub('</osm_id>','',osm_id)
		liste_osm.append(osm_id)

	print('Création du dictionnaire qui contient nom, latitude, longitude et adresse pour chaque bar')
	dic_infos = openbeermap_pivot.recuperation_infos(liste_noms, liste_osm)
	print("Impression du fichier OpenBeerMap_pivot")
	openbeermap_pivot.impression_xml_pivot(dic_infos)


	print("Création des autres fichiers au format xml pivot")
	fic="cinemas-a-paris.xml"
	dic=cinemas2xmlpivot.getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="nom_etablissement", adresse="adresse", coordinates="coordonnees")
	print(fic)
	cinemas2xmlpivot.writeInFile(dic, "cinema", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")
	
	fic="liste_des_marches_de_quartier_a_paris.xml"
	dic=cinemas2xmlpivot.getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="marche", adresse="adresse_complete_poi_approchant", coordinates="geo_coordinates")
	print(fic)
	cinemas2xmlpivot.writeInFile(dic, "marche", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic = "liste-des-cafes-a-un-euro.xml"
	dic=cinemas2xmlpivot.getInfos("../donnees_xml/"+fic, arrond="arrondissement", nom="nom_du_cafe", adresse="adresse", coordinates="geoloc")
	print(fic)
	cinemas2xmlpivot.writeInFile(dic,"cafe", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic="distributeurspreservatifsmasculinsparis2012.xml"
	dic=cinemas2xmlpivot.getInfos("../donnees_xml/"+fic, arrond="arrond", nom="site", adresse="adresse", coordinates="xy")
	print(fic)
	cinemas2xmlpivot.writeInFile(dic,"preservatifs", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	fic="restauration_france_entiere.xml"
	dic=cinemas2xmlpivot.getInfosCrous("../donnees_xml/"+fic)
	print(fic)
	cinemas2xmlpivot.writeInFile(dic,"crous", "../xml_formattes_pivot/"+fic[:-4]+"_pivot.xml")

	print("Création du fichier pivot des bibliothèques")
	fic = open("../donnees_xml/Bibliotheque.xml","r")
	out = open("../xml_formattes_pivot/Bibliotheque_pivot.xml","w")
	out.write(fic.readline())
	out.write("<root>\n")
	dico = {}
	dico2 = {}
	num_l=0
	lines =fic.readlines()
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


	# deuxième étape, utilisation des fichiers au format pivot pour la création du  fichier pivot final
	# TODO : faire une boucle recursive sur les fichiers du dossier "../xml_formattes_pivot/" et sortir le xml_pivot dans un autre dossier pour eviter doublons si le script est relancé.
	print("Création du fichier pivot général à partir des fichier formatés")
	dic = {}
	dic = creation_xml_pivot.open_and_dic("../xml_formattes_pivot/cinemas-a-paris_pivot.xml",dic)
	dic.update(creation_xml_pivot.open_and_dic("../xml_formattes_pivot/Bibliotheque_pivot.xml",dic))
	dic.update(creation_xml_pivot.open_and_dic("../xml_formattes_pivot/distributeurspreservatifsmasculinsparis2012_pivot.xml",dic))
	dic.update(creation_xml_pivot.open_and_dic("../xml_formattes_pivot/liste_des_marches_de_quartier_a_paris_pivot.xml",dic))
	dic.update(creation_xml_pivot.open_and_dic("../xml_formattes_pivot/liste-des-cafes-a-un-euro_pivot.xml",dic))
	dic.update(creation_xml_pivot.open_and_dic("../xml_formattes_pivot/openbeermap_pivot.xml",dic))
	dic.update(creation_xml_pivot.open_and_dic("../xml_formattes_pivot/restauration_france_entiere_pivot.xml",dic))

	creation_xml_pivot.out_xml(dic, "../xml_pivot/xml_pivot.xml")
