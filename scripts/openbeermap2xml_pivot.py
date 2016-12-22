#! usr/bin/python3
#! coding: utf-8

from lxml import etree
import osmapi
#pip install module python pour acces api open street map

# parser le fichier  xml en entrée
tree = etree.parse('../donnees_xml/OpenBeerMap.xml')
root = tree.getroot()
osm_list = {}
# récupérer l'ensemble des osm_id avec le nom du bar correspondant
dico = {}
cpt = 0
for child in root:
    for element in list(child):
        try:
            if element.tag == "osm_id":
                osm = element.text
                api = osmapi.OsmApi()
                lat = api.NodeGet(osm)['lat']
                lon = api.NodeGet(osm)['lon']
            if element.tag == "name":
                nom_bar = element.text
            dico[nom_bar] = {}
            dico[nom_bar]['lat'] = lat
            dico[nom_bar]['lon'] = lon
            cpt +=1
        except TypeError:
            tb = sys.exc_info()[2]
            raise print("Erreur pour Le Chablis !")
            next

# api = osmapi.OsmApi()
# print(api.NodeGet(1140477414)) #un des elements de openbeermap



# format de sortie attendu
# <root>
# 	<arrondissement num ="10" loyer_m_carre ="20.34">
# 		<elem id="75010_1" type="bar">
# 			<long> 4,6541468 </long>
# 			<lat> 45,456786 </lat>
# 			<adresse> 15, rue du foot</adresse>
# 			<nom>A la balle de match</nom>
# 		</elem>
# 	</arrondissement>
# </root>
