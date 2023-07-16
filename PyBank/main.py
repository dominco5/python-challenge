# import necessary modules
import os
import csv

# create variables
total_months = 0
total = 0
total_change = 0

# reference file being read
csvpath = os.path.join("Resources", "budget_data.csv")

# Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #store header and first row
    header = next(csvreader)
    firstrow = next(csvreader)

    # create variables and assign those needing values from firstrow
    total_months = 1
    total = int(firstrow[1])
    previous_pl = int(firstrow[1])
    total_change = 0
    greatest_increase = int(firstrow[1])
    greatest_decrease = int(firstrow[1])
    month_greatest_increase = firstrow[0]
    month_greatest_decrease = firstrow[0]

    # read through rest of csv file
    for row in csvreader:
        # month counter
        total_months += 1

        # net total P&L
        total += int(row[1])

        # find change from previous row
        difference = int(row[1]) - previous_pl

        # add to total change
        total_change += difference
        
        # find greatest increase/decrease and respective months
        if difference > greatest_increase:
            greatest_increase = difference
            month_greatest_increase = row[0]
        elif difference < greatest_decrease:
            greatest_decrease = difference
            month_greatest_decrease = row[0]
        
        # reassign previous P&L for next iteration
        previous_pl = int(row[1])

    # calculate average change
    average_change = total_change / total_months

# print analysis of data
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})")

# define filepath for output text file
output_path = os.path.join("analysis", "budget_data_analysis.txt")

# open in write mode
with open(output_path, 'w') as f:

    # write
    f.write(f"Financial Analysis")
    f.write('\n')
    f.write(f"----------------------------")
    f.write('\n')
    f.write(f"Total Months: {total_months}")
    f.write('\n')
    f.write(f"Total: ${total}")
    f.write('\n')
    f.write(f"Average Change: ${round(average_change, 2)}")
    f.write('\n')
    f.write(f"Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})")
    f.write('\n')
    f.write(f"Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})")
    


