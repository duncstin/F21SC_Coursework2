from user_input import UserInput
from task_manager import TaskManager
from file_input import FileInput

def main():
    user_input = UserInput()
    file_input = FileInput(user_input.file)
    print(file_input.df)



    if user_input.gui_flag:
        print('This would run a gui')
    else:
        print("UserInput:")
        print(user_input.user_id, user_input.doc_id, user_input.task, user_input.file)

        manager = TaskManager(user_input, file_input.df)
        manager.run()

if __name__ == '__main__':
    main()
