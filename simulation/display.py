import matplotlib.pyplot as plt
import numpy as np
import numpy.random #Only need this for simulation

x = np.random.randn(1024*40)
y = np.random.randn(1024*40)

# Create heatmap
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(40,40))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
 
# Plot heatmap
plt.clf()
plt.title('Test')
plt.ylabel('y')
plt.xlabel('x')
plt.imshow(heatmap, extent=extent)
plt.show()