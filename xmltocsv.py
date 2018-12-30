import xml.etree.ElementTree as ET
import csv
import sys

input_filename = str(sys.argv[1])
output_filename = str(sys.argv[2])

file = open(input_filename, "r")
xmldata = file.readlines()[1]
root = ET.fromstring(xmldata)

output_data = open(output_filename, 'w')
csvwriter = csv.writer(output_data)
csv_header = []

csv_header.append("Name")
csv_header.append("Device Count")
csvwriter.writerow(csv_header)

for member in root.iter('row'):
	csv_body = []
	name = member.find('name').text
	csv_body.append(name)
	device_count = member.find('count').text
	csv_body.append(device_count)
	csvwriter.writerow(csv_body)
output_data.close()
