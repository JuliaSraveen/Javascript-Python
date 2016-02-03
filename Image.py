#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from PIL import Image; 
img=Image.open("C:\mozilla_firefox.png");
print (img.size, img.format, img.mode)
pixel=img.load();
largeur=img.size[0];
hauteur=img.size[1];
for i in range(largeur):
	for j in range(hauteur):
		rouge,vert,bleu,a=pixel[i,j];
		pixel[i,j]=(0,0,bleu);
img.show();
