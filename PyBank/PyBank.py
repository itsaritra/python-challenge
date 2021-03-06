import os
import csv

budget_dataCSV = os.path.join('..', 'budget_data.csv')

with open(budget_dataCSV, 'r') as budgetdatafile:
    csvreader = csv.reader(budgetdatafile, delimiter=',')

    csv_header = next(budgetdatafile)
    total = 0
    months_count = 0
    increase_profit = 0
    decrease_profit = 0
    initial_value = 0
    for row in csv.reader(budgetdatafile):
        amount = row[1]
        months = row[0]
        total += int(row[1])
        months_count +=1
        diff = int(amount) - initial_value

        if increase_profit < diff:
            increase_profit = diff
            profit_increase_month = months

        if decrease_profit > diff:
            decrease_profit = diff
            profit_decrease_month = months
with open("Output.txt", "w") as text_file:

    print(f'Financial analysis', file=text_file)
    print(f'------------------', file=text_file)
    print(f'Total: ${total}', file=text_file)

    print(f'Total months: {months_count}', file=text_file)
    print(f'Greatest increase in profit: ${increase_profit}, {profit_increase_month}', file=text_file)
    print(f'Greatest decrease in profit: ${decrease_profit}, {profit_decrease_month}', file=text_file)

    