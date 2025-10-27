import xml.etree.ElementTree as ET
fp='C:\\Users\\rizzesim\\OneDrive - CASA DAMIANI SPA\\Documenti\\Workspace Visual\\Python\\scratches\\'
#tree = ET.parse('/Users/Simone/Desktop/country_data.xml')
tree = ET.parse(fp+'plant_catalog.xml')
root = tree.getroot()

#print (root)

for child in root:
    print (child.tag, child.attrib)
    for gc1 in child:
        print ('    1 ',gc1.tag,gc1.text)
        for gc2 in gc1:
            print('     2 ',gc2.tag,'___',gc2.text)
            for gc3 in gc2:
                print('         3 ',gc3.tag,'___', gc3.text)

#for denominazione in root.iter('Denominazione'):
    #print (denominazione.attrib)
#print(root[1].findall('.//ImportoTotaleDocumento'))
#print(root.findall('.//Denominazione')[0].text)
