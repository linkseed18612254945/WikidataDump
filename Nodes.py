center = [['Q28865', 'Python', 'general-purpose, high-level programming language'], ['P1613', 'IRC channel', ['Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value'], ['irc://irc.freenode.net/python', 'irc://irc.freenode.net/python-dev', 'irc://irc.freenode.net/distutils', 'irc://irc.freenode.net/python.de', 'irc://irc.freenode.net/python-pt', 'irc://irc.freenode.net/python-fr', 'irc://irc.ircnet.net/python.fi', 'irc://irc.freenode.net/python-tr', 'irc://chat.freenode.net/pyar'], []], ['P646', 'Freebase ID', ['Value'], ['/m/05z1_'], []], ['P373', 'Commons category', ['Value'], ['Python (programming language)'], []], ['P306', 'operating system', ['Q174666'], ['cross-platform'], ['attribute conferred to computer software or computing methods and concepts that are implemented and inter-operate on multiple computer platforms']], ['P275', 'license', ['Q2600299'], ['Python Software Foundation License'], ['Software license of Python 2.0.1, 2.1.1, and newer versions']], ['P227', 'GND ID', ['Value'], ['4434275-5'], []], ['P571', 'inception', ['Value'], [{'before': 0, 'after': 0, 'timezone': 0, 'calendarmodel': 'http://www.wikidata.org/entity/Q1985727', 'precision': 9, 'time': '+1991-01-01T00:00:00Z'}], []], ['P178', 'developer', ['Q30942', 'Q83818'], ['Guido van Rossum', 'Python Software Foundation'], ['Dutch programmer and creator of Python', 'organization']], ['P135', 'movement', ['Q1076638'], ['free software movement'], ['social and political movement']], ['P31', 'instance of', ['Q899523', 'Q1268980', 'Q341', 'Q3839507', 'Q9143', 'Q187432'], ['object-oriented programming language', 'dynamic programming language', 'free software', 'functional programming language', 'programming language', 'scripting language'], ['programming paradigm', 'None', 'software for which certain user freedoms to use, copy, modify, redistribute it (including modified) exist', 'None', 'language designed to communicate instructions to a machine', 'programming language for special run-time environments']], ['P1482', 'Stack Exchange tag', ['Value'], ['http://stackoverflow.com/tags/python'], []], ['P2184', 'history of topic', ['Q4205080'], ['History of Python'], ['of the programming language']], ['P935', 'Commons gallery', ['Value'], ['Python (programming language)'], []], ['P287', 'designer', ['Q30942'], ['Guido van Rossum'], ['Dutch programmer and creator of Python']], ['P1401', 'bug tracking system', ['Value'], ['https://bugs.python.org/'], []], ['P856', 'official website', ['Value'], ['http://www.python.org'], []], ['P737', 'influenced by', ['Q2166735'], ['ALGOL 68'], ['programming language']], ['P244', 'LCAuth ID', ['Value'], ['sh96008834'], []], ['P154', 'logo image', ['Value'], ['Python logo and wordmark.svg'], []], ['P138', 'named after', ['Q16402'], ['Monty Python'], ['British surreal comedy group']], ['P348', 'software version', ['Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value'], ['2.7.6', '3.3.3', '3.3.4', '3.4.0', '3.4.1', '3.4.2', '3.4.3', '2.7.9', '2.7.10', '3.5.0', '3.5.1', '2.7.11'], []], ['P18', 'image', ['Value'], ['Python.png'], []], ['P910', "topic's main category", ['Q7136128'], ['Category:Python (programming language)'], ['Wikimedia category']], ['P1051', 'PSH ID', ['Value'], ['13861'], []]]


class Node:
    def __init__(self, node):
        self.node = node
        self.name = node[0][1]
        self.wiki_id = node[0][0]
        self.description = node[0][2]
        self.value = {}
        self.target = []

    def get_info(self):
        return [self.wiki_id, self.name, self.description]

    def get_value(self):
        for detail in self.node[1:]:
            if detail[2][0] == 'Value':
                self.value[detail[1]] = detail[3]
        return self.value

    def get_target(self):
        for detail in self.node[1:]:
            if detail[2][0] != 'Value':
                for i in range(len(detail[2])):
                    self.target.append([detail[1],detail[2][i], detail[3][i], detail[4][i]])
        return self.target

    def __str__(self):
        return self.get_info()[0] + ' ' + self.get_info()[1] + ' : ' + self.get_info()[2]

# DG.add_nodes_from([1, 2], time='2pm')
# DG.add_edge(1, 2, predicate_name='inspect', predicate_id='P122')


# nx.draw(G, node_color='yellow', node_size=300 ,node_shape='o', pot='circular_layout')
# plt.show()
