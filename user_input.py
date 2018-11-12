import sys
import getopt


class UserInput:
    """Creates object container user input variables"""

    user_id = ''
    doc_id = ''
    task = ''
    file = ''
    gui_flag = False

    def __init__(self):
        self.get_input()
        if self.gui_flag == False:
            self.validate_task_requirements()

    def get_input(self):
        """Gets user input from commandline"""
        # first argument ignored as it is name of python file
        argv = sys.argv[1:]
        try:
            options, remainder = getopt.getopt(argv, 'hu:d:t:f:', ['help'])
            # print(len(options), len(remainder))
        except getopt.GetoptError:
            UserInput.usage(self)

        if len(options) == 0 and len(remainder) == 0:
            self.gui_flag = True
        elif len(remainder) > 0:
            UserInput.usage(self)
        else:
            for opt, arg in options:
                if opt in ('-h', '--help'):
                    UserInput.usage(self, True)
                    sys.exit(0)
                elif opt == '-u':
                    self.user_id = arg
                elif opt == '-d':
                    self.doc_id = arg
                elif opt == '-t':
                    self.task = arg
                elif opt == '-f':
                    self.file = arg



    def usage(self, fullexplain=False):
        """Prints message about usage. If called with 'True', will print expanded usage info"""
        message = '\nUsage: user_input.py -u <user_uuid> -d <doc_id> -t <task> -f <filename>\n'
        expanded = """    <user_uuid>: a 16 character hash representing a unique user
        
        <doc_id>: a unique hash representing a document that that can be read by users
        
        <task_id>: selects tasks to display results of. Recognised tasks are:
            2a - histogram of views per country 
            2b - histogram of views per continent 
            3a - histogram of views by full browser identifier 
            3b - histogram of views by main browser name
            4d - list of top 10 "also like" documents
            5 -  "also like" graph
            
        file_name: path to file containing data"""
        print(message)
        if fullexplain:
            print(expanded)
        sys.exit(0)

    def validate_task_requirements(self):
        print("Task Id:" + self.task)
        if self.task in ('2a', '2b', '3a', '3b'):
            if len(self.doc_id) != 45:
                print("Expected doc_id string of size 45 for task %s" % self.task)
                sys.exit(1)
        elif self.task in ('4d', '5'):
            print('Validation still required')
        else:
            print('Invalid task specified')
            UserInput.usage(self, True)


