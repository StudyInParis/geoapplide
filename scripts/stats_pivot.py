#!/usr/bin/python
# coding: utf-8

from pprint import pprint

"""
script pour réalisation de statistiques sur le fichier XML pivot
comptage du nobmre d'équipements par arrondissement, etc.
réalisation d'un fichier xls de statistiques pour réalisation de graphiques pour intégration dans le site
"""

def open_and_dic(fichier,dic):
	fic = open(fichier,'r')
	lines = fic.readlines()
	num_l=0
	for line in lines:
		num_l +=1
		#print(num_l)
		if "<arron" in line:
			arr = line.split('"')[1]
			for ligne in lines[num_l:]:
				if "</arr" in ligne:
					break
				if arr not in dic:
					dic[arr] = []
				dic[arr] += [ligne]
	return dic

def compter(dic):
	dic = open_and_dic("../xml_formattes_pivot/xml_pivot.xml",{})
	dico2 = {}
	for cle in dic:
		cle = cle.rstrip()
		nbr_total = 0
		dico2[cle] = {}
		for line in dic[cle]:
			if "<elem" in line:
				nbr_total +=1
			if "type" in line:
				if line.split('"')[3] not in dico2[cle]:
					dico2[cle][line.split('"')[3]] = 1
				else: dico2[cle][line.split('"')[3]] += 1
			dico2[cle]["total_lieux"] = nbr_total
	return dico2

def csv_like(xls_out,dic2):
	out = open(xls_out,'w')
	dic2 = compter({})
	for cle in dic2:
		out.write(cle+"\t")
		out.write("\n")
		for clef in dic2[cle]:
			out.write("\n"+clef+"\t"+str(dic2[cle][clef]))
		out.write("\n")

if __name__=='__main__':
	csv_like("../xml_formattes_pivot/stats_pivot.xls",{})
