api = osmapi.OsmApi()
print(api.NodeGet(1307259134))
# Resultat :
# {'version': 4,
# 'visible': True,
# 'tag': {'addr:city': 'Paris',
#     'note': 'Pub breton, crêperie. Musique à la cave jeudi, vendredi ...',
#     'addr:postcode': '75014',
#     'addr:housenumber': '30',
#     'addr:street': 'Rue Delambre',
#     'cuisine': 'french',
#     'amenity': 'pub',
#     'name': 'Ty jos',
#     'brewery': 'Leffe;Leffe Ruby'},
# 'uid': 587649,
# 'lon': 2.3258678,
# 'changeset': 17681527,
# 'lat': 48.8414796,
# 'timestamp': datetime.datetime(2013, 9, 5, 5, 28, 24),
# 'user': 'Emmanuel Delahaye',
# 'id': 1140477414}
