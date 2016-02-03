#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from PIL import Image; 
img=Image.open("C:\mozilla_firefox.png"); #On ouvre l'image#
print (img.size, img.format, img.mode)#On affiche ses données (car en rgba#
pixel=img.load();#on charge l'image dans la variable pixel#
largeur=img.size[0];#On définit les tailles#
hauteur=img.size[1];
for i in range(largeur):#double boucle largeur/hauteur#
	for j in range(hauteur):
		rouge,vert,bleu,a=pixel[i,j];
		pixel[i,j]=(0,0,bleu);#On modifie les couleurs en affichant que des tons bleus#
img.show();#Affiche l'image#
