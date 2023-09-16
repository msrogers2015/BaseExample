import tkinter as tk
from tkinter import ttk
import sqlite3

class Gui:
    def __init__(self):
        self.create_window()
        self.create_table()
        self.create_entries()
        self.create_buttons()
        self.root.mainloop()

    def create_window(self):
        '''Create GUI base window for user to interact with.'''
        # Create window
        self.root = tk.Tk()
        # Update Title
        self.root.title('Base Inventory')
        # Set window size variables
        self.width = 600
        self.height = 600
        # Set window location variables to center window in screen
        self.x = int(self.root.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(self.root.winfo_screenheight() / 2 - self.height / 2)
        # Update size and placement of window
        self.root.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        # Create inventory frame
        self.inv_frame = ttk.Frame(self.root).place(x=5, y=5, width=590, height=495)
        # Create user input frame
        self.user_frame = ttk.Frame(self.root).place(x=5, y=505, width=590, height=90)

    def create_table(self):
        '''Create inventory table'''
        # Create tree view for table
        self.inv_table = ttk.Treeview(self.inv_frame)
        # Create columns
        self.inv_table['columns'] = ('ID', 'Name', 'Description', 'Weight', 'Date')
        # Format columns
        self.inv_table.column('#0', width=0, minwidth=0)
        self.inv_table.column('ID',width=40, minwidth=40)
        self.inv_table.column('NAme',width=100, minwidth=100)
        self.inv_table.column('Description',width=250, minwidth=250)
        self.inv_table.column('Weight',width=100, minwidth=100)
        self.inv_table.column('Date',width=100, minwidth=100)
        # Create headings (titles) to label each column
        self.inv_table.heading('#0', text='', anchor='w')
        self.inv_table.heading('ID', text='ID', anchor='w')
        self.inv_table.heading('Name', text='Base', anchor='w')
        self.inv_table.heading('Description', text='Description', anchor='w')
        self.inv_table.heading('Weight', text='Weight', anchor='w')
        self.inv_table.heading('Date', text='Date', anchor='w')
        # Place table
        self.inv_table.pack(fill=True)
    
    def populate_table(self):
        '''Load inventory data into the inventory list.'''
        # Loop through window and clear records
        for base in self.inv_table.get_children():
            self.inv_table.delete(base)
        # Load bases from database as a list
        base_inv = ''
        # Loop through bases and add record to the inventory table
        for index, base in enumerate(base_inv):
            self.tree.insert(parent='', index='end', iid=index+1, text='',
                             values = base)

