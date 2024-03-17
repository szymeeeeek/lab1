import numpy as np
from tkinter import filedialog
import tkinter as tk

def generate_and_save_points_flat_horizontal(width, length, num_points, filepath):
    x_coords = np.random.uniform(0, width, num_points)
    y_coords = np.random.uniform(0, length, num_points)
    z_coords = np.zeros(num_points)
    points = np.column_stack((x_coords, y_coords, z_coords))
    np.savetxt(filepath, points, fmt='%.6f', header='x y z', comments='')
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(defaultextension=".xyz",filetypes=(("XYZ files","*.xyz"),("ALL files","*.*")),initialfile=f'horizontal_{num_points}.xyz')
    if save_path:
        np.savetxt(save_path, points, delimiter=' ', fmt='%.6f')
        print("Point cloud saved successfully.")
    else:
        print("Save operation canceled.")
# Przykład użycia
width = 10
length = 20
num_points = 100
filepath = 'flat_horizontal_points.xyz'
generate_and_save_points_flat_horizontal(width, length, num_points, filepath)
