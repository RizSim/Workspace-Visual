import os
import pandas as pd

# 🔧 Inserisci qui il percorso reale della cartella con i file Excel
input_directory = r'C:\Users\rizzesim\OneDrive - CASA DAMIANI SPA\LD Reporting\General\REPORTISTICA'  # <-- Modifica questo percorso
output_file = os.path.join(input_directory, 'riepilogo_fogli.txt')

riepilogo = []

for filename in os.listdir(input_directory):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_path = os.path.join(input_directory, filename)
        try:
            excel_file = pd.ExcelFile(file_path, engine='openpyxl' if filename.endswith('.xlsx') else 'xlrd')
            for sheet_name in excel_file.sheet_names:
                df = excel_file.parse(sheet_name)
                cell_value = str(df.iat[0, 0]) if not df.empty else 'Foglio vuoto'
                riepilogo.append(f"File: {filename} | Foglio: {sheet_name} | Cella A1: {cell_value}")
        except Exception as e:
            riepilogo.append(f"File: {filename} | Errore: {e}")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(riepilogo))

print(f"✅ Riepilogo completato. File salvato in: {output_file}")