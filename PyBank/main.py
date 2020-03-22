#import data and create paths for sourcing data and outputting data
import os
import csv
csv_path = os.path.join("Resources", "budget_data.csv")
fin_analysis_ = os.path.join("output", "results.txt")
#declare variables
Totalmonths = 0
Totalprofl = 0
Maxprofl = 0.00
MaxMonth = ""
Minprofl = 0.00
MinMonth = ""
Revchange = 0.00
Previousprofl = 0.00
Averageprofl = 0.00
Proflchange = 0.00
Firstprofl= 0.00
#set empty variables for appending
date = []
profit = []
month = []
year = []
profitchange = []
SetCount= 0

#read in file and split data by comma character
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#skip headers
    next(csvreader,None)
    for row in csvreader:
        #SetCount = SetCount + 1
        #finding total months included in dataset
        Totalmonths += 1
        #finding net total amount of profit/losses over entire period
        Totalprofl += int(row[1])
         #running list of profit loss changes
        if (Totalmonths == 1):
            Firstprofl= int(row[1])
            Previousprofl= int(row[1])
        #Add previous month value and append data from row
        date.append(row[0])
        profit.append(int(row[1]))
        #update totals
        Finalprofl = int(row[1])
        profitchange.append(Proflchange)
        #Previousprofl = Finalprofl
            #finding average profit loss change
     #finding max increase in profit
        if int(row[1]) > Maxprofl:
            Maxprofl = int(row[1]) -Previousprofl
            MaxMonth = row[0]
        #finding max loss (minimum increase in profit)
        if int(row[1]) < Minprofl:
            Minprofl = int(row[1]) -Previousprofl
            MinMonth = row[0]
        if (Totalmonths > 1):
            Proflchange = int(row[1]) - Firstprofl
            Previousprofl = int(row[1])
            Averageprofl = Proflchange / (Totalmonths-1)
        #printing output results
    print("      ")
    print(" Financial Analysis")
    print("----------------------")
    print("Total Months:" + str(Totalmonths))
    print("Total: $" + str(Totalprofl))
    print("Average Change: $" + str(Averageprofl))
    print("Greatest Increase in Profits: $" + str(Maxprofl) + " in " + str(MaxMonth))
    print("Greatest Decrease in Profits: $" + str(Minprofl) + " in " + str(MinMonth))
    print("    ")
    #print("SetCount" + str(SetCount))
        # output results on textfile
    with open('fin_analysis_', "w") as txt_file:
        txt_file.write("Financial Analysis \n")
        txt_file.write("---------------------------- \n")
        txt_file.write("Total Months: " + str(Totalmonths) + " \n")
        txt_file.write("Total: $" + str(Totalprofl) + " \n")
        txt_file.write("Average Change: $" + str(Averageprofl) + " \n")
        txt_file.write("Greatest Increase in Profits: $" + str(Maxprofl) + " in " + str(MaxMonth) + " \n")
        txt_file.write("Greatest Decrease in Profits: $" + str(Minprofl) + " in " + str(MinMonth) + " \n")

