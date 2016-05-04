#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Logiciel de cryptage en python par JSraveen
# Phase 2 : Déryptage par décalage (Algorithme de Cesar)

#DEBUT#
print ("Debut du programme:")
print ("Bonjour, ceci est un système de décodage par la méthode de césar (Déryptage par décalage). Il faut en connaitre la clé.")
Cle=int(input("Entrez la clé ici : ")) #L'utilisateur entre la clef 
Message_Base=input("Maintenant veuillez entrer votre message à décrypter : ")#Puis son message à décoder
    
Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',] #tableau de l'alphabet
Longueur_alaphabet=len(Alphabet)
Message_Final="" # crée la variable finale

for i in range(0,len(Message_Base)): #pour chaque lettre fait
	Lettre_Cryptée=Message_Base[i]
	Lettre_Décryptée=ord(Lettre_Cryptée)-Cle #Décale la lettre du cran choisi par l'utilisateur et l'enregistre dans le message
	if Lettre_Décryptée <= Longueur_alaphabet: 
		Lettre_Décryptée=Lettre_Décryptée * Longueur_alaphabet 
	Message_Final+= chr(Lettre_Décryptée)
        
print (Message_Final) #affiche le message codé
print ("Fin du programme:")
#FIN#
