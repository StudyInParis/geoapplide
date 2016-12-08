# geoapplide

*guide de l'endroit optimal à Paris par parties localisées indexées et destiné aux étudiants*

Projet M2 pour les cours de XML et de python réalisé par :
Chloé Monnin
Mathilde POULAIN
Léon-Paul SCHAUB

## Objectif :
Déterminer le meilleur quartier étudiant en fonction de :
- les distributeurs de préservatifs
- les cinémas
- les marchés de quartiers
- les cafés à un euro
- les brasseries
- les bibliothèques
- les établissements universitaires
- les CROUS (restoU)

Nous avons travaillé sur l'opendata. Nos données ont été récupérées principalement sur les sites https://opendata.paris.fr/page/home/ et http://www.data.gouv.fr/fr/.

## Données
Description détaillée des données :
- Distributeurs de préservatifs :
  - https://opendata.paris.fr/explore/dataset/distributeurspreservatifsmasculinsparis2012/export/
  - format json et geojson
  - informations fournies dans le fichier : id, année d'installation, horaires pendant les vacances d'été, adresse, site, horaires pendant les vacances d'hiver, accès (intérieur/extérieur), latitude/longitude, adresse complète, arrondissement, horaires normales.
- cafés à 1€
  - https://opendata.paris.fr/explore/dataset/liste-des-cafes-a-un-euro/export/
  - format json et geojson
  - informations fournies dans le fichier : id, arrondissement, adresse, prix, géolocalisation, nom du café, prix en terrasse, date, prix au comptoir.
- cinémas
  - https://opendata.paris.fr/explore/dataset/cinemas-a-paris/api/
  - format json et geojson
  - informations fournies dans le fichier : id, nombre d'écrans, nombre de fauteuils, ndegauto, arrondissement, art et essai (NON/A), adresse, nom de l'établissement, coordonnées (lat, long).
- marchés de quartiers
  - https://opendata.paris.fr/explore/dataset/liste_des_marches_de_quartier_a_paris/api/
  - format json et geojson
  - informations fournies dans le fichier : id, marché, jour (horaires), arrondissement, adresse complète, localisation (détail adresse), société gestionnaire.
- bières, openbeermap
  - https://www.data.gouv.fr/fr/datasets/bars-pubs-et-brasseries-artisanales-dopen-beer-map-ile-de-france-mai-2015/
  - informations fournies dans le fichier : nom de l'établissement, gml id, osm id, brewer (Oui/Non), bières (noms de bières), type (bar/pub).
  - format csv, séparateur = ","
- bibliothèques
  - https://www.data.gouv.fr/fr/datasets/adresses-des-bibliotheques-publiques/
  - format csv, séparateur = ","
  - informations fournies dans le fichier :id, numéro INSEE, ville, région, type de voie, voie, CPBIBLIO, nom de la voie, numéro de voie, département, population légale, libellé 1 (type de biliothèque, bibliothèque, médiathèque, communale, municipale), libellé 2 (nom de la bibliothèque).
- quartiers administratifs
  - https://opendata.paris.fr/explore/dataset/quartier_paris/
  - format json et geojson
  - informations fournies dans le fichier : id, et coordonnées des points du polygone qui définit le quartier (geom/type/coordinates/item/item/lat - long), numéro INSEE, nom du quartier, arrondissement.
- établissements universitaires
  - https://www.data.gouv.fr/fr/datasets/annuaire-immobilier-de-l-enseignement-superieur-prs/
  - format json
  - informations fournies dans le fichier :id, code postale, adresse, parcelle, surface, propriétaire, occupant, type, tutelle pédagogique, statut (public/privé), pres (?).
- CROUS (France entière)
  - https://www.data.gouv.fr/fr/datasets/ensemble-des-lieux-de-restauration-des-crous-france-entiere-1/
  - informations fournies dans le fichier : id, lat, long, nom, type (resto/cafeteria), contact (adresse complète).

## Transformation de toutes les données en XML
Nous avons réalisé plusieurs scripts en python3 pour transformer toutes nos données en XML, ce sont les suivants, présents dans le dossier /scripts :
- openbeermap2xml.py (transormation du fichier CSV d'OpenBeerMap)
- json2xml.py (transformation des fichiers au format json vers du XML)
- csv2xml.py (transformation du fichier CSV adresse_bibliotheque)
- format_xml (formattage du fichier CROUS)

### Problèmes rencontrés lors de la création des scripts
#### OpenBeerMap
Le fichier OpenBeerMap est construit de la façon suivante :\n
*OpenBeerMap_IDF.1126088147,1126088147,(1:Akerbeltz_ambrée),Non,L'Express,pub*\n
Voilà un exemple pour les brasseries qui proposent plusieurs types de bières :\n
*OpenBeerMap_IDF.1305927682,1305927682,"(9:Chouffe,Desperados,Guinness,Heineken,Hoegarden blanche,Leffe,...)",Non,Osmoz Café,pub*\n
Donc on ne peut pas spliter sur la virgule directement. On extraie donc ce qui est entre parenthèses, on le supprime de la ligne en le sauvegardant en mémoire pour pouvoir spliter la ligne sur la virgule et récupérer un tableau contanant toutes les informations pour les imprimer dans le fichier de sortie.

## Création d'un fichier XML pivot
