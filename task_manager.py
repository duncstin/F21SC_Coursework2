import user_input
from show_histogram import ShowHistogram


class TaskManager:
    def __init__(self, u_input: user_input, dataframe):
        self.u_input = u_input
        self.dataset = dataframe


    def run(self):
        show_histo = ShowHistogram(self.dataset)
        if self.u_input.task == '2a':
            show_histo.show_from_table('country', self.u_input.doc_id)
        if self.u_input.task == '3a':
            show_histo.show_from_table('browser', self.u_input.doc_id)
