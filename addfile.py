import argparse
import os
import shutil
import csv

folder_path= "files"
folder_list= sorted(os.listdir(folder_path))
recap_file = os.path.join(folder_path, "recap.csv")

# Verifica se il file recap.csv esiste già, altrimenti crea e scrive l'intestazione
if not os.path.exists(recap_file):
    with open(recap_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['file_name','type','size(B)']) # Intestazione del CSV
        
# Definizione dei gruppi di file
file_groups = {
    'img': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'doc': ['pdf', 'docx', 'txt', 'xlsx', 'odt'],
    'audio': ['mp3', 'wav', 'flac']
}
# Lista per i file che non appartengono ad alcun gruppo
others = "others"

def add_file(file_name):
    file_path= os.path.join(folder_path, file_name)
    # Verifica se è un file
    if os.path.isfile(file_path) and file_name!='recap.csv':    # Escludi il file recap.csv dal processo
        # Estrai l'estensione
        name, extension= os.path.splitext(file_name)
        extension=extension.lstrip('.').lower()
        file_size=os.path.getsize(file_path)

        # Trova il gruppo di estensioni a cui appartiene il file
        file_type = others
        for group, extensions in file_groups.items():
            if extension in extensions:
                file_type=group
                break

        # Creazione della sottocartella se non esiste
        subfolder_path= os.path.join(folder_path, file_type)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        # Sposta il file nella sottocartella
        destination_path= os.path.join(subfolder_path, file_name)
        shutil.move(file_path, destination_path)

        # Aggiungi le informazioni al file recap.csv
        with open(recap_file, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([file_name, file_type, file_size])

        # Stampa messaggio di conferma
        print(f'{file_name} spostato nella cartella: {file_type}')
    else:
        # Logging per file non trovati
        print(f"Errore: '{file_name}' non è un file valido o non esiste.")
    
if __name__ == '__main__':
    # Parsing degli argomenti da linea di comando
    parser= argparse.ArgumentParser(description='Sposta file in base alla sua estensione')
    parser.add_argument('nome_file', help='Nome del file nella cartella "files" da spostare')
    args= parser.parse_args()

    # Verifica se il file da spostare è presente nella cartella
    if args.nome_file not in folder_list:
        print(f'Il file {args.nome_file} non è presenta nella cartella {folder_path}')
    else:
        add_file(args.nome_file)    # Lancia la funzione
