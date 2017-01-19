# conding: utf-8
import math
from pprint import pprint

def create_dic(fichier):
	"""
	fonction pour le fichier des loyers
	entree : nom de fichier
	sortie : dictionnaire contenant les informations du fichier
	"""
	fic = open(fichier,"r")
	useless_ligne = fic.readline()
	lignes = fic.readlines()
	dic = {}
	dic2 = {}
	for ligne in lignes:
		ligne = ligne.rstrip()
		tab_ligne = ligne.split(",")
		if int(tab_ligne[0]) < 10:
			(tab_ligne[0]) = "7500"+(tab_ligne[0])
		else:
			(tab_ligne[0]) = "750"+(tab_ligne[0])
		if tab_ligne[0] not in dic:
			dic[tab_ligne[0]] = float(tab_ligne[7])
			dic2[tab_ligne[0]] = 1
		else :
			dic[tab_ligne[0]] += float(tab_ligne[7])
			dic2[tab_ligne[0]] += 1
	for cle in sorted(dic):
		dic[cle] = int(dic[cle]/dic2[cle])
	return dic
