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

def generate_and_save_points_flat_vertical(width, height, num_points, filepath):
    x_coords = np.random.uniform(-width/2, width/2, num_points)
    y_coords = np.zeros(num_points)
    z_coords = np.random.uniform(0, height, num_points)
    points = np.column_stack((x_coords, y_coords, z_coords))
    np.savetxt(filepath, points, fmt='%.6f', header='x y z', comments='')
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(defaultextension=".xyz",filetypes=(("XYZ files","*.xyz"),("ALL files","*.*")),initialfile=f'vertical_{num_points}.xyz')
    if save_path:
        np.savetxt(save_path, points, delimiter=' ', fmt='%.6f')
        print("Point cloud saved successfully.")
    else:
        print("Save operation canceled.")

def generate_and_save_points_cylindrical_surface(radius, height, num_points, filepath):
    theta = np.random.uniform(0, 2*np.pi, num_points)
    z_coords = np.random.uniform(0, height, num_points)
    x_coords = radius * np.cos(theta)
    y_coords = radius * np.sin(theta)
    points = np.column_stack((x_coords, y_coords, z_coords))
    np.savetxt(filepath, points, fmt='%.6f', header='x y z', comments='')
    save_path = filedialog.asksaveasfilename(defaultextension=".xyz",
                                             filetypes=(("XYZ files", "*.xyz"), ("ALL files", "*.*")),
                                             initialfile=f'cylindrical_{num_points}.xyz')
    if save_path:
        np.savetxt(save_path, points, delimiter=' ', fmt='%.6f')
        print("Point cloud saved successfully.")
    else:
        print("Save operation canceled.")


# Przykład użycia
width = 10
length = 20
radius = 5
height = 20
num_points = 1000
filepath = 'flat_horizontal_points.xyz'
generate_and_save_points_flat_vertical(width, height, num_points, filepath)
generate_and_save_points_flat_horizontal(width, length, num_points, filepath)
generate_and_save_points_cylindrical_surface(radius, height, num_points, filepath)

