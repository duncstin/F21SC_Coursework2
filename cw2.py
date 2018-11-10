from userinput import UserInput

def main():
    user_input = UserInput()
    print(user_input.user_id, user_input.doc_id, user_input.task, user_input.file)
    if user_input.doc_id == '':
        print("No doc id")

if __name__ == '__main__':
    main()
