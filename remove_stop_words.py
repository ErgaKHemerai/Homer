# Homer project, Alfredo Pizzirani, 2025
# loads a text file (input_file) and removes punctuation marks and stop words.
# then generates a txt file containing a line for each sentence in the text
# example: episode,Ὀρέστης,φίλτατ ἀνδρῶν προσπόλων σαφῆ σημεῖα φαίνεις ἐσθλὸς

import re
import csv
# import xml.etree.ElementTree as ET 
from lxml import etree as ET

file_name = "LAG_Iliad1" # Replace with relevant file path
input_file = file_name+".txt"  
output_file = file_name + "_nostops.txt"
words_file = "stopwords_greek.txt"  # File containing words to remove


file = open(output_file, 'w', encoding='utf-8', newline='')
writer = csv.writer(file)


def load_words(file_path):
    """Load words to remove from a file, one per line."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip().lower() for word in file)

        
def remove_punctuation(row):    # remove punctuation marks (,:"-()?!), excluding:
                                # full stops, semicolons, high point (changed to full stops)
                                # apostrophes (replace apostrophes with spaces)
    row = row.lower()           # make all words all lowercase
    row = row.translate(row.maketrans('', '', ',')) #eliminate commas
    row = row.translate(row.maketrans('', '', ';')) #eliminate semicolons
    row = row.translate(row.maketrans('', '', ':')) #eliminate colons
    row = row.translate(row.maketrans('', '', '"')) #eliminate double quotes
    row = row.translate(row.maketrans('', '', '-')) #eliminate dash 
    row = row.translate(row.maketrans('', '', '—')) #eliminate long dash
    row = row.translate(row.maketrans('', '', '?')) #eliminate question marks
    row = row.translate(row.maketrans('', '', "!")) #eliminate exclamation marks
    row = row.translate(row.maketrans('', '', '(')) #eliminate left parenthesis
    row = row.translate(row.maketrans('', '', ')')) #eliminate right parenthesis
    row = row.translate(row.maketrans('', '', "ʼ")) #eliminate apostrophes
    row = row.translate(row.maketrans('', '', "’")) #eliminate apostrophes (another form)
    row = row.translate(row.maketrans('', '', "·")) #eliminate high stop
    row = row.translate(row.maketrans('', '', ".")) #eliminate full stop
    return row
    
def remove_words(text, words_to_remove):
    """Remove specified words from the text."""
    pattern = r'\b(' + '|'.join(map(re.escape, words_to_remove)) + r')\b'
    cleaned_text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    return re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra spaces
            
words_to_remove = load_words(words_file)

csv_row = [] # temporary holder for data to be written to CSV
csv_data = [] # list of lists, containing one csv_row per dialog part

with open(input_file, 'r', encoding='utf-8') as input_file :
    reader = csv.reader(input_file)
    for line in reader: 
        original = line[2]
        cleaned_text = original.strip() if original else "" # remove spaces before and after the line (spaces in the line are left, even if duplicate)
        cleaned_text = cleaned_text + " " 
        cleaned_text = remove_punctuation(cleaned_text)
        nostops_text = remove_words(cleaned_text, words_to_remove)

        csv_row = [line[0], line[1], line[2]]    
        csv_row.append(nostops_text)
        csv_data.append(csv_row)
        csv_row = ""

with open(output_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print("Output written to", output_file)

