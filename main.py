import csv


#finds MPN value based on input, prints "value not found" if not on table

ui = input("Input combination of positives:")
with open('MPN-table.csv') as f:
  for row in csv.reader(f):
    if row[0] == ui:
      print('MPN value is:' + row[1])
      break
  else:
    print('MPN value not found')  
