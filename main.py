from tkinter import *
import csv

#finds MPN value based on input, prints "value not found" if not on table

#ui = input("Input combination of positives:")

with open('MPN_table_update.csv') as f:
  for row in csv.reader(f):
    print(row)
    #if row[0] == ui:
      #print('MPN value is:' + row[1])
      #break
  #else:
  #  print('MPN value not found')  

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