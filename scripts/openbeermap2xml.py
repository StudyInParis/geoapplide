import re

csv_file = open('../donnees_brutes/OpenBeerMap_IDF.csv','r')
xml_output = open('../donnees_XML/OpenBeerMap.xml','w')

def line_mod(line):
	"""
	fonction de nettoyage des lignes (suppression fins de ligne, et caractères spéciaux) et construit un dictionnaire à partir des éléments de la ligne.
	entree : string line = une ligne
	sortie : tableau : {balise:contenu_balise}
	"""
	lines = {}
	# nettoyage de la ligne en enelevant ce qui est entre parenthèse (donc les bières qui sont traitées à part)
	line = re.sub('(\(.*\))','',line)
	line = re.sub('&','&amp;',line)
	# split de la ligne
	items = line.split(',')
	# construction du tableau de sortie
	lines["gml_id"] = items[0].split(".")[-1]
	lines["osm_id"] = items[1]
	lines["brewer"] = items[3]
	lines["name"] = items[4]
	lines["type_name"] = items[5].strip("\n")
	return lines

def beer_mod(beer):
	"""
	nettoyage des noms de bières (suppression des :,(,),[0-9])
	entree : string beer
	sortie : string beer
	"""
	beer = re.sub('\(','', beer)
	beer = re.sub('[0-9]','', beer)
	beer = re.sub(':','', beer)
	beer = re.sub('\)','', beer)
	return beer

if __name__ == '__main__':
	cpt_line = 1
	balises = {}
	final_tab = {}
	with csv_file as c:
		for line in c.readlines():
			# recuperation des bieres
			out_beers = {}
			# recherche des éléments entre parenthèse
			pattern1 = re.search('\(.*\)',line)
			if pattern1:
				beer = pattern1.group()
				# récupération du contenu des parenthèses
				pattern2 = re.search('\,', beer)
				if pattern2:
					# si il trouve des virgules, donc on a une liste des bières donc création d'une liste
					beers = beer.split(',')
					out_list = []
					for element in beers:
						# nettoyage
						element = beer_mod(element)
						out_list.append(element)
					# ajout dans le tableau
					out_beers["beer"] = out_list
				else:
					# si pas de virgules, alors il n'y a qu'une seule bière, nettoyage
					beer = beer_mod(beer)
					# ajout dans le tableau
					out_beers["beer"] = beer
				# nettoyage de la ligne et récupération des infos dans un tableau
				lines = line_mod(line)
				# on ajoute les infos sur les bières
				lines["beer"] = out_beers
				final_tab[cpt_line] = lines
				cpt_line += 1

	# Impression du résultat dans le fichier de sortie
	xml_output.write('<?xml version="1.0" standalone="yes"?>\n<document id="open beer map">\n')
	for element in final_tab:
		xml_output.write('<item id="'+str(element)+'">\n')
		for item in final_tab[element]:
			if item == "beer":
				xml_output.write("\t<beers>\n")
				for beer_name in final_tab[element]["beer"]:
					# si l'objet est une string, on l'imprime simplement
					if type(final_tab[element]["beer"]["beer"]) == type('a'):
						xml_output.write("\t\t\t<beer>"+final_tab[element]["beer"]["beer"]+"</beer>\n")
					# sinon on parcourt le dictionnaire pour avoir toutes les valeurs de beer
					else:
						for bn in final_tab[element]["beer"]["beer"]:
							xml_output.write("\t\t\t<beer>"+bn+"</beer>\n")
					xml_output.write("\t</beers>\n")
			else:
				xml_output.write("\t<"+item+">"+final_tab[element][item]+"</"+item+">\n")
		xml_output.write('</item>\n')
	xml_output.write('</document>')
