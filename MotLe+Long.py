#Consigne : Ecrivez un script qui recherche le mot le plus long dans une phrase donnée par l'utilisateur#

print ("Debut du programme:")
P= input("Entrez votre phrase : ") #L'utilisateur entre sa phrase#
tableau=P.split()#Sépare la phrase dans un tableau /!\ on découpe avec un espace pas avec une virgule /!\#
i=0 #on met à 0 deux variables#
k=0
for a in tableau: #Il éxécute le bloc pour chaque valeur du tableau#
	i= len(a)#on appelle i la variable calculant la longueur de chaque mot#
	if i > k:#Si la longueur du mot est supérieure à la longueur précédente, on concerve cette longueur et le mot en question#
	  k=i
	  V=a
print ("Le mot le plus long est:")
print (V)#On affiche le mot le plus long et sa valeur#
print ("de")
print (k)
print ("caractères.")
print ("Fin du programme.")
