import numpy as np import matplotlib-pyplot as plt from mpl_toolkits.mplot3d import Axes3D
# Définition des paramètres pour l'hyperboloide à une nappe = 1 # rayon selon l'axe ›
= 1 # ravon celon 'axe
c = 1 # distance du centre à l'axe z
# Création des coordonnées theta et phi
theta = np. linspace(0, 2 * np.pi, 50)
phi = np. linspace (-0.5 * np.pi, 0.5 * np.pi, 50)
theta, phi = np.meshgrid (theta, phi)
# Coordonnées en 3D de 1 'hyperboloide
x = a * np. cosh(phi) * np. cos (theta)
Y = b * np.cosh(phi) * np.sin(theta)
Z = c * np. sinh (phi)
# Création de la figure et de l'axe 3D
fig = plt.figure()
ax = fig.add_subplot[a11, projection= '3d*5]
# Dessin de I'hyperboloide
ax-plot_surface(X, Y, Z, rstride=1, cstride=1, color='b', alpha=0.7, linewidth=0)
# Réglage des limites des axes ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax. set zlim(1-3, 31)
# Étiquettes des axes ax.set xlabel Axe X
ax.set _ylabel('Axe Y')
ax.set_zlabel( 'Axe Z')
#Affichage du graphique
plt.show()