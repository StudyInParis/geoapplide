from lxml import etree

# récupération des fichiers
cinemas = open('../donnees_XML/cinemas.xml')
preservatifs = open('../donnees_XML/preservatifs.xml')
facs = open('../donnees_XML/facs.xml')
cafes = open('../donnees_XML/liste_cafe.xml')
marches = open('../donnees_XML/liste_marches.xml')
quartiers = open('../donnees_XML/quartiers.xml')


megatab = {}
for element in megatab:
    tree = etree.parse("../donnees_XML/cinemas.xml")
    for name in tree.xpath("//nom_etablissement"):
        
