#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
from pylab import *;
x = array ([0,1,2,3,4,5,6,7,8,9,10]); #tableau d'une liste, coordonnées de x et y#
y = array ([0,3,6,9,12,15,18,21,24,27,30]);
plot(x,y); 
show() #affiche courbe#





#Ou avec trinket#
#https://trinket.io/python/
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9,10])
y = np.array([0,3,6,9,12,15,18,21,24,27,30])
plt.plot(x, y)

plt.show() # affiche la figure a l'ecran
