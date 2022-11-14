
### Importing Dependencies 
import os
import csv 

### csvpath location
csvpath = os.path.join("Resources", "budget_data.csv")

### Variables for Storage
date = []# This is to store total months
revenue = [] # This is to store max and min volumes
change = [] # This is the store the change between months 

### opening CSV file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) #skip the headers 
    
### Iterating to append rows for summmary statistics
    for row in reader:
            revenue.append(float(row[1]))
            date.append(row[0]) 

### To get Change of month
for i in range(1, int(len(revenue))):
    change.append(revenue[i] - revenue[i-1])   
    avg_change = round(sum(change)/len(change),2)

    max_change = max(change)

    min_change = min(change)

    # Must add 1 to account for the first month not having a previous
    max_change_date = str(date[change.index(max(change)) + 1])
    min_change_date = str(date[change.index(min(change)) + 1])


### Printing Statements    
print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(len(date)))
print("Total: " + "$" + str(int(sum(revenue))))
print("Average Change" + "$" + str(avg_change))
print("Greatest Increase in Profits: " + str(max_change_date) + " " + "($"
    + str(int(max_change)) + ")")
print("Greatest Decrease in Profits: " + str(min_change_date) + " " + "($"
    + str(int(min_change)) + ")")


### Export to TXT File
txtlocation = os.path.join("analysis", "analysis.txt")

with open(txtlocation, "a") as txtfile:
    print("Financial Analysis", file = txtfile)
    print("--------------------------------", file = txtfile)
    print("Total Months: " + str(len(date)), file = txtfile)
    print("Total: " + "$" + str(int(sum(revenue))), file = txtfile)
    print("Average Change" + "$" + str(avg_change), file = txtfile)
    print("Greatest Increase in Profits: " + str(max_change_date) + " " + "($"
    + str(int(max_change)) + ")", file = txtfile)
    print("Greatest Decrease in Profits: " + str(min_change_date) + " " + "($"
    + str(int(min_change)) + ")", file = txtfile)
    txtfile.close()
    