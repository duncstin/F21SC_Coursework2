from user_input import UserInput
from task_manager import TaskManager
from Gui import Gui


def main():
    """Entry point. Gets user input, runs GUI or task manager depending on the input"""
    user_input = UserInput()
    if user_input.gui_flag:
        g = Gui(user_input.get_file(), user_input.get_docid(), user_input.get_userid())
        g.run()
    else:
        manager = TaskManager(user_input.get_file(), user_input.get_docid(), user_input.get_userid())
        task = user_input.task
        manager.run(task)

if __name__ == '__main__':
    main()

