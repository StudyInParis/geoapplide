#! usr/bin/python3
#! coding: utf-8

from glob import glob
import subprocess as sub
import os

"""
prend en argument un dossier contenant des fichiers XML et un autre avec des DTD
ecrit un rapport de validation
"""

def validation(xmlfolder):
	if xmlfolder[-1] != "/": xmlfolder = xmlfolder+"/"
	# if dtdfolder[-1] != "/": dtdfolder = dtdfolder+"/"
	for xmlfile in glob(xmlfolder+"*.xml"):
		print(xmlfile)
		dtdfile=lireXML(xmlfile)
		if len(dtdfile) > 1:
			p = os.popen("xmllint --dtdvalid {dtdfile} --noout {xmlfile}".format(dtdfile=dtdfile, xmlfile=xmlfile))
			if len(p.readline()) < 1:
				print(xmlfile, "is valid.")
			
		print("*****************************")

def lireXML(xmlfile):
	with open(xmlfile,'r') as f:
		f.readline()
		dtdline=f.readline()
		# print(dtdline)
		if not dtdline.startswith("<!DOCTYPE"):
			print(xmlfile, "has no DTD declaration")
			return ""
		else:
			dtdfile=dtdline.strip().split('"')[1]
			if dtdfile.startswith("../../"): dtdfile=dtdfile[3:]
			return dtdfile

"""
p = sub.Popen(['your command', 'arg1', 'arg2', ...],stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()
print output"""

if __name__ == '__main__':
	for info in os.listdir("../XML/"):
		path="../XML/"+info
		if os.path.isdir(path):
			print(path)
			validation(path)
	# validation('../XML/fichiers_2xml_pivot')