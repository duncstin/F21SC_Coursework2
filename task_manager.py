from HistoTasks import HistoTasks
from ShowHistogram import ShowHistogram
from AlsoLikes import AlsoLikes1
from ALGraph import ShowDigraph
from decorator import timer


class TaskManager:
    """Class that links commandline/GUI input to underlying business logic"""

    file = ''
    doc = ''
    user = ''

    def __init__(self, file, doc, user):
        self.file = file
        self.doc = doc
        self.user = user

    def run(self, task):
        """Runs appropriate user specified task"""
        try:
            if task == '1':
                self.task1()

            if task[0] == '2':
                if task[1] == 'a':
                    self.task2()
                else:
                    self.task2(True)

            if task[0] == '3':
                if task[1] == 'a':
                    self.task3()
                else:
                    self.task3(True)

            if task[0] == '4':
                if task[1] == 'd':
                    self.task4()
                else:
                    self.task4(False)

            if task[0] == '5':
                self.task5()
        except FileNotFoundError:
            print("Please enter a valid file")
    @timer
    def task1(self):
        """Task 1 added simply to help find cases to test on, shows top 10 most read documents.
        Task is derived from quickly re-purposing other elements of code. As such, the sort function is just a quick
        copy paste, rather than being fully implemented."""
        t1 = HistoTasks(self.file)
        documents = t1.get_from_file("subject_doc_id")
        print(self.sort_descending(documents)[:10])

    def sort_descending(self, x):
        """Sorts dictionary by value, returning dict as list of tuples, highest first."""
        return sorted(x.items(), key=lambda k: k[1], reverse=True)


    def task2(self, extend=False):
        """Shows countries by default. If extend == True, will extend the task to include method for processing
        countries to continents"""
        t2 = HistoTasks(self.file)
        histo = ShowHistogram()
        countries = t2.get_from_file("visitor_country", self.doc)
        if extend:
            continents = t2.get_continents(countries)
            histo.show_histo(continents, "vert", "Continents", "Views by continent")
        else:
            histo.show_histo(countries, "vert", "Country Code", "Views by country")

    def task3(self, extend=False):
        """Shows views by browser. Will extend to task 3b if flag is true, calling method to process the verbose browser
        strings to just the key identifiers"""
        t3 = HistoTasks(self.file)
        histo = ShowHistogram()
        browsers = t3.get_from_file("visitor_useragent", self.doc)
        if extend:
            short_browsers = t3.get_short_browser(browsers)
            histo.show_histo(short_browsers, "vert", "Browser", "Views by browser")
        else:
            histo.show_histo(browsers, "vert", "Browser", "Views by browser")
    @timer
    def task4(self, show_counts=True):
        """Gets also like list of top 10 readers. By default, shows doc ID & count of readers.
        If show_contents is false, will display full reader strings. This is mainly used for debugging or testing"""
        also_likes = AlsoLikes1(self.file)
        result = also_likes.also_likes(self.doc)
        if result:
            print('\n' + self.doc + '-->')
            if show_counts: # show doc id with counts for readers
                for r in result:
                    print("(" + str(len(r[1])) + ": " + r[0] + ")")
            else: # show doc id and ALL associated reader ids
                for r in result:
                    print(r)
        else:  # if no readers, or readers haven't read any other documents
            print('There are no "also likes" documents in the current data')

    @timer
    def task5(self):
        """Displays 'also likes' graph for top 10 documents (excluding input doc)"""
        also_likes = AlsoLikes1(self.file)
        graph = ShowDigraph(self.file)
        result = also_likes.also_likes(self.doc, self.user)
        self.user = also_likes.user
        graph.also_likes_graph(result, self.doc, self.user)


