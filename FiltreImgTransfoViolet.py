#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from PIL import Image; #Importer depuis la librairie les fonction#
img=Image.open("C:\chien-noir-et-feu-adopter-52241.jpg"); #Ouvre l'image#
largeur=img.size[0]; #dimentions#
hauteur=img.size[1];
imgResultat = Image.new("RGB",(largeur,hauteur))#crée la nouvelle image#
for y in range ( hauteur ) : #Pour chaque ligne et colone (coordonnées du pixel)#
	for x in range ( largeur ) :
		p=img.getpixel(( x , y)) #code du pixel#
		if 0<=p[0]<=90 and 0<=p[1]<=90 and 0<=p[2]<=90  : p=(200 ,0 ,255) #si le pixel est sombre, le transforme en en violet#
		imgResultat.putpixel (( x , y) ,p) #insère le pixel dans la nouvelle image#
imgResultat .show()
