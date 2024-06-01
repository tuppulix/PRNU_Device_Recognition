import os
import csv

def generate_csv(directory, csv_filename):  #Genera un file CSV con i percorsi completi delle immagini e le etichette dei dispositivi,
                                            #considerando solo le cartelle che iniziano con 'device'.

    data = []

    # Itera attraverso tutte le sottocartelle (dispositivi)
    for root, dirs, files in os.walk(directory):
        # Considera solo le cartelle che iniziano con 'device'
        if os.path.basename(root).startswith('Tdevice'):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg')):
                    # Ottieni il percorso completo dell'immagine
                    full_path = os.path.join(root, file)
                    # L'etichetta del dispositivo è il nome della cartella padre
                    label = os.path.basename(root)
                    label=label.replace('T','')
                    data.append([full_path, label])

    # Scrivi i dati nel file CSV
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['image_path', 'label'])
        writer.writerows(data)

    print(f"CSV file '{csv_filename}' generated successfully.")

# Specifica il percorso della directory principale e il nome del file CSV
directory = 'digital'
csv_filename = 'test_labels.csv'

# Genera il file CSV
generate_csv(directory, csv_filename)
