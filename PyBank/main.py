# PyBank

# Importing necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join(".","Resources","budget_data.csv") # Input File Path
file_to_output = os.path.join(".","analysis","budget_analysis.txt") # Output File Path

# Initialize variables to track the budget data
total_months = 0
net_total_profit_loss = 0
row_value = 0
next_row_change = 0
changes_profit_loss = 0
sum_changes = 0
avg_profit_loss = 0

# Creating lists to store changes and their months
changes = []
months_changes = []

# Open the csv file
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheaders = next(csvreader) # Storing the headers
    
# Looping through given dataset
    for x in csvreader:
    
        if total_months == 0:
            row_value = int(x[1]) # Storing first dataset value
        else:
            months_changes.append(x[0]) # Adding months to months_changes[]
            next_row_value = int(x[1])
            changes_profit_loss = next_row_value - row_value
            changes.append(changes_profit_loss) # Adding values to changes[]
            
            row_value = next_row_value
        
        # Calculating total number of months
        total_months = total_months + 1
        # Calculating net total Profit/Loss
        net_total_profit_loss = net_total_profit_loss + int(x[1])
     
    # Calculating the total of changes
    sum_changes = sum(changes)
    # Calculating average of profit/loss changes
    avg_profit_loss = sum_changes/ (total_months -1)
    
    # Calculating greatest increase and greatest decrease values and their corresponding dates
    grt_increase_profits = max(changes)
    grt_increase_profits_date = changes.index(grt_increase_profits)
    grt_decrease_profits = min(changes)
    grt_decrease_profits_date = changes.index(grt_decrease_profits)
   
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("\nFinancial Analysis\n\n")
    txt_file.write("-"*20)
    txt_file.write(f"\n\nTotal Months: {total_months}\n\n")
    txt_file.write(f"Total: ${net_total_profit_loss}\n\n")
    txt_file.write(f"Average change: ${avg_profit_loss:.2f}\n\n")
    txt_file.write(f"Greatest Increase in Profits: {months_changes[grt_increase_profits_date]} (${grt_increase_profits})\n\n")
    txt_file.write(f"Greatest Decrease in Profits: {months_changes[grt_decrease_profits_date]} (${grt_decrease_profits})\n\n")

# Printing to terminal
    print("\nFinancial Analysis\n")
    print("-"*20)
    print(f"\nTotal Months: {total_months}\n")
    print(f"Total: ${net_total_profit_loss}\n")
    print(f"Average change: ${avg_profit_loss:.2f}\n")
    print(f"Greatest Increase in Profits: {months_changes[grt_increase_profits_date]} (${grt_increase_profits})\n")
    print(f"Greatest Decrease in Profits: {months_changes[grt_decrease_profits_date]} (${grt_decrease_profits})\n")
    
    # Resetting the variables so that the script run every time correctly
    total_months = 0
    net_total_profit_loss = 0
    row_value = 0
    next_row_change = 0
    changes_profit_loss = 0
    sum_changes = 0
    avg_profit_loss = 0
    changes = []
    months_changes = []

