from openpyxl import load_workbook
import os

wb = load_workbook("C:\\Users\\rizzesim\\Documents\\20251026NotteSanLorenzoSvp.xlsx")
ws = wb.active

output_dir = "C:\\Users\\rizzesim\\Documents\\immagini_estratte"
os.makedirs(output_dir, exist_ok=True)

for i, image in enumerate(ws._images, start=1):
    img_ref = image.anchor._from
    cell_ref = f"{img_ref.col + 1}{img_ref.row + 1}"
    img_path = os.path.join(output_dir, f"img_{i}_{cell_ref}.png")
    image.ref.save(img_path)

print("Immagini esportate.")