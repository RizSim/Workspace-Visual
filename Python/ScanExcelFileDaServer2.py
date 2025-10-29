import os
import pandas as pd

# 🔧 Inserisci qui il percorso reale della cartella con i file Excel
input_directory = r'\\fsval\archivio$\Docsvps\SCHEDE TECNICHE FORNITORI\LABORATORIO DAMIANI'
output_directory = r'C:\Users\rizzesim\OneDrive - CASA DAMIANI S.P.A\Allegati'

# Funzione per generare il nome del file con numero progressivo
def get_unique_filename(base_path):
    if not os.path.exists(base_path):
        return base_path
    
    base_name, ext = os.path.splitext(base_path)
    counter = 1
    while True:
        new_path = f"{base_name}_{counter}{ext}"
        if not os.path.exists(new_path):
            return new_path
        counter += 1

# Genera il nome del file di output
base_output_file = os.path.join(output_directory, 'riepilogo_fogli.txt')
output_file = get_unique_filename(base_output_file)

riepilogo = []

for filename in os.listdir(input_directory):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_path = os.path.join(input_directory, filename)
        try:
            excel_file = pd.ExcelFile(file_path, engine='openpyxl' if filename.endswith('.xlsx') else 'xlrd')
            for sheet_name in excel_file.sheet_names:
                df = excel_file.parse(sheet_name)
                cell_value = str(df.iat[2, 2]) if not df.empty else 'Foglio vuoto'
                riepilogo.append(f"File: {filename} | Foglio: {sheet_name} | Cella C3: {cell_value}")
        except Exception as e:
            riepilogo.append(f"File: {filename} | Errore: {e}")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(riepilogo))

print(f"✅ Riepilogo completato. File salvato in: {output_file}")