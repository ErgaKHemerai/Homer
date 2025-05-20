# Homer Project, Alfredo Pizzirani, 2025
# take a word list from Scaife Viewer and format it for Excel

import csv
import re

file_name = "Iliad1_words"
input_file = file_name + ".txt"
output_file = file_name + "_formatted.txt"

file = open(output_file, 'w', encoding='utf-8', newline='')
writer = csv.writer(file)
header = ('lemma','definition','frequency per 10k words')
writer.writerow(header)

with open(input_file, 'r', encoding='utf-8') as input_file :
    reader = csv.reader(input_file)
    
    for line in reader:
        entry = ",".join(line) # the line is read as a list; convert it to a string inserting a comma between list items
        if entry :
            lemma = entry.split()[0]
            start_def = len(lemma)
            freq_text = re.search(r'\((\d+(?:\.\d+)?)\)$', entry) # regular expression to select content of parenthesis at end of string
            frequency = float(freq_text.group(1))
            end_def, end_freq = freq_text.span()
            definition = entry[start_def:end_def]
            output_row=(lemma, definition, frequency)
            writer.writerow(output_row)

            print (lemma, definition, frequency)
        else :
            continue

file.close() 