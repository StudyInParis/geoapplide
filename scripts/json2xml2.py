#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import dicttoxml
import sys

"""
script qui transforme un fichier json en fichier XML
entree = fichier json
sortie = fichier XML

donner en argument
1 = nom du fichier json d'entrée
2 = nom du fichier xml de sortie
"""

def get_values(json_dict):
	i=1
	dictionnaire={}
	for row in json_dict:
		for cle in row:
			# print(cle)
			if cle == "fields":
				dictionnaire[str(i)]=row["fields"]
		i+=1
	return dictionnaire




def main(input_file, outfile):
	output = open(outfile, 'w')
	# importation du fichier json dans un dictionnaire
	with open(input_file, 'r') as f:
		json_file = json.load(f)
		# transformation du dictionnaire en fichier XML
		# + extraction des infos necessaires(mm fichier - les infos superflues)
		xml_file = dicttoxml.dicttoxml(get_values(json_file), attr_type=False, ids=True)
		# impression dans le fichier de sortie
		output.write(xml_file)

if __name__ == '__main__':
	liste=["annuaire_immobilier_de_l_enseignement_superieur","liste-des-cafes-a-un-euro","quartier_paris"]
	for fichier in liste:
		infile="../donnees_brutes/"+fichier+".json"
		outfile="../donnees_xml/"+fichier+".xml"
		main(infile, outfile)
