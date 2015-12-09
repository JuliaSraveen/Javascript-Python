a= input("a = ") #entrer la borne minime#
k=int(a)
b= input("b = ")#entrer la borne max#
z=int(b)
valeur=0 #la somme finale#
for x in range (k,z): #pour x entre les bornes#
  if x%5==0 : #si le reste est égal à 0 alors#
	  valeur=valeur+x #la somme prend la valeur#
print (valeur) #affiche la valeur finale#
