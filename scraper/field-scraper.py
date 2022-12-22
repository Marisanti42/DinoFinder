from bs4 import BeautifulSoup
import requests
import dinosaurs as dino_names

f = open("../dinosaurs.js", "w")
f.write("[")

fields_collection = []
model = 'https://www.nhm.ac.uk/discover/dino-directory/'
for name in dino_names.endpoints:
    fields = {
        "name": "",
        "type": "",
		"length": "",
		"weight": "",
        "diet": "",
        "teeth": "",
        "food": "",
        "movement": "",
        "era": "",
        "location": "",
    }
    html = requests.get(model + name + '.html').text
    parsed_html = BeautifulSoup(html, features='html.parser')
    nameContainer = parsed_html.find('h1', 'dinosaur--name dinosaur--name-unhyphenated')
    fields['name'] = nameContainer.contents[0]

    overviewContainer = parsed_html.find('dl', 'dinosaur--description dinosaur--list')
    typeContainer = overviewContainer.find('a')
    fields['type'] = typeContainer.contents[0]
    overviewDataContainer = overviewContainer.find_all('dd')
	# Some dinosaurs don't have documented lengths
    if len(overviewDataContainer) >= 2:
        fields['length'] = overviewDataContainer[1].contents[0]
	# Some dinosaurs don't have documented weights
    if len(overviewDataContainer) >= 3:
        fields['weight'] = overviewDataContainer[2].contents[0]

    detailsContainer = parsed_html.find('dl', 'dinosaur--info dinosaur--list')
    detailsHeadings = detailsContainer.find_all('dt')
    detailsData = detailsContainer.find_all('dd')
    headingMap = {
		"Diet:": "diet",
		"Teeth:": "teeth",
		"Food:": "food",
		"How it moved:": "movement",
		"When it lived:": "era",
		"Found in:": "location",
	}

    for i, heading in enumerate(detailsHeadings):
        mapableHeading = heading.contents[0]
        # if mapableHeading == "When it lived:" or "Diet:" or "Found in:":
        if mapableHeading == "When it lived:":
            fields[headingMap[mapableHeading]] = detailsData[i].find('a').contents[0]
        elif mapableHeading == "Diet:":
            fields[headingMap[mapableHeading]] = detailsData[i].find('a').contents[0]
        elif mapableHeading == "Found in:":
            fields[headingMap[mapableHeading]] = detailsData[i].find('a').contents[0]
        elif mapableHeading in headingMap:
            fields[headingMap[mapableHeading]] = detailsData[i].contents[0]

    print(fields)

    
    f.write(str(fields))
    f.write(',')


f.write(']')
f.close()

