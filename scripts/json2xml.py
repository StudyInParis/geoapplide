#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import dicttoxml
import sys

"""
script qui transforme un fichier json en fichier XML
entree = fichier json
sortie = fichier XML

donner en argument
1 = nom du fichier json d'entrée
2 = nom du fichier xml de sortie
"""

input_file = sys.argv[1]
output = open(sys.argv[2], 'w')
# importation du fichier json dans un dictionnaire qui sera enuite rnasformé transformé en xml
with open(input_file, 'r') as f:
    json_file = json.load(f)
    xml_file = dicttoxml.dicttoxml(json_file)
    output.write(xml_file)


# Exemple des données du fichier json :
# [{"datasetid": "distributeurspreservatifsmasculinsparis2012",
# "recordid": "f72375c37bd4ed841d4b6e97e167fab402f2b1d6",
# "fields":
#     {"horaires_vacances_hiver": "9h \u00e0 22h30",
#     "horaires_vacances_ete": "8h \u00e0 22h",
#     "adresse": "3 Av Maurice D'Ocagne",
#     "site": "Centre sportif Jules No\u00ebl",
#     "annee_installation": "2008/2009",
#     "acces": "Int\u00e9rieur",
#     "xy": [48.824547, 2.314142],
#     "adresse_complete": "3 Av Maurice D'Ocagne 75014 Paris  France",
#     "arrond": 75014,
#     "horaires_normal": "8h \u00e0 22h30"},
# "geometry":
#     {"type": "Point",
#     "coordinates": [2.314142, 48.824547]},
#     "record_timestamp": "2016-08-27T18:20:10+02:00"}
