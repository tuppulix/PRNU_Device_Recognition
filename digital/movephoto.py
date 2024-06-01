import os
import random
import shutil

def transfer_random_images(src_folder, dest_folder, num_images):    #    Trasferimento foto da training a test set.

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Ottieni tutte le immagini nella cartella di origine
    images = [f for f in os.listdir(src_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if len(images) < num_images:
        raise ValueError("La cartella di origine non contiene abbastanza immagini.")
    
    # Seleziona immagini a caso
    selected_images = random.sample(images, num_images)
    
    for image in selected_images:
        src_path = os.path.join(src_folder, image)
        dest_path = os.path.join(dest_folder, image)
        shutil.move(src_path, dest_path)
        print(f"Immagine trasferita: {image}")

# Specifica il percorso della cartella di origine e della cartella di destinazione
src_folder = 'device5'
dest_folder = 'Tdevice5'
num_images = 80  # Numero di immagini da trasferire

# Trasferisci le immagini random
transfer_random_images(src_folder, dest_folder, num_images)
