#importing all required modules
import os
import csv
import statistics as s

#declaring all variables
count = 0
total = 0
templist = []
templistdate = []
avglist = []
avgchange = 0
finalavg = 0
greatinc = 0 
greatdec = 0

print("Financial Analysis")
print("-------------------")

#Giving the file path
file_path = os.path.join("Resources", "budget_data.csv")

# opening the file and reading the data
with open (file_path) as csv_file:
    csvreader=csv.reader(csv_file, delimiter = ',')
    csv_header=next(csv_file)
    
    #creating a list each for storing date,profit/loss values; 
    #finding the number of months, total of profits/loss
    for row in csvreader:
        count=count+1
        total= total + int(row[1])
         
        templist.append(row[1])
        templistdate.append(row[0])
        
    print("Total Months: " + str(count))
    print("Total: $"+ str(total))
    
    # looping through the list that has profit/loss values to
    #calculate change of values for each month and storing it in another list
    for i in range (len(templist)-1):
    
        initial = templist[i]
        final = templist[i+1]
       
        avgchange = int(final) - int(initial)
        avglist.append(avgchange)
        
    #finding the avreage change of values,maximum,minimum values from the list
    finalavg = s.mean(avglist)
    print("Average Change: $"+str(finalavg))
    
    greatinc = max(avglist)
    greatdec = min(avglist)
    
    #getting the index of maximum value and using index to compare lists
    a = avglist.index(greatinc)
    max_month = templistdate[a + 1]
    print(f"Greatest Increase in Profits: {max_month}, (${greatinc})")
    
    #getting the index of minimum value and using index to compare lists
    b = avglist.index(greatdec)
    min_month = templistdate[b + 1]
    print(f"Greatest Decrease in Profits: {min_month}, (${greatdec})")
 
 #Giving the output path 
output_path = os.path.join("Result.txt")

#Opening file to write data and closing file once complete
with open(output_path, 'w', newline='') as text_file:
    text_file.write("Financial Analysis")
    text_file.write("\n-------------------")
    text_file.write("\nTotal Months:" + str(count))
    text_file.write("\nTotal: $" +str(total))
    text_file.write("\nAverage Change: $" +str(finalavg))
    text_file.write(f"\nGreatest Increase in Profits: {max_month}, (${greatinc})")
    text_file.write(f"\nGreatest Decrease in Profits: {min_month}, (${greatdec})")

text_file.close()

    