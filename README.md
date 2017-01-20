# GEOAPPLIDE

*guide de l'endroit optimal à Paris par parties localisées indexées et destiné aux étudiants*

Ce [projet](http://plancq.clement.free.fr/python/project/) a été réalisé dans le cadre de notre [M2 TAL](http://www.tal.univ-paris3.fr/plurital/) pour les cours de XML et de python réalisé par :

Chloé Monnin, Mathilde POULAIN, Léon-Paul SCHAUB

encadré par :

Johan FERGUTH et Clément PLANCQ

## Objectif :
Déterminer le meilleur quartier étudiant en fonction des données suivantes :
- les distributeurs de préservatifs
- les cinémas
- les marchés de quartiers
- les cafés à un euro
- les brasseries
- les bibliothèques
- les établissements universitaires
- les CROUS (restoU)
- les loyers par quartier par m²

Nous avons travaillé sur l'opendata. Nos données ont été récupérées principalement sur les sites [Paris OpenData](https://opendata.paris.fr/page/home/) et [Data.gouv](http://www.data.gouv.fr/fr/). Nos données sont donc uniquement opensource, réutilisables à volonté !

## Données
Description détaillée des données :
- [Distributeurs de préservatifs](https://opendata.paris.fr/explore/dataset/distributeurspreservatifsmasculinsparis2012/export/) :
  - source : opendata.paris.fr
  - format json et geojson
  - informations fournies dans le fichier : id, année d'installation, horaires pendant les vacances d'été, adresse, site, horaires pendant les vacances d'hiver, accès (intérieur/extérieur), latitude/longitude, adresse complète, arrondissement, horaires normales.
- [cafés à 1€](https://opendata.paris.fr/explore/dataset/liste-des-cafes-a-un-euro/export/)
  - source : opendata.paris.fr
  - format json et geojson
  - informations fournies dans le fichier : id, arrondissement, adresse, prix, géolocalisation, nom du café, prix en terrasse, date, prix au comptoir.
- [cinémas](https://opendata.paris.fr/explore/dataset/cinemas-a-paris/api/)
  - source : opendata.paris.fr
  - format json et geojson
  - informations fournies dans le fichier : id, nombre d'écrans, nombre de fauteuils, ndegauto, arrondissement, art et essai (NON/A), adresse, nom de l'établissement, coordonnées (lat, long).
- [marchés de quartiers](https://opendata.paris.fr/explore/dataset/liste_des_marches_de_quartier_a_paris/api/)
  - source : opendata.paris.fr
  - format json et geojson
  - informations fournies dans le fichier : id, marché, jour (horaires), arrondissement, adresse complète, localisation (détail adresse), société gestionnaire.
- bières,  [openbeermap](https://www.data.gouv.fr/fr/datasets/bars-pubs-et-brasseries-artisanales-dopen-beer-map-ile-de-france-mai-2015/)
  - source : data.gouv.fr/fr
  - informations fournies dans le fichier : nom de l'établissement, gml id, osm id, brewer (Oui/Non), bières (noms de bières), type (bar/pub).
  - format csv, séparateur = ","
- [bibliothèques](https://www.data.gouv.fr/fr/datasets/adresses-des-bibliotheques-publiques/)
  - source : data.gouv.fr/fr
  - format csv, séparateur = ","
  - informations fournies dans le fichier :id, numéro INSEE, ville, région, type de voie, voie, CPBIBLIO, nom de la voie, numéro de voie, département, population légale, libellé 1 (type de biliothèque, bibliothèque, médiathèque, communale, municipale), libellé 2 (nom de la bibliothèque).
- [quartiers administratifs](https://opendata.paris.fr/explore/dataset/quartier_paris/)
  - source : opendata.paris.fr
  - format json et geojson
  - informations fournies dans le fichier : id, et coordonnées des points du polygone qui définit le quartier (geom/type/coordinates/item/item/lat - long), numéro INSEE, nom du quartier, arrondissement.
- [établissements universitaires](https://www.data.gouv.fr/fr/datasets/annuaire-immobilier-de-l-enseignement-superieur-prs/)
  - source : data.gouv.fr/fr
  - format json
  - informations fournies dans le fichier :id, code postale, adresse, parcelle, surface, propriétaire, occupant, type, tutelle pédagogique, statut (public/privé), pres (?).
- [CROUS (France entière)](https://www.data.gouv.fr/fr/datasets/ensemble-des-lieux-de-restauration-des-crous-france-entiere-1/)
  - source : data.gouv.fr/fr
  - informations fournies dans le fichier : id, lat, long, nom, type (resto/cafeteria), contact (adresse complète).
- [LOYERS DE PARIS](https://www.data.gouv.fr/fr/datasets/encadrement-des-loyers-a-paris/)
  - source : data.gouv.fr/fr
  - informations fournies dans le fichier: zoneGL,quartier, n-pieces, prix moyen au m², prix mini, prix max

## Transformation de toutes les données en XML
Nous avons réalisé plusieurs scripts en python3 pour transformer toutes nos données en XML, ce sont les suivants, présents dans le dossier /scripts :
- openbeermap2xml.py (transormation du fichier CSV d'OpenBeerMap)
- json2xml.py (transformation des fichiers au format json vers du XML)
- csv2xml.py (transformation du fichier CSV adresse_bibliotheque)
- crous2xml (formattage du fichier CROUS)

Modules utilisés pour la réalisation des scripts :
- re (utilisation des expressions régulières)
- csv
- codecs
- xml.sax
- [dicttoxml](https://github.com/quandyfactory/dicttoxml) (génère un fichier xml à partir d'un dictionnaire python)
- [json](https://docs.python.org/3/library/json.html) (gestion des fichiers json et conversion en dictionnaire python)
- [lxml](https://pypi.python.org/pypi/lxml/3.3.3)
- [geopy](https://github.com/geopy/geopy)
- [osmapi](https://pypi.python.org/pypi/osmapi/)

### Problèmes rencontrés lors de la création des scripts
#### OpenBeerMap
Le fichier OpenBeerMap est construit de la façon suivante :

*OpenBeerMap_IDF.1126088147,1126088147,(1:Akerbeltz_ambrée),Non,L'Express,pub*

Voilà un exemple pour les brasseries qui proposent plusieurs types de bières :

*OpenBeerMap_IDF.1305927682,1305927682,"(9:Chouffe,Desperados,Guinness,Heineken,Hoegarden blanche,Leffe,...)",Non,Osmoz Café,pub*

Donc on ne peut pas spliter sur la virgule directement. On extraie donc ce qui est entre parenthèses, on le supprime de la ligne en le sauvegardant en mémoire pour pouvoir spliter la ligne sur la virgule et récupérer un tableau contenant toutes les informations pour les imprimer dans le fichier de sortie.

On obtient le fichier openbeermap.xml.

#### Scripts json2xml
Les fichiers json ont été très simples à passer en XML, python propose le module json qui traite un fichier json et créé un dictionnaire contenant toutes les données du fichier.

Ensuite un module dicttoxml permet dans l'autre sens, c'est à dire à partir d'un dictionnaire, de créer un fichier xml. C'est avec ce script que nous avons généré les fichiers suivants :

- facs.xml
- cinemas.xml
- preservatifs.xml
- quartiers.xml
- cafes.xml
- marches.xml

Après tentative de validation, les dtd montraient un problème dans la structure du xml: le module transformant en balise <item>
chaque liste du json d'origine. il y avait plusieurs balises <item>, dans différents noeuds...
  -> Résolution : il a fallu ne sélectionner que la clé qui nous intéressait dans le json pour supprimer l'erreur.
Récurrente sur tous les fichiers json d'origine

  Tous les XML ont à ce jour été validés par une DTD.

#### Récupération des adresses  partir des OSM_ID d'OpenBeerMap
Dans le fichier OpenBeerMap, on a les OSM_ID pour chaque bar, à partir de ces IDs, on utilise le module osmapi qui permet théoriquement d'obtenir la latitude, la longitude et l'adresse ocmplète (arrondissement, numéro et nom de la rue, ville, etc). Problème, l'adresse complète n'est récupérable que dans 34 (ou 38) cas sur les 119 entrées que compte le fichier. On utilise donc osmapi pour retrouver latitude et longitude puis un autre module (geopy) pour obtenir, à partir des coordonnées une adresse complète.
Ces étapes sont dans le script : openbeermap_pivot.py.

## Création d'un fichier XML pivot
On réalise ensuite un fichier XML pour croiser toutes les données et les mettre en correspondance. De plus, certaines de nos données concernent la France entière, nous travaillons sur Paris, il faut donc limiter les données à celles que nous allons utiliser.
D'abord on formate avec python tous les xml pour qu'ils ressemblent au modèle de xml que l'on veut, puis on les met en commun pour obtenir un seul xml.

### Ajout des loyers
  On passe par un fichier csv pour récupérer les loyers par quartier, malheureusement les quartiers étant identifiés par id et non par arrondissement, on doit passer par une comparaison avec les quartiers administratifs de Paris grâce à un tableau wikipédia. Ensuite, on établit la moyenne de loyer par arrondissement, par quartier, par taille d'appartement et par date de construction, pour obtenir un arrondi au mètre carré. Il est informé comme attribut de la balise 'arrondissement' dans le xml pivot.

### Fichier de stats
On a aussi créé un tableau excel (si on a le temps on fera un script qui le crée de A à Z mais ce n'est pas le plus urgent à ce jour) qui regroupe toutes les statistiques sur chaque arrondissement. Sa conception a été facilitée par la structure de données d'origine de python(dictionnaires) qui a permis d'extraire les chiffres intuitivement -> on trouve les moyennes de chaque type de lieu par arrondissement et en total, le max et le min de chacun, et deux matrices, une de covariance et une autre de corrélation qui nous sera utile à l'heure de formuler nos hypothèses.


## Réalisation d'un site pour le rendu final
Nous avons réalisé un site pour la présentation du projet, de nos données et une visualisation de nos données. Nous avons utilisé du jquery principalement et les librairies jquery suivantes :
- visualize.js pour les graphiques
- gmaps pour la carte
