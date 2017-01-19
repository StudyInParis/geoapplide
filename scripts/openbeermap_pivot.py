#! usr/bin/python3
#! coding: utf-8

import xml.etree.ElementTree as ET
import osmapi # pip install module python pour acces api open street map
from geopy.geocoders import Nominatim
from pprint import pprint


"""
script pour transformer le fichier OpenBeerMap.xml au format pour le fichier xml_pivot
"""

def recuperation_infos(liste_noms, liste_osm):
    """ recupere infos sur bars openbeermap, latitude et longitude à partir de coordonnees OSM avec OsmApi

    entree = liste des noms des elements et liste des coordonnees correspondantes
    sortie = dictionnaire de correspondance {noms:[latitude, longitude, adresse]}
    """
    cpt = 0
    dico = {}
    for element in liste_osm:
        try:
            api = osmapi.OsmApi()
            coord = api.NodeGet(element) #un des elements de openbeermap
            lat = coord["lat"]
            lon = coord["lon"]
            address = GetAddress(lat, lon)
            # on récupère l'arrondissement puisque c'est notre base de tri, il est donné en avant-dernièr position dans le résultat de geopy
            arrondissement = address.split(', ')[-2]
            # petit nettoyage au milieu pour que ça soit jouli
            adr = ", ".join(address.split(', ')[1:-4])
            # ensuite on rassemble les bars/pubs par arrondissement dans le dictionnaire
            if arrondissement in dico.keys():
                dico[arrondissement].append([liste_noms[cpt], lat, lon, adr])
            else:
                dico[arrondissement] = []
            cpt+=1
        except TypeError:
            # dans certains cas, NodeGet renvoie un objet NonType donc inutilisable
            print("Erreur NonType node pour", liste_noms[cpt])
            dico[liste_noms[cpt]] = []
            next
    return dico

def GetAddress(latitude, longitude):
    """ récupère une adresse à partir de coordonnées
    entrée : une latitude, une longitude
    sortie : une string contenant l'adresse complète
    """
    geolocator = Nominatim()
    coordinates = str(latitude) + ', ' + str(longitude)
    location = geolocator.reverse(coordinates)
    return location.address

def impression_xml_pivot(dico):
    """impression d'un dictionnaire dans un fichier xml
    entree = dictionnaire
    sortie = void
    """
    output = open("../xml_formattes_pivot/openbeermap_pivot.xml", 'w')
    output.write('<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<root>\n')
    for element in sorted(dico):
        if element.startswith("750"):
            output.write('\t<arrondissement num ="'+element+'">\n')
            cpt=0
            for item in dico[element]:
                output.write('\t\t<element id="'+str(cpt)+'" type="bar">\n')
                output.write('\t\t\t<latitude>'+str(item[1])+'</latitude>\n')
                output.write('\t\t\t<longitude>'+str(item[2])+'</longitude>\n')
                output.write('\t\t\t<adresse>'+str(item[3])+'</adresse>\n')
                output.write('\t\t\t<nom>'+item[0]+'</nom>\n')
                output.write('\t\t</element>\n')
                cpt+=1
            output.write('\t</arrondissement>\n')
    output.write('</root>')

if __name__ == "__main__":
    print("parser le fichier xml en entrée")
    tree = ET.parse('../donnees_xml/OpenBeerMap.xml')
    root = tree.getroot()
    print("récupérer l'ensemble des osm_id avec le name du bar correspondant dans 2 listes")
    liste_noms = []
    for nom in root.findall('item'):
        liste_noms.append(nom.find('name').text)
    liste_osm = []
    for osm in root.findall('item'):
        liste_osm.append(nom.find('osm_id').text)
    print('création du dictionnaire qui contient nom, latitude, longitude et adresse pour chaque bar')
    dic_infos = recuperation_infos(liste_noms, liste_osm)
    print("Impression du fichier de sortie")
    impression_xml_pivot(dic_infos)
