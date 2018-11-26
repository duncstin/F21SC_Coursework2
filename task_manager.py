from HistoTasks import HistoTasks
from ShowHistogram import ShowHistogram
from AlsoLikes import AlsoLikes


class TaskManager:

    file = ''
    doc = ''
    user = ''

    def __init__(self, file, doc, user):
        self.file = file
        self.doc = doc
        self.user = user

    def run(self, task):
        if task == '1':
            t1 = HistoTasks(self.file)
            documents = t1.get_from_file("subject_doc_id")
            sort_descending = lambda x: sorted(x.items(), key=lambda k: k[1], reverse=True)
            print(sort_descending(documents)[:10])

        if task[0] == '2':
            t2 = HistoTasks(self.file)
            histo = ShowHistogram()
            countries = t2.get_from_file("visitor_country", self.doc)
            #131223153937-571db15b5caf3bb49c3ddc0591a759c7
            #sorted_docs = lambda x: sorted(x.items(), key=lambda k: k[1], reverse=True)
            #print(sorted_docs(countries)[:5])
            if task[1] == 'a':
                histo.show_histo(countries, "vert", "Country Code", "Views by country")
            else:
                continents = t2.get_continents(countries)
                histo.show_histo(continents, "vert", "Continents", "Views by continent")

        if task[0] == '3':
            t3 = HistoTasks(self.file)
            histo = ShowHistogram()
            browsers = t3.get_from_file("visitor_useragent", self.doc)
            if task[1] == 'a':
                histo.show_histo(browsers, "vert", "Browser", "Views by browser")
            else:
                short_browsers = t3.get_short_browser(browsers)
                histo.show_histo(short_browsers, "vert", "Browser", "Views by browser")

        if task[0] == '4':
            also_likes = AlsoLikes(self.file)
            result = also_likes.also_likes(self.doc, self.user)
            print('\n' + self.doc + '-->')
            for r in result:
                print("(" + str(len(r[1])) +": "+ r[0] + ")")


        if task[0] == '5':
            sort_descending = lambda x: sorted(x.items(), key=lambda k: k[1], reverse=True)
            also_likes_graph = AlsoLikes(self.file)
            also_likes_graph.also_likes_graph(self.doc, self.user)
