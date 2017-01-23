#! /usr/bin/python3
#! coding: utf-8

"""
script général du projet pour récupération des informations de tous les fichiers de données brutes
traitement des données vers un format XML à partir de formats JSON, XML et CSV
traitement des données XML vers un format XML pivot
réalisation d'un fichier XML pivot final contenant toutes les données
"""

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import geocoder
import os

# sudo pip3 install dicttoxml nécessaire avant

# Import des modules faits maison
import extraction
import bibliotheque2xml
import jsonxml2xmlpivot
import crous2xml
import json2xml
import loyers
import openbeermap2xml
import openbeermap_pivot
import creation_xml_pivot
import xmlcrous2pivot
import xml_bibli
import grammaire

if __name__ == '__main__':
	fichiers_crees=[]
	fichiers_pivot=[]
	# Definition des chemins
	grammaires="../grammaires/"
	donnees_brutes="../donnees_brutes/"
	donnees_xml="../donnees_xml/"
	xml_formattes_pivot = "../xml_formattes_pivot/"
	# Defiition de la dtd de validation des fichers au format pivot
	dtd_pivot=grammaires+"dtd_fomat_pivot.dtd"

	# cinemas
	print("traitement des données des cinémas")
	# Extraction du fichier sur le web 
	fichier_cinemas_json=donnees_brutes+extraction.ecrire("https://opendata.paris.fr/explore/dataset/cinemas-a-paris/download/?format=json&timezone=Europe/Berlin")
	# Transformation json -> xml
	# definition du nom de fichier xml
	fichier_cinemas_xml=donnees_xml+os.path.basename(fichier_cinemas_json)[:-4]+"xml"
	# Transformation
	json2xml.main(fichier_cinemas_json, fichier_cinemas_xml)
	# Ajout de la grammaire de validation au format dtd
	fichier_cinemas_dtd = grammaires+os.path.basename(fichier_cinemas_json)[:-4]+"dtd"
	grammaire.addDTD(fichier_cinemas_xml,fichier_cinemas_dtd)
	# Passage au format xml_pivot
	# creation d'un dictionnaire normalisé
	dic_cinemas=jsonxml2xmlpivot.getInfos(fichier_cinemas_xml, arrond="arrondissement", nom="nom_etablissement", adresse="adresse", coordinates="coordonnees")
	# ecriture du des données dans le xml au format pivot
	fichier_cinemas_xml_pivot = xml_formattes_pivot+os.path.basename(fichier_cinemas_xml)[:-4]+"_pivot.xml"
	print("Pertes :")
	jsonxml2xmlpivot.writeInFile(dic_cinemas, "cinema", fichier_cinemas_xml_pivot)
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(fichier_cinemas_xml_pivot,dtd_pivot)
	print("le fichier", fichier_cinemas_xml_pivot, "a été créé avec succès")
	fichiers_crees += [fichier_cinemas_json,fichier_cinemas_xml,fichier_cinemas_xml_pivot]
	fichiers_pivot+=[fichier_cinemas_xml_pivot]
	
	print('**************************************')

	# preservatifs
	print("traitement des données des distributeurs de préservatifs")
	# Extraction du fichier sur le web 
	fichier_preservatifs_json=donnees_brutes+extraction.ecrire("https://opendata.paris.fr/explore/dataset/distributeurspreservatifsmasculinsparis2012/download/?format=json&timezone=Europe/Berlin")
	# Transformation json -> xml
	# definition du nom de fichier xml
	fichier_preservatifs_xml=donnees_xml+os.path.basename(fichier_preservatifs_json)[:-4]+"xml"
	# Transformation
	json2xml.main(fichier_preservatifs_json, fichier_preservatifs_xml)
	# Ajout de la grammaire de validation au format dtd
	fichier_preservatifs_dtd = grammaires+os.path.basename(fichier_preservatifs_json)[:-4]+"dtd"
	grammaire.addDTD(fichier_preservatifs_xml,fichier_preservatifs_dtd)
	# Passage au format xml_pivot
	# creation d'un dictionnaire normalisé
	dic_preservatifs=jsonxml2xmlpivot.getInfos(fichier_preservatifs_xml, arrond="arrond", nom="site", adresse="adresse", coordinates="xy")
	# ecriture du des données dans le xml au format pivot
	fichier_preservatifs_xml_pivot = xml_formattes_pivot+os.path.basename(fichier_preservatifs_xml)[:-4]+"_pivot.xml"
	print("Pertes :")
	jsonxml2xmlpivot.writeInFile(dic_preservatifs, "preservatifs", fichier_preservatifs_xml_pivot)
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(fichier_preservatifs_xml_pivot,dtd_pivot)
	print("le fichier", fichier_preservatifs_xml_pivot, "a été créé avec succès")
	fichiers_crees += [fichier_preservatifs_json,fichier_preservatifs_xml,fichier_preservatifs_xml_pivot]
	fichiers_pivot+=[fichier_preservatifs_xml_pivot]

	print('**************************************')

	# cafes
	print("traitement des données des cafés à 1€")
	# Extraction du fichier sur le web 
	fichier_cafes_json=donnees_brutes+extraction.ecrire("https://opendata.paris.fr/explore/dataset/liste-des-cafes-a-un-euro/download/?format=json&timezone=Europe/Berlin")
	# Transformation json -> xml
	# definition du nom de fichier xml
	fichier_cafes_xml=donnees_xml+os.path.basename(fichier_cafes_json)[:-4]+"xml"
	# Transformation
	json2xml.main(fichier_cafes_json, fichier_cafes_xml)
	# Ajout de la grammaire de validation au format dtd
	fichier_cafes_dtd = grammaires+os.path.basename(fichier_cafes_json)[:-4]+"dtd"
	grammaire.addDTD(fichier_cafes_xml,fichier_cafes_dtd)
	# Passage au format xml_pivot
	# creation d'un dictionnaire normalisé
	dic_cafes=jsonxml2xmlpivot.getInfos(fichier_cafes_xml, arrond="arrondissement", nom="nom_du_cafe", adresse="adresse", coordinates="geoloc")
	# ecriture du des données dans le xml au format pivot
	fichier_cafes_xml_pivot = xml_formattes_pivot+os.path.basename(fichier_cafes_xml)[:-4]+"_pivot.xml"
	print("Pertes :")
	jsonxml2xmlpivot.writeInFile(dic_cafes, "cafes", fichier_cafes_xml_pivot)
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(fichier_cafes_xml_pivot,dtd_pivot)
	print("le fichier", fichier_cafes_xml_pivot, "a été créé avec succès")
	fichiers_crees += [fichier_cafes_json,fichier_cafes_xml,fichier_cafes_xml_pivot]
	fichiers_pivot+=[fichier_cafes_xml_pivot]

	print('**************************************')

	# marchés
	print("traitement des données des marchés de quartier")
	# Extraction du fichier sur le web 
	fichier_marches_json=donnees_brutes+extraction.ecrire("https://opendata.paris.fr/explore/dataset/liste_des_marches_de_quartier_a_paris/download/?format=json&timezone=Europe/Berlin")
	# Transformation json -> xml
	# definition du nom de fichier xml
	fichier_marches_xml=donnees_xml+os.path.basename(fichier_marches_json)[:-4]+"xml"
	# Transformation
	json2xml.main(fichier_marches_json, fichier_marches_xml)
	# Ajout de la grammaire de validation au format dtd
	fichier_marches_dtd = grammaires+os.path.basename(fichier_marches_json)[:-4]+"dtd"
	grammaire.addDTD(fichier_marches_xml,fichier_marches_dtd)
	# Passage au format xml_pivot
	# creation d'un dictionnaire normalisé
	dic_marches=jsonxml2xmlpivot.getInfos(fichier_marches_xml, arrond="arrondissement", nom="marche", adresse="adresse_complete_poi_approchant", coordinates="geo_coordinates")
	# ecriture du des données dans le xml au format pivot
	fichier_marches_xml_pivot = xml_formattes_pivot+os.path.basename(fichier_marches_xml)[:-4]+"_pivot.xml"
	print("Pertes :")
	jsonxml2xmlpivot.writeInFile(dic_marches, "marche", fichier_marches_xml_pivot)
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(fichier_marches_xml_pivot,dtd_pivot)
	print("le fichier", fichier_marches_xml_pivot, "a été créé avec succès")
	fichiers_crees += [fichier_marches_json,fichier_marches_xml,fichier_marches_xml_pivot]
	fichiers_pivot+=[fichier_marches_xml_pivot]

	print('**************************************')

	# bars
	print("traitement des données des bars")
	fichier_bars_csv=donnees_brutes+"OpenBeerMap_IDF.csv"
	# extraction.ecrire("Adresse de téléchargement des données des bars")
	# Transformation csv -> xml
	# definition du nom de fichier xml
	fichier_bars_xml=donnees_xml+os.path.basename(fichier_bars_csv)[:-4]+".xml"
	# Transformation
	infile = open(fichier_bars_csv,'r')
	outfile = open(fichier_bars_xml,'w')
	openbeermap2xml.fromcsv2xml(infile, outfile)
	# Ajout de la grammaire de validation au format dtd
	fichier_bars_dtd = grammaires+os.path.basename(fichier_bars_csv)[:-4]+".dtd"
	grammaire.addDTD(fichier_bars_xml,fichier_bars_dtd)
	# Passage au format xml_pivot
	# ecriture du des données dans le xml au format pivot
	soup = BeautifulSoup(open("../donnees_xml/OpenBeerMap_IDF.xml"), "xml")
	liste_noms = []
	for nom in soup.find_all('name'):
		nom = str(nom)
		nom = re.sub('<name>','',nom)
		nom = re.sub('</name>','',nom)
		# print (nom)
		liste_noms.append(nom)
	liste_osm = []
	for osm_id in soup.find_all('osm_id'):
		osm_id = str(osm_id)
		osm_id = re.sub('<osm_id>','',osm_id)
		osm_id = re.sub('</osm_id>','',osm_id)
		liste_osm.append(osm_id)
	print("Pertes :")
	# print('Création du dictionnaire qui contient {bar:nom, latitude, longitude et adresse')
	dic_infos = openbeermap_pivot.recuperation_infos(liste_noms, liste_osm)
	# print("Impression du fichier OpenBeerMap_pivot")
	openbeermap_pivot.impression_xml_pivot(dic_infos)
	fichier_bars_xml_pivot=xml_formattes_pivot+"openbeermap_pivot.xml"
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(fichier_bars_xml_pivot,dtd_pivot)
	print("le fichier", fichier_bars_xml_pivot, "a été créé avec succès")
	fichiers_crees += [fichier_bars_csv,fichier_bars_xml,fichier_bars_xml_pivot]
	fichiers_pivot+=[fichier_bars_xml_pivot]

	print('**************************************')

	# bibliothèques
	print("traitement des données des bibliothèques")
	# Extraction du fichier sur le web 
	fichier_bibli_csv=donnees_brutes+extraction.ecrire("https://opendata.paris.fr/explore/dataset/equipements_de_proximite/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true")
	# Transformation csv -> xml
	# definition du nom de fichier xml
	fichier_bibli_xml=donnees_xml+"Bibliotheque"+".xml"
	# Transformation
	bibliotheque2xml.get_data(fichier_bibli_csv, "Bibliothèque")
	# Ajout de la grammaire de validation au format dtd
	fichier_bibli_dtd = grammaires+os.path.basename(fichier_bibli_csv)[:-4]+".dtd"
	grammaire.addDTD(fichier_bibli_xml,fichier_bibli_dtd)
	# Passage au format xml_pivot
	# ecriture du des données dans le xml au format pivot
	fichier_bibli_xml_pivot=xml_formattes_pivot+os.path.basename(fichier_bibli_xml)[:-4]+"_pivot.xml"
	xml_bibli.ecriture(fichier_bibli_xml,fichier_bibli_xml_pivot)
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(fichier_bibli_xml_pivot,dtd_pivot)
	print("le fichier", fichier_bibli_xml_pivot, "a été créé avec succès")
	fichiers_crees += [fichier_bibli_csv,fichier_bibli_xml,fichier_bibli_xml_pivot]
	fichiers_pivot+=[fichier_bibli_xml_pivot]

	print('**************************************')

	# crous
	print("traitement des données des crous")
	# Extraction du fichier sur le web 
	fichier_crous_xml_brut=donnees_brutes+extraction.ecrire("https://www.data.gouv.fr/s/resources/ensemble-des-lieux-de-restauration-des-crous-france-entiere-1/20160116-000310/crous_restauration_france_entiere.xml")
	# Transformation csv -> xml
	# definition du nom de fichier xml
	print(fichier_crous_xml_brut)
	fichier_crous_xml_nettoye=donnees_xml+os.path.basename(fichier_crous_xml_brut)
	print(fichier_crous_xml_nettoye)
	# Transformation
	crous2xml.clean_crous(fichier_crous_xml_brut)
	# Ajout de la grammaire de validation au format dtd
	fichier_crous_dtd = grammaires+os.path.basename(fichier_crous_xml_brut)[:-4]+".dtd"
	grammaire.addDTD(fichier_crous_xml_nettoye,fichier_crous_dtd)
	# Passage au format xml_pivot
	fichier_crous_xml_pivot=xml_formattes_pivot+os.path.basename(fichier_crous_xml_brut)[:-4]+"_pivot.xml"
	# ecriture du des données dans le xml au format pivot
	dic_crous=jsonxml2xmlpivot.getInfosCrous(fichier_crous_xml_nettoye)
	jsonxml2xmlpivot.writeInFile(dic_crous,"crous", fichier_crous_xml_pivot)
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(fichier_crous_xml_pivot,dtd_pivot)
	print("le fichier", fichier_crous_xml_pivot, "a été créé avec succès")
	fichiers_crees += [fichier_crous_xml_brut,fichier_crous_xml_nettoye,fichier_crous_xml_pivot]
	fichiers_pivot+=[fichier_crous_xml_pivot]


	print('**************************************')

	# loyers
	print("traitement des données des loyers")
	# Extraction du fichier sur le web 
	fichier_loyers_csv=donnees_brutes+"encadrement_loyers_paris.csv"
	# Transformation csv -> dico python à ajouter au xml pivot
	dic_loyers=loyers.create_dic(fichier_loyers_csv)
	print("le fichier", fichier_loyers_csv, "a été traité avec succès")
	fichiers_crees += [fichier_loyers_csv]

	print('**************************************')
	
	print("Création du fichier pivot général à partir des fichiers formatés")
	dic = {}
	for filename in fichiers_pivot:
		if fichiers_pivot.index(filename)==0:
			dic = creation_xml_pivot.open_and_dic(filename,dic)
		else:
			dic.update(creation_xml_pivot.open_and_dic(filename,dic))
	# creation du fichier pivot final
	xml_pivot="../xml_pivot/xml_pivot.xml"
	creation_xml_pivot.out_xml(dic, xml_pivot, dic_loyers)
	# Ajout de la grammaire de validation au format dtd
	grammaire.addDTD(xml_pivot,dtd_pivot)
	fichiers_crees+=[xml_pivot]
	print("Le fichier", xml_pivot, "a été créé avec succès.")
	print("Au total,", len(fichiers_crees), "fichiers ont été créés.")
