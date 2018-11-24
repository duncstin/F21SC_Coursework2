from HistoTasks import HistoTasks
from ShowHistogram import ShowHistogram

class TaskManager:

    file = ''
    doc = ''
    user = ''

    def __init__(self, u_input):
        self.file = u_input.get_file()
        self.doc = u_input.get_docid()
        self.user = u_input.get_userid()

    def run(self, task):
        if task[0] == '2':
            t2 = HistoTasks(self.file)
            histo = ShowHistogram()
            countries = t2.get_from_file("visitor_country", self.doc)
            if task[1] == 'a':
                histo.show_histo(countries, "vert", "Country Code", "Views by country")
            else:
                continents = t2.get_continents(countries)
                histo.show_histo(continents, "vert", "Country Code", "Views by country")

        if task[0] == '3':
            t3 = HistoTasks(self.file)
            histo = ShowHistogram()
            browsers = t3.get_from_file("visitor_useragent", self.doc)
            if task[1] == 'a':
                histo.show_histo(browsers, "vert", "Browser", "Views by browser")
