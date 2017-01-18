#! /usr/bin/python3
#! coding: utf-8

from lxml import etree

# sudo pip3 install dicttoxml nécessaire avant

# Import des modules faits maison
import bibliotheque2xml
import json2xml2
import openbeermap2xml
import crous2xml
import loyers
import test_xml_pivot

# ici j'ai modifié les imports pour qu'on puisse voir plus facilement quels scripts sont utilisés où
# aide pour le debug et la compréhension du bouzin

if __name__ == '__main__':
	print("Création du fichier xml des bibliothèques")
	bibliotheque2xml.get_data("../donnees_brutes/equipements_de_proximite.csv", "Bibliothèque")

	print("Création des fichiers xml à partir des fichiers json")
	liste=["annuaire_immobilier_de_l_enseignement_superieur","liste-des-cafes-a-un-euro","quartier_paris", "liste_des_marches_de_quartier_a_paris","cinemas-a-paris", "distributeurspreservatifsmasculinsparis2012"]
	# Traceback (most recent call last):
	#   File "main.py", line 20, in <module>
	#     main(infile, outfile)
	#   File "/home/mathilde/Dropbox/coursS1/geoapplide/scripts/json2xml2.py", line 40, in main
	#     output.write(xml_file)
	# TypeError: write() argument must be str, not bytes
	# => Erreur dûe à un json2xml2 qui est en python2 et appelé en python3
	# les strings ne sont pas encodées pareil selon les versions
	# => dicttoxml renvoie des bytes au lieu d'une string
	# ~~~~~TODO : debugger~~~~ DONE, ajout ouverture en mode binaire dans json2xml2.main()


	# ~~~~~~~ TODO : appliquer chaque fonction orig->format_pivot à chaque fichier ~~~~~~~~ OK
	for fichier in liste:
		infile="../donnees_brutes/"+fichier+".json"
		outfile="../donnees_xml/"+fichier+".xml"
		print("Traitement du fichier : ",fichier)
		json2xml2.main(infile, outfile)

	print("Récupération des données d'OpenBeerMap")
	infile = open('../donnees_brutes/OpenBeerMap_IDF.csv','r')
	outfile = open('../donnees_xml/OpenBeerMap.xml','w')
	openbeermap2xml.fromcsv2xml(infile, outfile)

	print("Création du fichier des CROUS")
	crous2xml.clean_crous('../donnees_brutes/restauration_france_entiere.xml')

	print("Création du fichier xml_pivot")
	# première étape, formalisation des xml vers un format xml_pivot
	

	#erreur dans ce bloc, incompréhensible, le xml est bien formé d'apres XML_copy_editor et le W3C validator
	# TODO : trouver un autre parser/trouver l'erreur
	# print("Parser le fichier OpenBeerMap xml en entrée")
	# parser = etree.XMLParser(recover=True)
	# tree = etree.parse('../donnees_xml/OpenBeerMap.xml')
	# root = tree.getroot()
	# liste_noms = root.xpath("//name/text()")
	# liste_osm = root.xpath("//osm_id/text()")
	# dic_infos = recuperation_infos(liste_noms, liste_osm)
	# impression_xml_pivot(dic_infos)
	# renvoie une erreur dans le parse du ficheir openbeermap

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
