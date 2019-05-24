import csv

keys = ['Combination of Positives', 'MPN INdex/100mL', 'Confidence Limit LOW', 'Confidence Limit HIGH']

with open ('MPN_table.csv') as f:
  reader = csv.reader(f)
  fixed_table =[]
  for row in reader: 
    row = [item for item in row if item != '']
    new_row = [item for item in row[0:4]]
    fixed_table.append(new_row)
    new_row = [item for item in row[4:]] 
    fixed_table.append(new_row)
    sorted_table = sorted([row for row in fixed_table], key = lambda x: x[0])
  print(sorted_table)

with open ('MPN_table_update.csv', 'w', newline = '') as f:
  writer = csv.writer(f)
  writer.writerow(keys)
  for row in sorted_table:
    writer.writerow(row)



