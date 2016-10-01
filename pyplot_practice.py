from matplotlib import pyplot as plt
from skimage import data

# basic plot.
plt.plot([1, 2, 3, 4])
plt.show()

 # pyplot have the concept of the current figure and the current axes. All plotting commands apply to the current axes.
image = data.astronaut()
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.imshow(image)
plt.show()
