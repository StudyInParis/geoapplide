# geoapplide

*guide de l'endroit optimal à Paris par parties localisées indexées et destiné aux étudiants*

Projet M2 pour les cours de XML et de python réalisé par :
Chloé Monnin
Mathilde POULAIN
Léon-Paul SCHAUB

## Objectif :
Déterminer le meilleur quartier étudiant en fonction de :
- la présence de distributeurs de préservatifs
- les cinémas
- les marchés de quartiers
- les cafés à un euro
- les brasseries
- les bibliothèques
- les établissements universitaires
- les CROUS (restoU)

Nous avons travaillé sur l'opendata. Nos données ont été récupérées principalament sur le site https://opendata.paris.fr/page/home/ et http://www.data.gouv.fr/fr/.

## Données
Description détaillée des données :
- Distributeurs de préservatifs :
  - https://opendata.paris.fr/explore/dataset/distributeurspreservatifsmasculinsparis2012/export/
  - format json et geojson
  - informations fournises dans le fichier : id, année d'installation, horaires pendant les vacances d'été, adresse, site, horaires pendant les vacances d'hiver, accès (intérieur/extérieur), lattitude/longitude, adresse complète, arrondissement, horaires normales.
- cafés à 1€
  - https://opendata.paris.fr/explore/dataset/liste-des-cafes-a-un-euro/export/
  - format json et geojson
  - informations fournises dans le fichier : id, arrondissement, adresse, prix, géolocalisation, nom du café, prix en terrasse, date, prix au comptoir.
- cinémas
  - https://opendata.paris.fr/explore/dataset/cinemas-a-paris/api/
  - format json et geojson
- marchés de quartiers
  - https://opendata.paris.fr/explore/dataset/liste_des_marches_de_quartier_a_paris/api/
  - format json et geojson
- bières, openbeermap
  - https://www.data.gouv.fr/fr/datasets/bars-pubs-et-brasseries-artisanales-dopen-beer-map-ile-de-france-mai-2015/
  - format csv, séparateur = ","
- bibliothèques
  - https://www.data.gouv.fr/fr/datasets/adresses-des-bibliotheques-publiques/
  - format csv, séparateur = ","
- quartiers administratifs
  - https://opendata.paris.fr/explore/dataset/quartier_paris/
  - format json et geojson
- établissements universitaires
  - https://www.data.gouv.fr/fr/datasets/annuaire-immobilier-de-l-enseignement-superieur-prs/
  - format json
- CROUS (France entière)
  - https://www.data.gouv.fr/fr/datasets/ensemble-des-lieux-de-restauration-des-crous-france-entiere-1/
