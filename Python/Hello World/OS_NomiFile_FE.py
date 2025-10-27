import os
import xml.etree.ElementTree as ET

fp='C:\\Users\\rizzesim\\OneDrive - CASA DAMIANI SPA\\Documenti\\Workspace Visual\\Python\\scratches\\'


with os.scandir(fp) as it:
    for entry in it:
        #if not entry.name.startswith('.') and entry.is_file():
            #print(entry.name)
        if entry.name.startswith('IT') and entry.is_file():
            print(entry.name)


#tree = ET.parse('/Users/Simone/Desktop/country_data.xml')
tree = ET.parse(entry.name[0])
print('pallo',entry.name[0])
root = tree.getroot()

print(root.findall('.//Denominazione')[0].text)