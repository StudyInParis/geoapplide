#! usr/bin/python3
#! coding: utf-8

import csv, os
from csv2xml import prepare

def get_data(infilename, pattern):
	"""
	entree : nom de fichier, motif
	sortie : impression directement dans un fichier de sortie
	"""
	liste = []
	with open(infilename) as csvfile:
		# reader = csv.reader(csvfile, delimiter=";")
		reader = csv.DictReader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
		for row in reader:
			# print(row)
			for data in row:
				# print(data)
				if row[data] == pattern:
					liste+=[row]
	xmlfile=open("../donnees_xml/"+arrange_data(pattern)+".xml", 'w')
	xmlfile.write("""<?xml version="1.0" encoding="UTF-8" ?>\n<root>\n""")
	i=1
	for elem in liste:
		xmlfile.write("""\t<element id="{}">\n""".format(str(i)))
		for data in elem:
			content=prepare(elem[data])
			xmlfile.write("\t\t<"+arrange_data(data)+">"+content+"</"+arrange_data(data)+">\n")
		xmlfile.write("\t</element>\n")
		i+=i
	xmlfile.write("""</root>""")

def arrange_data(string):
	"""
	fonctin pour nettoyage, élimine les accents
	entree : string
	sortie : string
	"""
	equivalents={
	"é":"e",
	"è":"e",
	"à":"a",
	"â":"a",
	"ù": "u",
	"î":"i",
	"ô":"o",
	"û":"u",
	" ":"_",
	"'":"_"
	}
	for char in string:
		if char in equivalents:
			# print(char)
			string=string.replace(char, equivalents[char])
	return string


if __name__ == '__main__':
	get_data("../donnees_brutes/equipements_de_proximite.csv", "Bibliothèque")