from scipy.stats import norm
from csv import writer
from tkinter import Tk, filedialog


def generate_points(num_points: int = 2000):
    distribution_x = norm(loc=0, scale=20)
    distribution_z = norm(loc=0, scale=20)

    x = distribution_x.rvs(size=num_points)
    y = [0] * num_points
    z = distribution_z.rvs(size=num_points)

    points = zip(x, y, z)
    return points


if __name__ == '__main__':
    num_points = 2000
    cloud_points = generate_points(num_points)

    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.asksaveasfilename(defaultextension=".xyz")
    if file_path:
        with open(file_path, 'w', encoding='utf-8', newline='\n') as csvfile:
            csvwriter = writer(csvfile)
            for p in cloud_points:
                csvwriter.writerow(p)
        print("Dane zostały zapisane.")
    else:
        print("Operacja zapisu została anulowana.")
