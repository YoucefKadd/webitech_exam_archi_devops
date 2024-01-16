import os
from numpy import log

print("bon on essayer hein")

a = os.environ['A']
b = os.environ['B']
# Tache 4
print('la multiplication : ', a * b)

# BONUS
log1 = log(a*b)
log2 = log(a) + log(b)

print('BONUS :')
print('log(a*b) = ', log1)
print('log(a) + log(b) = ', log2)

print('hamdoulilah')
