from lxml import etree

# récupération des fichiers
cinemas = open('../donnees_xml/cinemas.xml')
preservatifs = open('../donnees_xml/preservatifs.xml')
facs = open('../donnees_xml/facs.xml')
cafes = open('../donnees_xml/liste_cafe.xml')
marches = open('../donnees_xml/liste_marches.xml')
quartiers = open('../donnees_xml/quartiers.xml')


megatab = {}
for element in megatab:
    tree = etree.parse("../donnees_xml/cinemas.xml")
    for name in tree.xpath("//nom_etablissement"):
