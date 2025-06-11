#Homer Project, Alfredo Pizzirani, 2025

# USE OF THIS PROGRAM IS NOT RECOMMENDED. 

# lemmatize one book of the Iliad
# input: file produced by remove_stop_words.py
# output: comma delimited file, one row per each line of the poem, with original text words replaced with lemmas and stops removed

from cltk import NLP
import csv
from datetime import datetime


file_name = "Iliad1_clean"
input_file = file_name + "_nostops.txt"
output_file = file_name + "_lemmatized.txt"

file = open(output_file, 'w', encoding='utf-8', newline='')
writer = csv.writer(file)
header = ('line','speaker','original line', 'no stops', 'lemmatized')
writer.writerow(header)

with open(input_file, 'r', encoding='utf-8') as input_file :
    reader = csv.reader(input_file)
    print(datetime.now())    
        # Initialize for Ancient Greek
    cltk_nlp = NLP(language="grc")
    
    lemmas = ""
    
    for line in reader: 
        print(line)
        # This will automatically download necessary models
        doc = cltk_nlp.analyze(line[3])
        #print (doc)
        print(datetime.now()) 
        for word in doc.words:
            if word.stop == True:
                continue
            else :
                lemmas = lemmas + " " + word.lemma
                #print(word.lemma)
        #print (doc) # print all data extracte
        line.append(lemmas)
        writer.writerow(line)
        output_line = ()
        lemmas = ""
        # View lemmas
        # for word in doc.words:
            # print(f"Word: {word.string}, Lemma: {word.lemma}")


file.close()



