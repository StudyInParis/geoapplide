#!/usr/bin/python3
#! coding: utf-8


# def extraction(url) :
#
import urllib.request
import ssl

def export(url):
	#url = 'https://opendata.paris.fr/explore/dataset/liste-des-cafes-a-un-euro/download/?format=json&timezone=Europe/Berlin'
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	response = urllib.request.urlopen(url,context=ctx)
	data = response.read()      # a `bytes` object
	text = data.decode('utf-8')
	return text
def choose(url):
	if "opendata" in url:
		filename = url.split("dataset/")[1].split("/download")[0]
		if "json" in url:
			filename +=".json"
		elif "csv" in url:
			filename += '.csv'
	elif "Beer" in url:
		filename = "OpenBeerMap_IDF.csv"
	else:
		filename = url.split("/")[-1]
	return filename
def ecrire(url):
	fic = choose(url)
	fichier=open("../donnees_brutes/"+fic,'w')
	fichier.write(export(url))
	fichier.close()
	return fic

if __name__=='__main__':
	print(ecrire('https://opendata.paris.fr/explore/dataset/liste-des-cafes-a-un-euro/download/?format=json&timezone=Europe/Berlin'))
	#print(write('https://opendata.paris.fr/explore/dataset/equipements_de_proximite/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true'))
	print(ecrire('https://www.data.gouv.fr/s/resources/ensemble-des-lieux-de-restauration-des-crous-france-entiere-1/20160116-000310/crous_restauration_france_entiere.xml'))
