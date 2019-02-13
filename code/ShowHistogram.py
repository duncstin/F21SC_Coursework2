import matplotlib.pyplot as plt


class ShowHistogram:
    """Code taken from sample material provided for the Industrial Programming course at Heriot Watt Universitry:
    http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Samples/simple_histo.py"""

    def show_histo(self, dict, orient="horiz", label="counts", title="title"):
        if dict:
            """Take a dictionary of counts and show it as a histogram."""
            if orient == "horiz":
                bar_fun = plt.barh  # NB: this assigns a function to bar_fun!
                bar_ticks = plt.yticks
                bar_label = plt.xlabel
            elif orient == "vert":
                bar_fun = plt.bar
                bar_ticks = plt.xticks
                bar_label = plt.ylabel
            else:
                raise Exception("show_histo: Unknown orientation: %s ".format % orient)

            n = len(dict)
            bar_fun(range(n), list(dict.values()), align='center', alpha=0.4)
            bar_ticks(range(n), list(dict.keys()))  # NB: uses a higher-order function
            bar_label(label)
            plt.title(title)
            plt.show()
        else:
            print("No data to show")
