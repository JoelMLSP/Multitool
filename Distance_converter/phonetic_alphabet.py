student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

software_on = True

"""while software_on:
    word = input("What word do you want to be spelled out?\n ").upper()
    df = pandas.read_csv("nato_phonetic_alphabet.csv")
    for x in word:
        for (index,row) in df.iterrows():
            if str(row.letter) == str(x):
                print (f"{row.letter},{row.code}")
"""

df = pandas.read_csv("nato_phonetic_alphabet.csv")

while software_on:
    word = input("What word do you want to be spelled out?\n ").upper()
    output = {row.letter:row.code for (index, row) in df.iterrows()}
    phonetic_code = [output[letter] for letter in word]
    print (phonetic_code)