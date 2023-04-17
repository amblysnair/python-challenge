import os
import csv

csvpath = os.path.join('', 'Resource', 'budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    total_month = 0
    total_profit = 0
    profit_loss_array =[]
    avgchange = []
    changeinmonth=[]
    changeAmt = 0
    maxincrease = 0
    mindecrease = 0
    for row in csvreader:
        total_month += 1
        total_profit += int(row[1])
        profit_loss_array.append(int(row[1]))
        changeinmonth.append(str(row[0]))
    
    maxincrease = profit_loss_array[0]
    mindecrease = profit_loss_array[0]
    for i in range(len(profit_loss_array)-1):
       changeAmt +=  profit_loss_array[i+1] - profit_loss_array[i]
       avgchange.append(profit_loss_array[i+1] - profit_loss_array[i])
print(" \n Financial Analysis ")
print("\n-------------------------------")

print('\nTotal Months : ' +str(total_month))
print('\nTotal  : $' + str(total_profit))

print('\nAverage change : $' + str(round(changeAmt/85, 2)))

print(f'\nGreatest increase in profits : {changeinmonth[avgchange.index(max(avgchange))+1]} ($ {max(avgchange)})')
print(f'\nGreatest decrease in profits : {changeinmonth[avgchange.index(min(avgchange))+1]} ($ {min(avgchange)})\n')