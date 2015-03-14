#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
from __future__ import division
import numpy as np
from random import choice, random, randint
from pylab import imshow, figure, grid, show, savefig, plot
from ising import *

SIZE=100
system=buildsystem(SIZE)
mu=[]
t=np.linspace(0.1,4,30)
for T in t: 
  final=loop(system,int(1e6),T)
  mu.append(abs(np.mean(final)))

print mu
print t
  
plot(t,mu)
show()

