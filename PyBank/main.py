
import os
import csv

## Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

## Reading file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    
    ## Delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    ## Reading Header...
    csv_header = next(csvreader)
    row = next(csvreader)
    
    ## Calculating variables...
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    ## Reading after header...
    for row in csvreader:
        
        ## Getting Number Of Months
        total_months += 1
        ## Getting Net Amount Of "Profit/Losses"
        net_amount += int(row[1])

        ## Getting Monthly Change
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        ## Getting Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        ## Getting Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    ## Getting Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

## Printing Results
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

## Exporting a text file
output_file = os.path.join("..", "PyBank", "analysis", "Results.text")

with open(output_file, 'w',) as txtfile:

## Writing results
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
