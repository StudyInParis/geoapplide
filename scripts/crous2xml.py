#!/usr/bin/python3
#! coding: utf-8

"""
script pour traitement du fichier XML des CROUS
"""

import xml.etree.ElementTree as ET

def clean_crous(filename):
	"""
	fonction qui créé un fichier de sortie au format XML
	entree : nom de fichier
	sortie : impression directement dans un fichier de sortie au format XML
	"""
	tree = ET.parse(filename)
	root = tree.getroot()
	for child in root:
		for contact in child.findall('contact'):
			data=contact
		newatt={}
		for att in child.attrib:
			if att in ['id', 'title', 'lat', 'lon', 'zone', 'type']:
				# print({att, child.attrib[att]})
				newatt.update({att: child.attrib[att]})
		child.clear()
		for att in newatt:
			child.set(att, newatt[att])
		child.append(data)
	tree.write('../donnees_xml/restauration_france_entiere.xml')

if __name__ == '__main__':
	clean_crous('../donnees_brutes/restauration_france_entiere.xml')
