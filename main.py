import tkinter as tk
import sqlite3
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox

class Gui:
    labels = ('Times', 14)
    def __init__(self):
        self.commands = Commands()
        self.create_window()
        self.create_table()
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_filter()
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

    def create_table(self):
        '''Create inventory table'''
        # Create tree view for table
        self.inv_table = ttk.Treeview(self.root)
        # Create columns
        self.inv_table['columns'] = ('ID', 'Name', 'Batch Number', 'Weight', 'Date')
        # Format columns
        self.inv_table.column('#0', width=0, minwidth=0)
        self.inv_table.column('ID',width=40, minwidth=40)
        self.inv_table.column('Name',width=100, minwidth=100)
        self.inv_table.column('Batch Number',width=225, minwidth=225)
        self.inv_table.column('Weight',width=100, minwidth=100)
        self.inv_table.column('Date',width=100, minwidth=100)
        # Create headings (titles) to label each column
        self.inv_table.heading('#0', text='', anchor='w')
        self.inv_table.heading('ID', text='ID', anchor='w')
        self.inv_table.heading('Name', text='Base', anchor='w')
        self.inv_table.heading('Batch Number', text='Batch Number', anchor='w')
        self.inv_table.heading('Weight', text='Weight', anchor='w')
        self.inv_table.heading('Date', text='Date', anchor='w')
        self.inv_table.place(x=10, y=10, width=580, height=480)
        self.populate_table('None')
    
    def create_labels(self):
        self.batch = ttk.Label(self.root, text='Batch Number', font=Gui.labels)
        self.batch.place(x=15, y=500, width=150, height=30)
        self.weight = ttk.Label(self.root, text='Weight', font=Gui.labels)
        self.weight.place(x=360, y=500, width=80, height=30)
    
    def create_entries(self):
        self.batch_entry = ttk.Entry(self.root)
        self.batch_entry.place(x=150, y=500, width=200, height=30)
        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.place(x=430, y=500, width=100, height=30)

    def create_buttons(self):
        self.red_btn = ttk.Button(self.root, text='Red',
            command=lambda: self.add_base('red')
        ).place(x=15, y=535, width=105, height=30)

        self.blue_btn = ttk.Button(self.root, text = 'Blue',
            command=lambda: self.add_base('blue')
        ).place(x=130, y=535, width=105, height=30)

        self.yellow_btn = ttk.Button(self.root,text = 'Yellow',
            command=lambda: self.add_base('yellow')
        ).place(x=245, y=535, width=105, height=30)

        self.reflex_btn = ttk.Button(self.root, text='Reflex',
            command=lambda: self.add_base('reflex')
        ).place(x=360, y=535, width=105, height=30)

        self.violet_btn = ttk.Button(self.root, text='Violet',
            command=lambda: self.add_base('violet')
        ).place(x=475, y=535, width=105, height=30)

    def create_filter(self):
        self.options = ['Red','Red', 'Blue','Yellow','Reflex','Violet', 'None']
        
        self.selected = tk.StringVar(self.root)
        self.selected.set('')
        
        self.filter = ttk.OptionMenu(self.root, self.selected, *self.options)
        self.filter.place(x=15, y=565, width=250, height=25)
       
        self.filter_btn = ttk.Button(self.root, text='Filter',
            command=lambda: self.populate_table(self.selected.get())
        )
        self.filter_btn.place(x=275, y=565, width=75, height=25)

    def populate_table(self, filter):
        '''Load inventory data into the inventory list.'''
        # Loop through window and clear records
        for base in self.inv_table.get_children():
            self.inv_table.delete(base)
        if filter == 'None':
            # Load bases from database as a list
            base_inv = self.commands.load_bases()
        else:
            base_inv = self.commands.load_filtered(filter)
        # Loop through bases and add record to the inventory table
        for index, base in enumerate(base_inv):
            self.inv_table.insert(parent='', index='end', iid=index+1, text='',
                             values = base)
    
    def add_base(self, color):
        weight = ''
        date = datetime.now().strftime('%m-%d-%Y')
        try:
            weight = float(self.weight_entry.get())
            batch = self.batch_entry.get()
            self.commands.add_base(color,batch,weight,date)
            self.populate_table('None')
        except ValueError as e:
            messagebox.showerror(title='Wrong Format', message='Please enter a number')

class Commands:
    def __init__(self):
        self.database = 'bases.db'

    def connect(self):
        self.con = sqlite3.connect(self.database)
        self.cur = self.con.cursor()
    
    def disconnect(self):
        self.con.close()
    
    def load_bases(self):
        self.connect()
        sql = '''SELECT * FROM inventory'''
        data = self.cur.execute(sql).fetchall()
        self.disconnect()
        return data
    
    def add_base(self, color, batch, weight, date):
        self.connect()
        sql = '''INSERT INTO inventory(name, batch, weight, date) VALUES(?,?,?,?)'''
        self.cur.execute(sql, (color, batch, weight, date))
        self.con.commit()
        self.disconnect()
    
    def load_filtered(self, color):
        self.connect()
        sql = '''SELECT * from inventory WHERE name=?'''
        data = self.cur.execute(sql, (color,)).fetchall()
        self.disconnect()
        return data
    
if __name__ == '__main__':
    app = Gui()