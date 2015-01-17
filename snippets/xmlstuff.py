from bs4 import BeautifulSoup

result = []

with open('dev.xml') as file:
    xml = BeautifulSoup(file)

children = xml.find_all('optic')

for child in children:
    result.append({'id': child.parent.get('id'), 
                    'location': child.parent.get('location'),
                    'type': child.get('type'),
                    'serial': child.get('serial')})
