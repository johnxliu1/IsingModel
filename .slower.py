#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
from random import choice, random, randint
from pylab import imshow, figure, grid, show, savefig
#CTES
#k=1.38e-23;
k=1
T=1;
J=1;

def buildsystem(m): #optimizar
  system=np.empty([m,m])
  for i in range(m):
    for j in range (m):
      system[i,j]=choice([1,-1])
  return system


#def flips(E):
#  P=np.exp(-E/(k*T))
#  x=random()
#  return P>x

def energyvar(spin, neighbors):
  E=2*J*spin*sum(neighbors)
  return E

def bc(i):
    if i+1 > SIZE-1:
        return 0
    if i-1 < 0:
        return SIZE-1
    else:
        return i

def getneighbors(system,i,j): #simplificar con cuatro llamadas boundarycond
  m=len(system)-1
  up=i-1; down=i+1; left=j-1; right=j+1
  if up<0: sup=system[m,j]
  else: sup=system[up,j]
  if down>m: sdown=system[0,j]
  else: sdown=system[down,j]
  if left<0: sleft=system[i,m]
  else: sleft=system[i,left]
  if right>m: sright=system[i,0]
  else: sright=system[i,right]
  return [sup, sdown, sleft, sright]
  #return [system[bc(i+1),j],system[bc(i-1),j],system[i,bc(j+1)],system[i,bc(j-1)]]

def loop(system,nit):
  m=len(system)-1
  for n in range(nit):
    i=np.random.randint(0,m)
    j=np.random.randint(0,m)
    neighbors=getneighbors(system,i,j)
    E=energyvar(system[i,j],neighbors)
    if E<=0:
      system[i,j]*=-1
    elif np.exp(-E/(k*T))>random():
  #  elif flips(E):
      system[i,j]*=-1
  return system

SIZE=150

def call():
  SIZE=150
  system=buildsystem(SIZE)
  final=loop(system,int(1e5))


if __name__=="__main__":
  SIZE=150
  system=buildsystem(SIZE)
  final=loop(system,int(1e7))
  figure(1)
  print np.mean(final)
  imshow(final, interpolation='nearest')
  grid(True)
  #savefig("ising2.png")
