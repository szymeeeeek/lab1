import math
from csv import writer
from tkinter import Tk, filedialog
from random import uniform


def generate_points(num_points: int = 2000, radius: float = 20, height: float = 40):
    points = []
    for _ in range(num_points):
        # Losowy kąt phi od 0 do 2*pi
        phi = uniform(0, 2 * math.pi)
        # Losowa wysokość od 0 do height
        z = uniform(0, height)
        # Obliczenie współrzędnych x i y na podstawie promienia i kąta phi
        x = radius * math.cos(phi)
        y = radius * math.sin(phi)
        points.append((x, y, z))
    return points


if __name__ == '__main__':
    num_points = 2000
    radius = 20
    height = 40
    cloud_points = generate_points(num_points, radius, height)

    root = Tk()
    root.withdraw()  # Ukryj główne okno

    file_path = filedialog.asksaveasfilename(defaultextension=".xyz")
    if file_path:
        with open(file_path, 'w', encoding='utf-8', newline='\n') as csvfile:
            csvwriter = writer(csvfile)
            for p in cloud_points:
                csvwriter.writerow(p)
        print("Dane zostały zapisane.")
    else:
        print("Operacja zapisu została anulowana.")
