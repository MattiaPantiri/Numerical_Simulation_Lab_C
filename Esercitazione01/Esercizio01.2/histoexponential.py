import matplotlib
import matplotlib.pyplot as plt
import numpy as np

n1, n2, n10, n100 = np.loadtxt("exponential.txt", usecols=(0,1,2,3), delimiter='	', unpack='true')

n_bins = 50
n, bins, patches = plt.hist(n1, n_bins, range=(0, 6))
plt.xlabel('ciao')
plt.ylabel('prova')
plt.title('Histogram loaded from file!')
plt.grid(True)

plt.figure()
n, bins, patches = plt.hist(n2, n_bins, range=(0, 5))
plt.xlabel('ciao')
plt.ylabel('prova')
plt.title('Histogram loaded from file!')
plt.grid(True)

plt.figure()
n, bins, patches = plt.hist(n10, n_bins, range=(0, 2.5))
plt.xlabel('ciao')
plt.ylabel('prova')
plt.title('Histogram loaded from file!')
plt.grid(True)

plt.figure()
n, bins, patches = plt.hist(n100, n_bins, range=(0.5, 1.5))
plt.xlabel('ciao')
plt.ylabel('prova')
plt.title('Histogram loaded from file!')
plt.grid(True)


plt.show()
