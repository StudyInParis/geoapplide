#! usr/bin/python3
#! coding: utf-8

from lxml import etree
import osmapi #pip install module python pour acces api open street map

def recuperation_infos(liste_nom, liste_osm):
    """ recupere infos sur bars openbeermap, latitude et longitude à partir de coordonnees OSM avec OsmApi

    entree = liste des noms des elements et liste des coordonnees correspondantes
    sortie = dictionnaire de correspondance noms et latitude/longitude
    """
    cpt = 0
    dico = {}
    for element in liste_osm:
        try:
            api = osmapi.OsmApi()
            coord = api.NodeGet(element) #un des elements de openbeermap
            lat = coord["lat"]
            lon = coord["lon"]
            dico[liste_nom[cpt]] = [lat, lon]
            cpt+=1
        except KeyError:
            print("Erreur (postcode) non renseigné", liste_nom[cpt])
            dico[liste_nom[cpt]] = []
            next
        except TypeError:
            print("NonType node Error pour ", liste_nom[cpt])
            dico[liste_nom[cpt]] = []
            next
    return dico

def impression_xml_pivot(dico):
    """impression d'un dictionnaire dans un fichier xml
    entree = dictionnaire
    sortie = void
    """
    output = open("../xml_formattes_pivot/openbeermap_pivot.xml", 'w')
    output.write('<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<!DOCTYPE root SYSTEM "xml_pivot.dtd">\n<root>\n')
    cpt=0
    for element in dico:
        output.write('\t<elem id="'+str(cpt)+'" type="bar">\n')
        output.write('\t\t<long>'+str(dico[element][1])+'</long>\n')
        output.write('\t\t<lat>'+str(dico[element][0])+'</lat>\n')
        output.write('\t\t<name>'+element+'</name>\n')
        output.write('\t</elem>\n')
        cpt+=1
    output.write('</root>')
    # <elem id="75010_1" type="bar">
    # 			<long> 4,6541468 </long>
    # 			<lat> 45,456786 </lat>
    # 			<adresse> 15, rue du foot</adresse>
    # 			<name>A la balle de match</name>
    # 		</elem>

if __name__ == "__main__":
    # parser le fichier xml en entrée
    tree = etree.parse('../donnees_xml/OpenBeerMap.xml')
    root = tree.getroot()
    osm_list = {}
    # récupérer l'ensemble des osm_id avec le name du bar correspondant
    liste_nom = root.xpath("//name/text()")
    liste_osm = root.xpath("//osm_id/text()")
    noms_lat_lon = recuperation_infos(liste_nom, liste_osm)
    for item in noms_lat_lon:
        print(item, noms_lat_lon[item])
    impression_xml_pivot(noms_lat_lon)

# api = osmapi.OsmApi()
# print(api.NodeGet(1140477414)) #un des elements de openbeermap



# format de sortie attendu
# <root>
# 	<arrondissement num ="10" loyer_m_carre ="20.34">
# 		<elem id="75010_1" type="bar">
# 			<long> 4,6541468 </long>
# 			<lat> 45,456786 </lat>
# 			<adresse> 15, rue du foot</adresse>
# 			<name>A la balle de match</name>
# 		</elem>
# 	</arrondissement>
# </root>
