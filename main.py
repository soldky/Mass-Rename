#!/usr/bin/python3
import os

def fileParse(fileName):
	res = []
	with open(nameFile, 'r') as file:
	        line = next(file, None)
	        while line:
	        	res.append(line)
	        	line = next(file, None)
	return res

if __name__ == '__main__':
	print("------------------------------------------------")
	print("----------------- Renommage --------------------\n")
	fin=False

	while not fin:

		try:

			nameFolder = input("Nom du dossier qui contient les fichiers à renommer : ")
			nameFile = input("Nom du fichier qui contient les nouveaux noms : ")
			saison = input("Numéro de la saison : ")

			containFile = fileParse(nameFile)
			files = os.listdir(nameFolder)
			files.sort()

			if len(files) != len(containFile):
				print("Nombre de nom et de fichiers à renommer différent")
				fin=True
				break;

			print("\n------------------------------------------------")
			print("-------- Liste des fichiers présents -----------\n")
			for file in files:
				print("	- "+file)
			print("\n------------------------------------------------")

			tri=int(input("Voulez vous les renommer (1:Oui, 0:Non) : "))

			print("\n------------------------------------------------")

			if tri==1:
				for i in range(0,len(files)):
					if i<=9:
						num = "0"+str(i+1)
					else:
						num = str(i+1)

					pattern = nameFolder+"/"+saison+"x"+num+" - "

					os.rename(nameFolder+"/"+files[i],pattern+containFile[i])

				print("Renommage terminé")
				fin=True

			elif tri==0:
				print("Renommage annulé")
				fin=True

			else:
				print("Mauvaise saisi -- Fin du programme")
				fin=True

		except FileNotFoundError:
			print("\nFichier ou dossier introuvable")
			fin=True

	print("\n-------------------- Fin -----------------------")
	print("------------------------------------------------")