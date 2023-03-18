# to calculate average
import csv

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    average = []
    for row in spreadsheet:
        averages = int (row['sales'])
        average.append(averages)
    total_average = sum(average) / 12
    print('The average is £{:.2f}'.format(total_average))

#monthly changes as %
import csv

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    monthly_changes = []
    for row in spreadsheet:
        changes = int(row['sales'])
        monthly_changes.append(changes)
    increase = (monthly_changes [1] - monthly_changes [0]) / monthly_changes [0] *100
    print ('The monthly change is {:.2f}%'.format(increase))

#monthly changes as %
import csv

# This list below is just to make the printing nicer :)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    monthly_changes = []
    for row in spreadsheet:
        changes = int(row['sales'])
        monthly_changes.append(changes)

    # This for loop begins in index 0 (Jan) and ends in index 10 (Nov)
    # that is because I put the -1 to indicate that I want to stop at
    # idx 10 rather than 11
    for idx in range(len(monthly_changes)-1):
        diff = ((monthly_changes[idx+1] - monthly_changes [idx]) / monthly_changes [idx]) *100
        print('The monthly change b/w month {} and {} is {:.2f}%'.format(months[idx], months[idx+1], diff))