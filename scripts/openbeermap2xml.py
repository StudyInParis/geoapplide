import re

csv_file = open('../donnees_brutes/OpenBeerMap_IDF.csv','r')
xml_output = open('../donnees_XML/OpenBeerMap.xml','w')

def line_mod(line):
	"""
	entree : string line = une ligne
	sortie : tableau : {balise:contenu_balise}
	"""
	lines = {}
	# nettoyage de la ligne
	line = re.sub('(\(.*\))','',line)
	line = re.sub('&','&amp;',line)
	# split de la ligne
	items = line.split(',')
	lines["gml_id"] = items[0].split(".")[-1]
	lines["osm_id"] = items[1]
	lines["brewer"] = items[3]
	lines["name"] = items[4]
	lines["type_name"] = items[5].strip("\n")
	return lines

def beer_mod(beer):
	"""
	nettoyage d'une ligne
	entree : string beer
	sortie : string beer
	"""
	beer = re.sub('\(','', beer)
	beer = re.sub('[0-9]','', beer)
	beer = re.sub(':','', beer)
	beer = re.sub('\)','', beer)
	return beer

def tablification(tab1, tab2,i):
	"""
	ajoute les donnees d'un tableau a un autre tableau
	entree : 2 tableaux
	sortie : 1 tableau avec tab2 a la suite de tab1
	"""
	megatab = {}
	for element in tab1:
		megatab[element] = tab1[element]
	return megatab


if __name__ == '__main__':
	cpt_line = 1
	balises = {}
	final_tab = {}
	with csv_file as c:
		for line in c.readlines():
			# recuperation des bieres
			out_beers = {}
			pattern1 = re.search('\(.*\)',line)
			if pattern1:
				beer = pattern1.group()
				pattern2 = re.search('\,', beer)
				if pattern2:
					beers = beer.split(',')
					out_list = []
					for element in beers:
						element = beer_mod(element)
						out_list.append(element)
					out_beers["beer"] = out_list
				else:
					beer = beer_mod(beer)
					out_beers["beer"] = beer
				lines = line_mod(line)
				lines["beer"] = out_beers
				final_tab[cpt_line] = lines
				cpt_line += 1


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
