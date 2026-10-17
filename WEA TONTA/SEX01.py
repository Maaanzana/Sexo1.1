# Instala esta mierda loco pip install matplotlib y esta tambien pip install numpy-stl
# https://drive.google.com/drive/folders/1W5tGjsizpBtWrL-kK5X7Xict-GjYPJqE?usp=drive_link DESCARGA ESA MADRE LOCO 


import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from stl import mesh
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 1. Ventana emergente para seleccionar el archivo STL
root = tk.Tk()
root.withdraw() # Oculta la ventana principal vacía
ruta_stl = filedialog.askopenfilename(
    title="SELECCIONA LA MIERDA DE STL QUE TE DIJE QUE DESCARGUES EN EL LINK DEL CODIGO PE CAUSA",
    filetypes=[("Archivos STL", "*.stl")]
)

if not ruta_stl:
    print("No seleccionaste ningún archivo. Programa terminado.")
    exit()

print(f"Cargando modelo: {ruta_stl}...")
mi_malla = mesh.Mesh.from_file(ruta_stl)

minimos = mi_malla.vectors.reshape(-1, 3).min(axis=0)
maximos = mi_malla.vectors.reshape(-1, 3).max(axis=0)
centro = (minimos + maximos) / 2.0
mi_malla.translate(-centro)

# 3. Configurar la escena 3D
fig = plt.figure(figsize=(10, 8))
fig.patch.set_facecolor('#1e1e1e')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('#1e1e1e')
ax.axis('off')

coleccion = Poly3DCollection(mi_malla.vectors, facecolors='#00bfff', linewidths=0.2, edgecolors='black', alpha=0.8)
ax.add_collection3d(coleccion)

escala_max = (maximos - minimos).max() / 2.0
ax.set_xlim([-escala_max, escala_max])
ax.set_ylim([-escala_max, escala_max])
ax.set_zlim([-escala_max, escala_max])
ax.set_box_aspect([1,1,1]) 


plt.subplots_adjust(bottom=0.15)
ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03], facecolor='#333333')

slider_angulo = Slider(
    ax=ax_slider, 
    label='Giro Horizontal (°)', 
    valmin=0, 
    valmax=360, 
    valinit=0, 
    valstep=1, 
    color='#00bfff'
)
slider_angulo.label.set_color('white')
slider_angulo.valtext.set_color('white')


def rotar_microondas(val):
    ax.view_init(elev=15, azim=slider_angulo.val)
    fig.canvas.draw_idle()

slider_angulo.on_changed(rotar_microondas)


ax.view_init(elev=15, azim=0)

print("PENE POLLA")
plt.show()
