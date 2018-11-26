

def invert_dict(self, dictionary):
    """Inverts a dictionary of lists, where list values can be non unique"""
    inverted = {}
    for key, value in dictionary.items():
        for k in key:
            for v in value:
                if v in inverted:
                    inverted[v] = inverted[v].append(key)
                else:
                    inverted[v] = []
                    inverted[v].append(key)
                    print(inverted)
    return inverted