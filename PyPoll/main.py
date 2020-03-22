#importing all dependencies

import os
import csv
from collections import Counter

count = 0
list_name = []

print("Election Results\n--------------------")

file_path = os.path.join("Resources","election_data.csv")

#opening file and finding the total number of votes cast
#storing only the candidates name in a list
#using the list to find the number of votes received by each candidate and store in a dictionary

with open (file_path) as csv_file:
    csvreader=csv.reader(csv_file, delimiter = ',')
    cvs_header=next(csv_file)
    
    for row in csvreader:
      count = count + 1
      list_name.append(row[2])
    print(f"Total Votes: {count}")
    mydict = Counter(list_name)
    print("----------------------")
    
    for x,y in mydict.items() :
      
      print(f"{x}: {(round((y/count)*100,2))}% ({y})")
    
#create 2 lists with only the dictionary values,keys
#Use index to find the key of the maximum value in the dictionary

v = list(mydict.values()) 
k=list(mydict.keys())
w=v.index(max(v))

print("----------------------")
print("Winner :"  + str(k[w]))
print("----------------------")
     
output_path = os.path.join("Output", "Result.txt")

#Opening file to write data and closing file once complete

with open(output_path, 'w', newline='') as text_file:
    text_file.write("Election Results")
    text_file.write("\n-------------------")
    text_file.write("\nTotal Votes:" + str(count))
    text_file.write("\n-------------------")
    for x,y in mydict.items() :
      
        text_file.write(f"\n{x}: {(round((y/count)*100,2))}% ({y})")

    text_file.write("\n-------------------")
    text_file.write("\nWinner: " + str(k[w]))
    text_file.write("\n-------------------")
    
text_file.close()


    
    

