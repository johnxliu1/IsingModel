#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
from random import choice, random, randint
#cambiar pylab por matplotlib
from pylab import imshow, figure, grid, show, savefig
from math import exp
import cenergy
#CTES
k=1
T=0.1;
J=1;

def buildsystem(m): #optimizar
  system=np.empty([m,m])
  for i in xrange(m):
    for j in xrange (m):
      system[i,j]=choice([1,-1])
  return system

def loop(system,nit,T): #compile
  m=len(system)-1
  for n in xrange(nit):
    i=np.random.randint(0,m)
    j=np.random.randint(0,m)
    E=cenergy.get_energy(system,i,j,m)*J
    if E<=0:
      system[i,j]*=-1
    elif exp(-E/(k*T))>random():
      system[i,j]*=-1
  return system

def plotting(system):
  imshow(system, interpolation='nearest')
  grid(True)
  savefig("plot.png")

def callising(iterations, size, temperature):
  T=temperature
  system=buildsystem(size)
  final=loop(system,int(size,T)

if __name__=="__main__":
  SIZE=150
  system=buildsystem(SIZE)
  final=loop(system,int(1e7))
  figure(1)
  #print np.mean(final)
  imshow(final, interpolation='nearest')
  grid(True)
  savefig("long2.png")
