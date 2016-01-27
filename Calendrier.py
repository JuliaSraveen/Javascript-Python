#Consigne : Ecrivez un script capable d'afficher la liste de tous les jours d'une année qui commence un lundi. #
#Votre script utilisera lui-même trois listes : une des jours, une des mois et une des nombres.#

print ("Voila le calendrier de l'année : ") #affiche le message#
nomjour=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]#tableau 1 : nom des jours#
nommois=["janvier","février","mars","avril","mai","juin","juillet","aout","septembre","novembre","décembre"]#tableau 2 : nom des mois#
finmois=[31,28,30,31,30,31,31,30,31,30,31]#tableau 3 : nombre de jours dans un mois#
numerojour=1
indicedunomdujour=0
for mois in nommois:
	while numerojour<=finmois:
		print (nomjour[indicedunomdujour])
		print (numerojour)
		print (mois)
		numerojour=numerojour+1
		if indicedunomdujour>6 :
		    indicedunomdujour=0
		if indicedunomdujour<=6 :
		    indicedunomdujour=indicedunomdujour+1
	finmois=finmois+1
