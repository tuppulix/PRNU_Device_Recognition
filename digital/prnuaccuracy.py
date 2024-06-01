import function as f
import csv
import os
import cv2


def calculate_accuracy(test_labels_file, avg_prnus):    #Calcola l'accuratezza del sistema di classificazione.
    
    correct_predictions = 0
    total_predictions = 0
    
    with open(test_labels_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_image_path = row['image_path']
            true_label = row['label']
            
            if os.path.exists(test_image_path):
                test_image = cv2.resize(cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE), (700, 1080))
                closest_device, _ = f.classify_image(test_image, avg_prnus)
                if closest_device == true_label:
                    correct_predictions += 1
                total_predictions += 1
    
    accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
    return accuracy

def main():     #Funzione principale che processa le immagini dei dispositivi e classifica un set di immagini di test.
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

    # Percorso del file CSV contenente le etichette delle immagini di test
    test_labels_file = '/test_labels.csv'

    # Calcolo dell'accuratezza
    accuracy = calculate_accuracy(test_labels_file, avg_prnus)
    print(f"\nClassification Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
