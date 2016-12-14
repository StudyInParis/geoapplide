#!/usr/bin/env python
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
				dictionnaire[i]=row["fields"]
	return dictionnaire




def main():
	input_file = sys.argv[1]
	output = open(sys.argv[2], 'w')
	# importation du fichier json dans un dictionnaire
	with open(input_file, 'r') as f:
		json_file = json.load(f)
		# transformation du dictionnaire en fichier XML
		# + extraction des infos necessaires(mm fichier - les infos superflues)
		xml_file = dicttoxml.dicttoxml(json_file)
		# impression dans le fichier de sortie
		output.write(xml_file)

if __name__ == '__main__':
	main()
