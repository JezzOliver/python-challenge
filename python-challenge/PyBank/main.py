#import os and csv modules
import os
import csv

#set path for the file
#csvpath = os.path.join("..", "..", "Pybank", "Resources", "budget_data.csv")
#moved csv file to same folder couldnt get this to work

with open("budget_data.csv") as bdfile:
    csvreader = csv.reader(bdfile, delimiter =",")

    #comment
    csv_header = next(bdfile)

    #printed header for testing now commented out command
    #print(f"Header: {csv_header}") 
    
    #define rowcount variable, now add monthy_change
    rowcount = 0
    cumtotal = 0
    date_list = []
    total_list = []
    prev_mon_list = []
    prev_mon_list.append(0)
  
   #calculate and print number of rows
    for row in csvreader:
        rowcount = rowcount +1
        cumtotal += (int(row[1]))
        total_list.append(int(row[1]))
        prev_mon_list.append(int(row[1]))
        date_list.append(row[0])
                 
#print results in format requested
print("Financial Analysis")
print(" ")
print("---------------------")   
print("Total Months: " + str(rowcount))
print(" ")
print("Total: $" + str(cumtotal))

#commented out as just for testing
#print(total_list)
#print(date_list)
#print(prev_mon_list)

diff_list = []
diff_date = []
budgetout_csv = zip(date_list, total_list, prev_mon_list)

#initially thought I need to ouptput csv but didnt so its now commented out
#output_file = os.path.join("bd_out.csv")

#join("bd_final.csv")
#with open(output_file, "w") as datafile:
    #writer = csv.writer(datafile)

    #writer.writerow(["Month", "Total", "Previous"])
    #writer.writerows(budgetout_csv)

#create lists to help obtain difference 
for row in budgetout_csv:
    diff = (int(row[1])-(int(row[2])))
    diff_list.append(diff)
    diff_date.append(row[0])

    #testing only        
    #print(diff)
    #python main.pyprint(row)

#print(diff_list)

#get rid of row 1
diff_list.pop(0)
diff_date.pop(0)

#determine and print average,min,max
avg_diff = sum(diff_list)/len(diff_list)
print(" ")
print("Avergae Change: $", round(avg_diff,2))
print(" ")
max_diff = max(diff_list)
min_diff = min(diff_list)

#testing purposes only
#print(diff_list[78])
#print(diff_list[48])

print("Greatest Increase in Profits: " + (str(diff_date[78])) + " (" + (str(max_diff)) + ")")
print("")
print("Greatest Increase in Profits: " + (str(diff_date[48])) + " (" + (str(min_diff)) + ")")

#testing purposes only
#print(max_diff)
#print(min_diff)

#create text file

with open("pybank.txt", "a") as f:
    print("Financial Analysis", file=f)
    print(" ", file=f)
    print("---------------------", file=f)   
    print("Total Months: " + str(rowcount), file=f)
    print(" ", file=f)
    print("Total: $" + str(cumtotal), file=f)
    print(" ", file=f)
    print("Avergae Change: $", round(avg_diff,2), file=f)
    print("Greatest Increase in Profits: " + (str(diff_date[78])) + " (" + (str(max_diff)) + ")", file=f)
    print(" ", file=f)
    print("", file=f)
    print("Greatest Increase in Profits: " + (str(diff_date[48])) + " (" + (str(min_diff)) + ")", file=f)
