# geoapplide

*guide de l'endroit optimal à Paris par parties localisées indexées et destiné aux étudiants*

Projet M2 pour les cours de XML et de python réalisé par :
Chloé Monnin
Mathilde POULAIN
Léon-Paul SCHAUB

## Objectif :
Déterminer le meilleur quartier étudiant en fonction de
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
- cafés à 1€ : json, geojson
  - https://opendata.paris.fr/explore/dataset/liste-des-cafes-a-un-euro/export/
- cinémas : json, geojson
  - https://opendata.paris.fr/explore/dataset/cinemas-a-paris/api/
- marchés de quartiers : json, geojson
  - https://opendata.paris.fr/explore/dataset/liste_des_marches_de_quartier_a_paris/api/
- bières, openbeermap : csv
  - https://www.data.gouv.fr/fr/datasets/bars-pubs-et-brasseries-artisanales-dopen-beer-map-ile-de-france-mai-2015/
- bibliothèques : csv
  - https://www.data.gouv.fr/fr/datasets/adresses-des-bibliotheques-publiques/
- quartiers administratifs : json, geojson
  - https://opendata.paris.fr/explore/dataset/quartier_paris/
- établissements universitaires : json
  - https://www.data.gouv.fr/fr/datasets/annuaire-immobilier-de-l-enseignement-superieur-prs/
- CROUS (France entière) : XML
  - https://www.data.gouv.fr/fr/datasets/ensemble-des-lieux-de-restauration-des-crous-france-entiere-1/
