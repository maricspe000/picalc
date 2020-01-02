import numpy as np

num = 0

for k in range(99999999):
  i = k+1
  num += 1/(i*i)

pi = np.sqrt(num*6)

print(pi)
