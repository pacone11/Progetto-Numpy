**Step 1**

Script Python che itera in ordine alfabetico sui file della cartella files e, a seconda del tipo (audio, documento, immagine), li sposta nella relativa sottocartella. Se la sottocartella non esiste, lo script la crea automaticamente.

Durante il ciclo, lo script stampa le informazioni dei file: nome, tipo e dimensione in byte. 

Man mano che i file vengono  spostati, il documento *recap.csv* viene aggiornato con le stesse informazioni.

**Step 2**

Creazione di un file eseguibile (*addfile.py*, situato nella stessa cartella del notebook) dotato di *interfaccia a linea di comando* (CLI)

Lo scopo dell'eseguibile è spostare un *singolo* file (che si trova nella cartella files) nella sottocartella di competenza, aggiornando il file recap.csv

L'interfaccia dell'eseguibile ha come unico argomento (obbligatorio) il nome del file da spostare, comprensivo di formato (*nome_file*).  
Nel caso in cui il file passato come argomento non esiste, l'interfaccia lo comunica all'utente.

**Step 3**

Script che itera sulla sottocartella *img* e costruisce una tabella riassuntiva prodotta con la libreria *tabulate*.

Oltre al nome del file, la tabella riporta:

- altezza dell'immagine, in pixel
- larghezza dell'immagine, in pixel
- se l'immagine è in scala di grigio, la colonna *grayscale* indica la media dei valori dell'unico livello di colore
- se l'immagine è a colori, le altre colonne indicano la media dei valori di ogni livello di colore (per RGB) e opacità (per RGBA).
