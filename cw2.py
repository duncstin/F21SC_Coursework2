from user_input import UserInput
from task_manager import TaskManager
from Gui import Gui


def main():
    user_input = UserInput()
    if user_input.gui_flag:
        g = Gui()
        g.run()
    else:
        print("UserInput:")
        print(user_input.user_id, user_input.doc_id, user_input.task, user_input.file)

        manager = TaskManager(user_input.get_file(), user_input.get_docid(), user_input.get_userid())
        task = user_input.task
        manager.run(task)

if __name__ == '__main__':
    main()
