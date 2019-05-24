import csv
from tkinter import *


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
  print(fixed_table)

with open ('MPN_table_update.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(keys)
  for row in fixed_table:
    writer.writerow(row)




#finds MPN value based on input, prints "value not found" if not on table

#ui = input("Input combination of positives:")
#with open('MPN-table.csv') as f:
#  for row in csv.reader(f):
#    if row[0] == ui:
#      print('MPN value is:' + row[1])
#      break
#  else:
#    print('MPN value not found')  




#class Window(Frame):
#  def __init__(self, master=None):
#    Frame.__init__(self, master)
#    self.master = master
#    self.init_window()
#
#  def init_window(self):
#    self.master.title("MPN Generator")
#    self.pack(fill = BOTH, expand = 1)
#      
#    menu = Menu(self.master)
#    self.master.config(menu = menu)
#    
#    file = Menu(menu)
#    file.add_command(label = 'Exit', command = self.client_exit)
#    menu.add_cascade(label = 'File', menu = file)
#    
#    edit = Menu(menu)
#    edit.add_command(label ='Undo')
#    menu.add_cascade(label = 'Edit', menu = edit)




 # def client_exit(self):
 #   exit()


#root = Tk()
#root.geometry("400x300")
#app = Window(root)

#root.mainloop()
