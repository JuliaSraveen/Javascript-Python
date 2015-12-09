a= input("a (en mètres) = ") #entrer la borne minime#
k=int(a)
b= input("b (en mètres) = ")#entrer la borne max#
z=int(b)
valeur=0 #la valeur#
for x in range (k,z): #pour x entre les bornes#
	if x%2==0 :
	  F=(6.67*10**-11)*((10000*10000)/(x**2))
	  print (F)
