import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import *
x = linspace(0, 7, 70)
y = cos(x)
y2= sin(x)

from matplotlib import pyplot as plt
plt.grid
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x) $un $sin(x)$')
plt.plot(x, y, color = "#7FFF00")
plt.plot(x, y2, color ="#0000FF")
plt.show()



