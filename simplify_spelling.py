# Homer Project, Alfredo Pizzirani, 2025
# This program reads a file in xml format and outputs a txt file.
# Output txt file line format: line number, speaker, original line text, line text in simplified conventional spelling.
# Before running this program: add speaker tags to source, if desired.


import xml.etree.ElementTree as ET
import csv
import re

file_name = "Iliad1_clean"          # Replace with relevant file name


def simplify_spelling(linename):
    # this functions removes capitals, accents, breathings, punctiation marks; replaces diphtongs with conventional signs and splits double consonants
    vowels = ["α","ε","η","ι","ο","υ","ω","ᾳ","ῃ","ῳ","1","2","3","4","5","6","7","8"]
    shortvowel = ["ε","ο"]
    longvowel = ["η","ω","ᾳ","ῃ","ῳ","1","2","3","4","5","6","7","8"]

    #Remove capitals
    linename = linename.lower()

    # remove all accents and breatings, because they have no bearing on scansion. Preserve subscribed iotas, because they mark long vowels. Also, ϊ is not reduced to ι so that it will be treated as a distinct vowel in the following steps
    linename = linename.replace("ά","α")
    linename = linename.replace("ὰ","α")
    linename =  linename.replace("ᾶ","α")
    linename =  linename.replace("ἀ","α")
    linename =  linename.replace("ἄ","α")
    linename =  linename.replace("ἂ","α")
    linename =  linename.replace("ἆ","α")
    linename =  linename.replace("ἁ","α")
    linename =  linename.replace("ἅ","α")
    linename =  linename.replace("ἃ","α")
    linename =  linename.replace("ἇ","α")
    linename =  linename.replace("ᾴ","ᾳ")
    linename =  linename.replace("ᾲ","ᾳ")
    linename =  linename.replace("ᾷ","ᾳ")
    linename =  linename.replace("ᾀ","ᾳ")
    linename =  linename.replace("ᾄ","ᾳ")
    linename =  linename.replace("ᾂ","ᾳ")
    linename =  linename.replace("ᾆ","ᾳ")
    linename =  linename.replace("ᾁ","ᾳ")
    linename =  linename.replace("ᾅ","ᾳ")
    linename =  linename.replace("ᾃ","ᾳ")
    linename =  linename.replace("ᾇ","ᾳ")
    linename =  linename.replace("ί","ι")
    linename =  linename.replace("ὶ","ι")
    linename =  linename.replace("ῖ","ι")
    linename =  linename.replace("ἰ","ι")
    linename =  linename.replace("ἴ","ι")
    linename =  linename.replace("ἲ","ι")
    linename =  linename.replace("ἶ","ι")
    linename =  linename.replace("ἱ","ι")
    linename =  linename.replace("ἵ","ι")
    linename =  linename.replace("ἳ","ι")
    linename =  linename.replace("ἷ","ι")
    linename =  linename.replace("ύ","υ")
    linename =  linename.replace("ὺ","υ")
    linename =  linename.replace("ῦ","υ")
    linename =  linename.replace("ὐ","υ")
    linename =  linename.replace("ὔ","υ")
    linename =  linename.replace("ὒ","υ")
    linename =  linename.replace("ὖ","υ")
    linename =  linename.replace("ὑ","υ")
    linename =  linename.replace("ὕ","υ")
    linename =  linename.replace("ὓ","υ")
    linename =  linename.replace("ὗ","υ")
    linename =  linename.replace("ῄ","ῃ")
    linename =  linename.replace("ῂ","ῃ")
    linename =  linename.replace("ῇ","ῃ")
    linename =  linename.replace("ᾐ","ῃ")
    linename =  linename.replace("ᾔ","ῃ")
    linename =  linename.replace("ᾒ","ῃ")
    linename =  linename.replace("ᾖ","ῃ")
    linename =  linename.replace("ᾑ","ῃ")
    linename =  linename.replace("ᾕ","ῃ")
    linename =  linename.replace("ᾓ","ῃ")
    linename =  linename.replace("ᾗ","ῃ")
    linename =  linename.replace("ώ","ω")
    linename =  linename.replace("ὼ","ω")
    linename =  linename.replace("ῶ","ω")
    linename =  linename.replace("ὠ","ω")
    linename =  linename.replace("ὤ","ω")
    linename =  linename.replace("ὢ","ω")
    linename =  linename.replace("ὦ","ω")
    linename =  linename.replace("ὡ","ω")
    linename =  linename.replace("ὥ","ω")
    linename =  linename.replace("ὣ","ω")
    linename =  linename.replace("ὧ","ω")
    linename =  linename.replace("έ","ε")
    linename =  linename.replace("ὲ","ε")
    linename =  linename.replace("ἐ","ε")
    linename =  linename.replace("ἔ","ε")
    linename =  linename.replace("ἒ","ε")
    linename =  linename.replace("ἑ","ε")
    linename =  linename.replace("ἕ","ε")
    linename =  linename.replace("ἓ","ε")
    linename =  linename.replace("ό","ο")
    linename =  linename.replace("ὸ","ο")
    linename =  linename.replace("ὀ","ο")
    linename =  linename.replace("ὄ","ο")
    linename =  linename.replace("ὂ","ο")
    linename =  linename.replace("ὁ","ο")
    linename =  linename.replace("ὅ","ο")
    linename =  linename.replace("ὃ","ο")
    linename =  linename.replace("ῴ","ῳ")
    linename =  linename.replace("ῲ","ῳ")
    linename =  linename.replace("ῷ","ῳ")
    linename =  linename.replace("ᾠ","ῳ")
    linename =  linename.replace("ᾤ","ῳ")
    linename =  linename.replace("ᾢ","ῳ")
    linename =  linename.replace("ᾦ","ῳ")
    linename =  linename.replace("ᾡ","ῳ")
    linename =  linename.replace("ᾥ","ῳ")
    linename =  linename.replace("ᾣ","ῳ")
    linename =  linename.replace("ᾧ","ῳ")
    linename =  linename.replace("ή","η")
    linename =  linename.replace("ὴ","η")
    linename =  linename.replace("ῆ","η")
    linename =  linename.replace("ἠ","η")
    linename =  linename.replace("ἤ","η")
    linename =  linename.replace("ἢ","η")
    linename =  linename.replace("ἦ","η")
    linename =  linename.replace("ἡ","η")
    linename =  linename.replace("ἥ","η")
    linename =  linename.replace("ἣ","η")
    linename =  linename.replace("ἧ","η")
    linename =  linename.replace("ΰ","ϋ")
    linename =  linename.replace("ῢ","ϋ")
    linename =  linename.replace("ῧ","ϋ")
    linename =  linename.replace("ΐ","ϊ")
    linename =  linename.replace("ῒ","ϊ")
    linename =  linename.replace("ῗ","ϊ")
    
       
    # replace diphtongs with conventional symbols to simplify parsing. 
    linename =  linename.replace("αι","1")
    linename =  linename.replace("αυ","2")
    linename =  linename.replace("ει","3")
    linename =  linename.replace("ευ","4")
    linename =  linename.replace("ηυ","5")
    linename =  linename.replace("οι","6")
    linename =  linename.replace("ου","7")
    linename =  linename.replace("υι","8")


    # remove punctuation (including apostrophes) and spaces
    linename =  linename.replace(",","")
    linename =  linename.replace(";","")
    linename =  linename.replace(":","")
    linename =  linename.replace(".","")
    linename =  linename.replace("ʼ","")
    linename =  linename.replace("·","")
    linename =  linename.replace(" ","")
    linename =  linename.replace('"',"")
    linename =  linename.replace('-',"")
    linename =  linename.replace("?","")
    linename =  linename.replace("!","")
    linename =  linename.replace("(","")
    linename =  linename.replace(")","")

    # split double consonants
    linename =  linename.replace("ζ","σδ")
    linename =  linename.replace("ξ","κσ")
    linename =  linename.replace("ψ","πσ")
    
    return linename

