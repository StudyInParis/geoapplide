from lxml import etree

from bibliotheque2xml import *
# sudo pip3 install dicttoxml nécessaire avant
from json2xml2 import *
from openbeermap2xml import *
from crous2xml import *
from loyers import *

if __name__ == '__main__':
	print("Création du fichier xml des bibliothèques")
	get_data("../donnees_brutes/equipements_de_proximite.csv", "Bibliothèque")

	print("Création des fichiers xml à partir des fichiers json")
	liste=["annuaire_immobilier_de_l_enseignement_superieur","liste-des-cafes-a-un-euro","quartier_paris", "liste_des_marches_de_quartier_a_paris","cinemas-a-paris", "distributeurspreservatifsmasculinsparis2012"]
# Traceback (most recent call last):
#   File "main.py", line 20, in <module>
#     main(infile, outfile)
#   File "/home/mathilde/Dropbox/coursS1/geoapplide/scripts/json2xml2.py", line 40, in main
#     output.write(xml_file)
# TypeError: write() argument must be str, not bytes
# => dicttoxml renvoie des bytes au lieu d'une string

	# for fichier in liste:
	# 	infile="../donnees_brutes/"+fichier+".json"
	# 	outfile="../donnees_xml/"+fichier+".xml"
	# 	print("Traitement du fichier : ",fichier)
	# 	main(infile, outfile)

	print("Récupération des données d'OpenBeerMap")
	infile = open('../donnees_brutes/OpenBeerMap_IDF.csv','r')
	outfile = open('../donnees_xml/OpenBeerMap.xml','w')
	fromcsv2xml(infile, outfile)

	print("Création du fichier des CROUS")
	clean_crous('../donnees_brutes/crous_restauration_france_entiere.xml')

	print("Création du fichier xml_pivot")
	# première étape, formalisation des xml vers un format xml_pivot
	print("Parser le fichier OpenBeerMap xml en entrée")
	tree = etree.parse('../donnees_xml/OpenBeerMap.xml')
	root = tree.getroot()
	liste_noms = root.xpath("//name/text()")
	liste_osm = root.xpath("//osm_id/text()")
	dic_infos = recuperation_infos(liste_noms, liste_osm)
	impression_xml_pivot(dic_infos)

	# deuxième étape, utilisation des fichiers au format pivot pour la création du  fichier pivot final
	dic = {}
	dic = open_and_dic("../xml_formattes_pivot\cinemas-a-paris_pivot.xml",dic)
	dic.update(open_and_dic("../xml_formattes_pivot\Bibliotheque_modele.xml",dic))
	dic.update(open_and_dic("../xml_formattes_pivot\distributeurspreservatifsmasculinsparis2012_pivot.xml",dic))
	dic.update(open_and_dic("../xml_formattes_pivot\liste_des_marches_de_quartier_a_paris_pivot.xml",dic))
	dic.update(open_and_dic("../xml_formattes_pivot\liste-des-cafes-a-un-euro_pivot.xml",dic))
	dic.update(open_and_dic("../xml_formattes_pivot\openbeermap_pivot.xml",dic))
	dic.update(open_and_dic("../xml_formattes_pivot\\restauration_france_entiere_pivot.xml",dic))

	#pprint(dic)
	out_xml(dic)
