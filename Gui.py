from tkinter import *

class Gui:
    buttons = '2a', '2b', '3a', '3b', '4d', '5'
    fields = 'File: ', 'Reader Id:', 'Document Id:'
    """https://www.python-course.eu/tkinter_entry_widgets.php"""

    def __init__(self):
        task_selector = Tk()
        task_selector.resizable(False, False)
        self.make_text_entry(task_selector)
        self.make_buttons(task_selector)
        task_selector.title("Issuu Document Tracker Data Processing")

    def make_text_entry(self, root):
        for field in self.fields:
            row = Frame(root)
            lab = Label(row, width=12, text=field, anchor='w')
            ent = Entry(row, width=50)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)

    def make_buttons(self, root):
        for button in self.buttons:
            button = Button(root, text=button, width=5, command=lambda b=button: self.start_task_manager(b))
            button.pack(side=LEFT, padx=5, pady=5)

    def run(self):
        mainloop()

    def start_task_manager(self, task):
        print(task)
