from user_input import UserInput
from task_manager import TaskManager

def main():
    user_input = UserInput()
    if user_input.gui_flag:
        print('This would run a gui')
    else:
        print("UserInput:")
        print(user_input.user_id, user_input.doc_id, user_input.task, user_input.file)

        manager = TaskManager(user_input)

if __name__ == '__main__':
    main()
