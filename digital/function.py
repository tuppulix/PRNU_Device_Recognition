import numpy as np
from scipy.ndimage import gaussian_filter
from tabulate import tabulate
import os
import cv2

def extract_prnu(image):     #Estrae il PRNU da un'immagine.
    
    denoised_image = gaussian_filter(image, sigma=1)
    noise_residual = image.astype(float) - denoised_image.astype(float)
    mean = np.mean(noise_residual)
    std = np.std(noise_residual)
    normalized_noise_residual = (noise_residual - mean) / std
    return normalized_noise_residual

def average_prnu(images):       #Calcola il PRNU medio da una lista di immagini.
    if not images:
        raise ValueError("No images provided for PRNU calculation.")
    
    prnu_sum = None
    count = len(images)
    for image in images:
        prnu = extract_prnu(image)
        if prnu_sum is None:
            prnu_sum = prnu
        else:
            prnu_sum += prnu
    average_prnu = prnu_sum / count
    return average_prnu

def process_device_images(device_folder):      #Processa tutte le immagini di una cartella di un dispositivo per calcolare il PRNU medio.
    
    image_files = [os.path.join(device_folder, f) for f in os.listdir(device_folder) if f.lower().endswith(('.jpg', '.jpeg'))]
    if not image_files:
        raise ValueError(f"No images found in directory {device_folder}")
    
    images = []
    for image_file in image_files:
        try:
            image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
            if image is None:
                print(f"Unable to read image file: {image_file}")
                continue
            normalized_image = cv2.equalizeHist(image)
            images.append(cv2.resize(normalized_image, (700, 1080)))
        except cv2.error as e:
            print(f"Error processing image file {image_file}: {e}")
        except Exception as e:
            print(f"Unexpected error processing image file {image_file}: {e}")
    
    if not images:
        raise ValueError(f"No valid images processed in directory {device_folder}")
    
    avg_prnu = average_prnu(images)
    return avg_prnu

def classify_image(test_image, avg_prnus):         #Classifica un'immagine di test confrontandola con i PRNU medi dei dispositivi.

    test_prnu = extract_prnu(test_image)
    differences = {}
    for device, avg_prnu in avg_prnus.items():
        difference = np.linalg.norm(test_prnu - avg_prnu)
        differences[device] = difference
    closest_device = min(differences, key=differences.get)
    return closest_device, differences
