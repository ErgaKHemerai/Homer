# Homer Project, Alfredo Pizzirani, 2025
# Distance calculation
# This is the first program in the pipeline. The full pipeline computes distances between occurrences of the same lemma.
# input: download a file from https://github.com/gcelano/LemmatizedAncientGreekXML/tree/master/texts
# output: a text file with the layout: ['line number', 'Original word forms', 'Lemmatized words']

import xml.etree.ElementTree as ET
from collections import defaultdict
import csv

file_name = 'LAG_full_Iliad'
input_file = file_name + '.xml'
output_file = file_name + '.txt'

# Parse the XML file
tree = ET.parse(input_file)  # Replace with your actual file path
root = tree.getroot()

# Group f and l1 values by p line number
f_grouped = defaultdict(list)
l1_grouped = defaultdict(list)

# Traverse each <t> element
for t in root.iter('t'):
    raw_p = t.attrib.get('p', 'N/A')
    p_value = raw_p.split('.')[-1] if '.' in raw_p else raw_p

    for f in t.iter('f'):
        if f.text:
            f_grouped[p_value].append(f.text)

    for l1 in t.iter('l1'):
        if l1.text:
            l1_grouped[p_value].append(l1.text)

# Get a sorted list of all unique p values
#all_p_values = sorted(set(f_grouped.keys()) | set(l1_grouped.keys()), key=lambda x: int(x) if x.isdigit() else x)
all_p_values = sorted(set(f_grouped.keys()) | set(l1_grouped.keys()), key=lambda x: (0, int(x)) if x.isdigit() else (1, x))

# Build combined output: [p, f_list, l1_list]
combined_output = []
for p in all_p_values:
    f_list = f_grouped.get(p, [])
    l1_list = l1_grouped.get(p, [])
    combined_output.append([p, f_list, l1_list])

# Export to CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['line', 'Original', 'Lemmatized'])  # header
    for row in combined_output:
        writer.writerow([row[0], ', '.join(row[1]), ', '.join(row[2])])

print("Data exported to", output_file)
