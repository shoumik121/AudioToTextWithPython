import numpy as np
import matplotlib.pyplot as plt


str=input('Enter the Text:')

print("Text: " + str)
data_temp = ' '.join(format(ord(x), 'b') for x in str)

print("Text to Binary: " + data_temp)
data = ''.join(format(ord(x), 'b') for x in str)
print("Text to Binary(marged): " + data)

c = list(data)
data = list(map(int, c))

print ("Binary data to list: ")
print (c)
print ("Binary data to list(int): ")
print (data)

xs = np.repeat(range(len(data)),2)
ys = np.repeat(data, 2)
xs = xs[1:]
ys = ys[:-1]
plt.plot(xs, ys)
plt.xlim(0,len(data)+0.5)
plt.ylim(-1, 2)
plt.grid()
plt.show()
#plt.hold(True)
#plt.pause(0.5)
plt.clf()