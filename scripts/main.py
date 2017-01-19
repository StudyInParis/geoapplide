#! /usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

# sudo pip3 install dicttoxml nécessaire avant

# Import des modules faits maison
import bibliotheque2xml
import json2xml2
import openbeermap2xml
import crous2xml
import loyers
import test_xml_pivot
import openbeermap_pivot2
from openbeermap_pivot2 import recuperation_infos
from openbeermap_pivot2 import impression_xml_pivot

if __name__ == '__main__':
	print("Création du fichier xml des bibliothèques")
	bibliotheque2xml.get_data("../donnees_brutes/equipements_de_proximite.csv", "Bibliothèque")

	print("Création des fichiers xml à partir des fichiers json")
	liste=["annuaire_immobilier_de_l_enseignement_superieur","liste-des-cafes-a-un-euro","quartier_paris", "liste_des_marches_de_quartier_a_paris","cinemas-a-paris", "distributeurspreservatifsmasculinsparis2012"]

	# ~~~~~~~ TODO : appliquer chaque fonction orig->format_pivot à chaque fichier ~~~~~~~~ OK
	print("Traitement du fichier : ")
	for fichier in liste:
		infile="../donnees_brutes/"+fichier+".json"
		outfile="../donnees_xml/"+fichier+".xml"
		print("\t"+fichier)
		json2xml2.main(infile, outfile)

	print("Récupération des données d'OpenBeerMap")
	infile = open('../donnees_brutes/OpenBeerMap_IDF.csv','r')
	outfile = open('../donnees_xml/OpenBeerMap.xml','w')
	openbeermap2xml.fromcsv2xml(infile, outfile)

	print("Création du fichier des CROUS")
	crous2xml.clean_crous('../donnees_brutes/restauration_france_entiere.xml')

	print("Création du fichier xml_pivot")
	# première étape, formalisation des xml vers un format xml_pivot

	print("parser le fichier xml en entrée")
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


	print('création du dictionnaire qui contient nom, latitude, longitude et adresse pour chaque bar')
	dic_infos = recuperation_infos(liste_noms, liste_osm)
	print("Impression du fichier de sortie")
	impression_xml_pivot(dic_infos)

	# deuxième étape, utilisation des fichiers au format pivot pour la création du  fichier pivot final
	# TODO : faire une boucle recursive sur les fichiers du dossier "../xml_formattes_pivot/" et sortir le xml_pivot dans un autre dossier pour eviter doublons si le script est relancé.
	dic = {}
	dic = test_xml_pivot.open_and_dic("../xml_formattes_pivot/cinemas-a-paris_pivot.xml",dic)
	dic.update(test_xml_pivot.open_and_dic("../xml_formattes_pivot/Bibliotheque_modele.xml",dic))
	dic.update(test_xml_pivot.open_and_dic("../xml_formattes_pivot/distributeurspreservatifsmasculinsparis2012_pivot.xml",dic))
	dic.update(test_xml_pivot.open_and_dic("../xml_formattes_pivot/liste_des_marches_de_quartier_a_paris_pivot.xml",dic))
	dic.update(test_xml_pivot.open_and_dic("../xml_formattes_pivot/liste-des-cafes-a-un-euro_pivot.xml",dic))
	dic.update(test_xml_pivot.open_and_dic("../xml_formattes_pivot/openbeermap_pivot.xml",dic))
	dic.update(test_xml_pivot.open_and_dic("../xml_formattes_pivot//restauration_france_entiere_pivot.xml",dic))

	#pprint(dic)
	test_xml_pivot.out_xml(dic, "../xml_pivot.xml")
