import os
import csv

with open("election_data.csv") as bdfile:
    csvreader = csv.reader(bdfile, delimiter =",")
 
    csv_header = next(bdfile)
    
    #define rowcount variable, now add monthy_change
    rowcount = 0
    cand_list = []
    
   #calculate and print number of rows
    for row in csvreader:
        rowcount = rowcount +1
        cand_list.append(row[2])

#maybe call auxillary something else
auxiliaryList = []
for word in cand_list:
    if word not in auxiliaryList:
        auxiliaryList.append(word)
    
print(" ")
print("Election Results")
print("------------------------")
print(" ")
print("Total Votes: " +(str(rowcount)))   
print("------------------------",)

#print(auxiliaryList) this was to test

rounded_list = []

#add conversion to percantage, multiply by 100 and finally rounding, then get order of opertions correct
cand_one = (100 * ((int(cand_list.count(auxiliaryList[0]))) /rowcount))
rounded_C1 = round(cand_one,3)
rounded_list.append(rounded_C1)
print((auxiliaryList[0]) + ": " + ("{}%".format(rounded_C1)) + (" (") + (str(cand_list.count(auxiliaryList[0]))) + (")"))
print("")

cand_two = (100 * ((int(cand_list.count(auxiliaryList[1]))) /rowcount))
rounded_C2 = round(cand_two,3)
rounded_list.append(rounded_C2)
print((auxiliaryList[1]) + ": " + ("{}%".format(rounded_C2)) + (" (") + (str(cand_list.count(auxiliaryList[1]))) + (")"))
print("")
cand_three = (100 * ((int(cand_list.count(auxiliaryList[2]))) /rowcount))
rounded_C3 = round(cand_three,3)
rounded_list.append(rounded_C3)

print((auxiliaryList[2]) + ": " + ("{}%".format(rounded_C3)) + (" (") + (str(cand_list.count(auxiliaryList[2]))) + (")"))
cand_dict = {rounded_C1: (auxiliaryList[0]), rounded_C2: (auxiliaryList[1]), rounded_C3: (auxiliaryList[2])}

#added rounded list above then command to determine winner
winnerV = max(rounded_list)
#print(winnerV)
#print(f'{cand_dict[rounded_C1]}')
#test winnerV retrieval
#print(f'{cand_dict[winnerV]}')



print("")
print("------------------------")
print("")
# add winner line
print("Winner: " + (f'{cand_dict[winnerV]}'))
print("")
print("------------------------")

#(":") + (cand_list.count(auxiliaryList[0]))
#("{}%".format(rounded_C1))
#print(cand_list.count(auxiliaryList[0]))
#print(cand_list.count(auxiliaryList[1]))
#print(cand_list.count(auxiliaryList[2]))

#add comands to print to text commented out now that file has been created
#with open("pypoll.txt", "a") as f:
    #print(" ", file=f)
    #print("Election Results", file=f)
    #print("------------------------", file=f)
    #print(" ", file=f)
    #print("Total Votes: " +(str(rowcount)), file=f)   
    #print("------------------------", file=f)
    #print((auxiliaryList[0]) + ": " + ("{}%".format(rounded_C1)) + (" (") + (str(cand_list.count(auxiliaryList[0]))) + (")"),file=f)
    #print("", file=f)
    #print((auxiliaryList[1]) + ": " + ("{}%".format(rounded_C2)) + (" (") + (str(cand_list.count(auxiliaryList[1]))) + (")"), file=f)
    #print("", file=f)
    #print((auxiliaryList[2]) + ": " + ("{}%".format(rounded_C3)) + (" (") + (str(cand_list.count(auxiliaryList[2]))) + (")"), file=f)
    #print("", file=f)
    #print("------------------------", file=f)
    #print("", file=f)
    #print("Winner: " + (f'{cand_dict[winnerV]}'), file=f)
    #print("", file=f)
    #print("------------------------", file=f)
    
