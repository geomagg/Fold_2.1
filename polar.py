import numpy as np
import matplotlib.pyplot as plt


cmp = np.load('cmp__.npz')
r =cmp['offset'] 
t=cmp['azim']
theta=(t*np.pi)/180 +np.pi
area=r/1000

colors = r

fig = plt.figure()
ax = fig.add_subplot(111,projection='polar')
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
plt.show()
