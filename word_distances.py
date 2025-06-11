# Homer project, Alfredo Pizzirani, 2025
# Distance calculation pipeline - third program
# loads a file with no stop words and for each lemma calculates the distance (in lines) to the next occurrence of the same lemma
# After this program, use Excel to open the output.


import re
import csv
import pdb # debugger, can remove when code is complete 

file_name = "LAG_full_Iliad" # Replace with relevant file path
input_file = file_name + "_nostops.txt"  
output_file = file_name + "_distances.txt"

list_of_lines = []
hit_list = []
hit_list_entry = []


file = open(output_file, 'w', encoding='utf-8', newline='')
writer = csv.writer(file)


csv_row = [] # temporary holder for data to be written to CSV
csv_data = [] # list of lists, containing one csv_row per dialog part

with open(input_file, 'r', encoding='utf-8') as input_file :
    book = csv.reader(input_file)
    for line in book: 
        pair = [line[0], line[3].strip()]
        list_of_lines.append(pair) # list_of_lines contains all lemmatized verses, one list per verse

for i in range(0, len(list_of_lines)) :
    #pdb.set_trace() # debug checkpoint
    current_line = list_of_lines[i]
    words = current_line[1].split(" ") # create a list where each element is one of the lemmata in the line
    end_of_range = len(list_of_lines)-1
    for word in words:
        if any(word in lemma for lemma in hit_list): # skip lemmas already processed
            continue
        else :    
            hit_list_entry.append(word)
            hit_list_entry.append(current_line[0])
            for r in range(i, end_of_range):
                #print(list_of_lines[r])
                if any(word in item for item in list_of_lines[r+1]) :  # if any(substring in item for item in my_list):
                    #print("Hit!",word, "in",list_of_lines[r][0], list_of_lines[r+1][0]) # append this to hit list
                    hit_list_entry.append(list_of_lines[r+1][0])
        hit_list.append(hit_list_entry)    
        hit_list_entry=[]
       
#print("final",hit_list)



       # #pdb.set_trace() # debug checkpoint

with open(output_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(hit_list)
print("Output written to", output_file)

