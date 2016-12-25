#! usr/bin/python3
#! coding: utf-8

import osmapi
#pip install module python pour acces api open street map

api = osmapi.OsmApi()
print(api.NodeGet(1140477414)) # un des elements de openbeermap
#resultats :
# {'changeset': 17681527,
#  'id': 1140477414,
#  'lat': 48.8414796,
#  'lon': 2.3258678,
#  'tag': {'addr:city': 'Paris',
#          'addr:housenumber': '30',
#          'addr:postcode': '75014', <========= ARRONDISSEMENT BITCHES !!
#          'addr:street': 'Rue Delambre',
#          'amenity': 'pub',
#          'brewery': 'Leffe;Leffe Ruby',
#          'cuisine': 'french',
#          'name': 'Ty jos',
#          'note': 'Pub breton, crêperie. Musique à la cave jeudi, vendredi ...'},
#  'timestamp': datetime.datetime(2013, 9, 5, 5, 28, 24),
#  'uid': 587649,
#  'user': 'Emmanuel Delahaye',
#  'version': 4,
#  'visible': True}
