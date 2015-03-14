import numpy as np
cimport cython
cimport numpy as np

#@cython.boundscheck(False)
def get_energy(np.ndarray[np.float64_t, ndim=2] system, int i,int j,unsigned int m): 
  cdef int up
  cdef int down
  cdef int left
  cdef int right
  cdef np.float64_t total
  up=i-1;  down=i+1;  left=j-1;  right=j+1
  if up<0: total=system[m,j]
  else: total=system[up,j]
  if down>m: total+=system[0,j]
  else: total+=system[down,j]
  if left<0: total+=system[i,m]
  else: total+=system[i,left]
  if right>m: total+=system[i,0]
  else: total+=system[i,right]
  return 2*system[i,j]*total
