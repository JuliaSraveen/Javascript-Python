#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Logiciel de cryptage en python par JSraveen
# Phase 1 : Cryptage par décalage (Algorithme de Cesar)

#DEBUT#
print ("Debut du programme:")
print ("Bonjour, ceci est un système d'encodage par la méthode de césar (Cryptage par décalage).")
Cle=int(input("Entrez la clé souaitée : ")) #L'utilisateur entre la clef 
Message_Base=input("Maintenant veuillez entrer votre message à crypter : ")#Puis son message à encoder

def prepare(Message_Base):
    liste1=["âà","éèêë","îï","ô","ûü","ç"]#Liste les caratères spéciaux
    liste2=["A","E","I","O","U","C"]
    i=0
    for mot in liste1:# Remplacement des caractères accentués éventuels en mots (comme "à")
       repl=liste2[i]
       for lettre in mot:# Remplacement des caractères accentués éventuels dans un mot
           Message_Base=Message_Base.replace(lettre,repl)
       i+=1      
    for lettre in "',-;:!?. ":  # Suppression de la ponctuation
        Message_Base=Message_Base.replace(lettre,"")
    Message_Base=Message_Base.upper()    # Passage en majuscules
    return Message_Base
    
A_Crypter=prepare(Message_Base) #le message est maintenant sans caractères spéciaux
Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',] #tableau de l'alphabet
Longueur_alaphabet=len(Alphabet)
Message_Final="" # crée la variable finale
 
for i in range(0,len(A_Crypter)): #pour chaque lettre fait
	Lettre_A_Crypter=A_Crypter[i]
	Lettre_Cryptee=ord(Lettre_A_Crypter)+Cle #Décale la lettre du cran choisi par l'utilisateur et l'enregistre dans le message
	if Lettre_Cryptee <= Longueur_alaphabet: #Si la lettre cryptée dépasse l'alphabet
		Lettre_Cryptee=Lettre_Cryptee % Longueur_alaphabet #La lettre cryptée
	Message_Final+= chr(Lettre_Cryptee)
        
print (Message_Final) #affiche le message codé
print ("Fin du programme:")
#FIN#
