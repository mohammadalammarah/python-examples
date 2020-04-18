
#!/usr/bin/env python3

# 13Jul16  Adapted from newimg.py by Everett Lipman
#

import math

limit = 2
def mandelbrot(z,maxiter):
    c = z
    for n in range(0,maxiter):
        if abs(z) > limit:
            return n
        z = z*z + c
     #   print("z",z)
    return maxiter



import numpy as np
import matplotlib.pyplot as plt

#
# image size
#
X =512
Y = 383
xpoint = 0.262
ypoint = 0.49075
scale = 1000000
loff = X/2 - xpoint*scale
boff = Y/2 - ypoint*scale

#
# array for image data (pixel values): one integer value at each (x,y) point
#
# color is determined from pixel value by the colormap
#
pvals = np.zeros((X,Y), dtype='uint')

xinc = 1000/X
yinc = 1000/Y


for j in range(Y):
   for i in range(X):
        mValue = mandelbrot(complex((i-loff)/scale, (j-boff)/scale),250)
        pvals[i,j] = 256 - mValue


#
# Transpose and flip rows so that origin is displayed at bottom left,
# with x horizontal and y vertical.
#

plotarr = np.flipud(pvals.transpose())

f1, ax1 = plt.subplots()



picture = ax1.imshow(plotarr, interpolation='none', cmap='gnuplot2')

# lines below just change the axis labels
a=ax1.get_xticks().tolist()

plt.draw()
ll=[]
for item in a:
    ll.append(str(((float(item)-loff)/scale)))
print(ll)
ax1.set_xticklabels(ll)

a=ax1.get_yticks().tolist()

ll=[]
for item in a:
    ll.append(str((Y - boff - float(item))/scale))
print(ll)
ax1.set_yticklabels(ll)


#
# draw figure
#
f1.show()

input("\nPress <Enter> to exit...\n")
