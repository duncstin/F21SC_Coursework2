from tkinter import *
from task_manager import TaskManager

class Gui:
    buttons = '1', '2a', '2b', '3a', '3b', '4d', '5'
    fields = 'File: ', 'Reader Id:', 'Document Id:'
    """https://www.python-course.eu/tkinter_entry_widgets.php"""
    text_input = ''

    def __init__(self, file='', doc='', user=''):
        task_selector = Tk()
        task_selector.resizable(False, False)
        self.text_input = self.make_text_entry(task_selector)
        self.make_buttons(task_selector)
        task_selector.title("Issuu Document Tracker Data Processing")
        # if any input has been specified by the user, inputs it
        self.text_input[0].insert(0, file)
        self.text_input[1].insert(0, user)
        self.text_input[2].insert(0, doc)


    def make_text_entry(self, root):
        """loops over Fields, creating label and text box for each. Returns a list allowing them to be accessed"""
        text_fields = []
        for field in self.fields:
            row = Frame(root)
            lab = Label(row, width=12, text=field, anchor='w')
            ent = Entry(row, width=50)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            text_fields.append(ent)
        return text_fields

    def make_buttons(self, root):
        """Loops over buttons, creatinga button for each"""
        for button in self.buttons:
            button = Button(root, text=button, width=5, command=lambda b=button: self.start_task_manager(b))
            # https://stackoverflow.com/questions/1539787/determine-which-button-was-pressed-in-tkinter
            button.pack(side=LEFT, padx=5, pady=5)

    def run(self):
        """Displays GUI"""
        mainloop()

    def start_task_manager(self, task):
        """Takes information from GUI, instantiates a task manager, and runs appropriate task"""
        file = self.text_input[0].get()
        print("file " + file)
        user = self.text_input[1].get()
        print("user " + user)
        doc = self.text_input[2].get()
        print("doc " + doc)
        manager = TaskManager(file, doc, user)
        manager.run(task)