input_file = file_name + ".xml"
output_file = file_name + ".txt"
output_row = []

tree = ET.parse(input_file)
root = tree.getroot()

elements_to_process = [root]

file = open(output_file, 'w', encoding='utf-8', newline='')
writer = csv.writer(file)
    

while elements_to_process:
    elem = elements_to_process.pop(0) # this removes and returns the first element of the tree
    
    tag_info = f"Tag: <{elem.tag}>" # f-string (formatted string literal): embeds expression into string
    if elem.attrib:
        tag_info += f" - Attributes: {elem.attrib}"
    if elem.text and elem.text.strip():
        tag_info += f" - Text: {elem.text.strip()}"
    if elem.tag == "speaker":
        speaker = elem.text
    if elem.tag == "l" :
        line_attrib = elem.attrib # returns a dictionary, in the form {'n': '4'}
        line_numb = line_attrib['n']
        original_text = elem.text
        simplified_text = simplify_spelling(original_text)
        output_row.append(line_numb)
        output_row.append(speaker)
        output_row.append(original_text)
        output_row.append(simplified_text)
    if output_row:      # if the output list is not empty, write it, else skip and down write empty lines
        writer.writerow(output_row)
        line_numb = ""
        original_text = ""
        output_row = []
        
    
    elements_to_process.extend(list(elem)) #list(elem) creates a list of children, and extend adds each children to the bottom of elements_to_process
file.close()