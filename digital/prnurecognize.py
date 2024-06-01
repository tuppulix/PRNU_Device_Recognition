import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
import os
from PIL import Image
from tabulate import tabulate
import function as f

def main():     #Funzione principale che processa le immagini dei dispositivi e classifica un'immagine di test.

    device_folders = ['device1', 'device2', 'device3', 'device4', 'device5']
    avg_prnus = {}

    for device_folder in device_folders:
        if os.path.isdir(device_folder):
            try:
                avg_prnus[device_folder] = f.process_device_images(device_folder)
                print(f"Processed {device_folder}")
            except ValueError as e:
                print(e)
        else:
            print(f"Directory {device_folder} does not exist.")

    test_image_path = 'Tdevice3/D03_I_natWA_0035.jpg' #example
    if os.path.exists(test_image_path):
        test_image = cv2.resize(cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE), (700, 1080))
        closest_device, differences = f.classify_image(test_image, avg_prnus)
        
        print("\nClassification Results:")
        print(f"Test image is most similar to: {closest_device}")
        print(f"Difference with the closest device: {differences[closest_device]:.4f}")

        # Creazione della tabella di confronto
        comparison_table = []
        for device_folder, diff in differences.items():
            comparison_table.append([device_folder, diff])
        
        print("\nComparison Table:")
        print(tabulate(comparison_table, headers=['Device', 'Difference'], floatfmt=".4f"))
    else:
        print(f"Test image {test_image_path} does not exist.")

if __name__ == "__main__":
    main()
