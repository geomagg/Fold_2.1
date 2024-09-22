import numpy as np
import matplotlib.pyplot as plt


cmp = np.load('cmp__.npz')
off =cmp['offset'] 
t=cmp['azim']
ang=(t*np.pi)/180. 


nr = 30
ntheta = 48
s = np.linspace(1, 6000.,nr+1 )
a = np.linspace(0, 2*np.pi, ntheta+1)

print len(s),len(a)

H, _, _ = np.histogram2d(off, ang ,[s, a])
theta, r = np.meshgrid(a,s)

cmap = plt.get_cmap('rainbow')
ax = plt.subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.tick_params(axis='both', which='major', labelsize=6)
ax.tick_params(axis='both', which='minor', labelsize=6)

im=ax.pcolormesh(theta, r,H ,cmap=cmap)
cbar = plt.colorbar(im,orientation="horizontal",aspect=40,ax=ax)

plt.title('Offset Distribution')
plt.grid(True)
plt.grid(color='black', linestyle='--', linewidth=.4)
cbar.set_label('# of hits', rotation=0)
plt.show()
