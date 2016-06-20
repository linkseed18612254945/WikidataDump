import networkx as nx
import matplotlib.pyplot as plt
from Nodes import Node

center = [['Q28865', 'Python', 'general-purpose, high-level programming language'], ['P1613', 'IRC channel', ['Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value'], ['irc://irc.freenode.net/python', 'irc://irc.freenode.net/python-dev', 'irc://irc.freenode.net/distutils', 'irc://irc.freenode.net/python.de', 'irc://irc.freenode.net/python-pt', 'irc://irc.freenode.net/python-fr', 'irc://irc.ircnet.net/python.fi', 'irc://irc.freenode.net/python-tr', 'irc://chat.freenode.net/pyar'], []], ['P646', 'Freebase ID', ['Value'], ['/m/05z1_'], []], ['P373', 'Commons category', ['Value'], ['Python (programming language)'], []], ['P306', 'operating system', ['Q174666'], ['cross-platform'], ['attribute conferred to computer software or computing methods and concepts that are implemented and inter-operate on multiple computer platforms']], ['P275', 'license', ['Q2600299'], ['Python Software Foundation License'], ['Software license of Python 2.0.1, 2.1.1, and newer versions']], ['P227', 'GND ID', ['Value'], ['4434275-5'], []], ['P571', 'inception', ['Value'], [{'before': 0, 'after': 0, 'timezone': 0, 'calendarmodel': 'http://www.wikidata.org/entity/Q1985727', 'precision': 9, 'time': '+1991-01-01T00:00:00Z'}], []], ['P178', 'developer', ['Q30942', 'Q83818'], ['Guido van Rossum', 'Python Software Foundation'], ['Dutch programmer and creator of Python', 'organization']], ['P135', 'movement', ['Q1076638'], ['free software movement'], ['social and political movement']], ['P31', 'instance of', ['Q899523', 'Q1268980', 'Q341', 'Q3839507', 'Q9143', 'Q187432'], ['object-oriented programming language', 'dynamic programming language', 'free software', 'functional programming language', 'programming language', 'scripting language'], ['programming paradigm', 'None', 'software for which certain user freedoms to use, copy, modify, redistribute it (including modified) exist', 'None', 'language designed to communicate instructions to a machine', 'programming language for special run-time environments']], ['P1482', 'Stack Exchange tag', ['Value'], ['http://stackoverflow.com/tags/python'], []], ['P2184', 'history of topic', ['Q4205080'], ['History of Python'], ['of the programming language']], ['P935', 'Commons gallery', ['Value'], ['Python (programming language)'], []], ['P287', 'designer', ['Q30942'], ['Guido van Rossum'], ['Dutch programmer and creator of Python']], ['P1401', 'bug tracking system', ['Value'], ['https://bugs.python.org/'], []], ['P856', 'official website', ['Value'], ['http://www.python.org'], []], ['P737', 'influenced by', ['Q2166735'], ['ALGOL 68'], ['programming language']], ['P244', 'LCAuth ID', ['Value'], ['sh96008834'], []], ['P154', 'logo image', ['Value'], ['Python logo and wordmark.svg'], []], ['P138', 'named after', ['Q16402'], ['Monty Python'], ['British surreal comedy group']], ['P348', 'software version', ['Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value'], ['2.7.6', '3.3.3', '3.3.4', '3.4.0', '3.4.1', '3.4.2', '3.4.3', '2.7.9', '2.7.10', '3.5.0', '3.5.1', '2.7.11'], []], ['P18', 'image', ['Value'], ['Python.png'], []], ['P910', "topic's main category", ['Q7136128'], ['Category:Python (programming language)'], ['Wikimedia category']], ['P1051', 'PSH ID', ['Value'], ['13861'], []]]
a = Node(center)


class KG:
    def __init__(self, node=None):
        if node:
            self.DG = nx.DiGraph(center=node.name, center_id=node.wiki_id)
            self.add_node(node)
        else:
            self.DG = nx.DiGraph()

    def add_node(self, node):
        self.DG.add_node(node.wiki_id)
        new_node = self.DG.node[node.wiki_id]
        new_node['name'] = node.name
        new_node['description'] = node.description
        values = node.get_value()
        for i in values:
            new_node[i] = values[i]
        self.add_target(node)

    def add_target(self, node):
        for target in node.get_target():
            self.DG.add_node(target[1])
            the_node = self.DG.node[target[1]]
            the_node['name'] = target[2]
            the_node['description'] = target[3]
            self.DG.add_edge(node.wiki_id, target[1], predicate=target[0])

    def draw(self):
        nx.draw_networkx(self.DG, pos=nx.circular_layout(self.DG))
        plt.axis('off')
        plt.show()

    def __str__(self):
        nodes = ''
        for node in self.DG.nodes():
            nodes = nodes + node + ', '
        return nodes


c = KG(a)
c.draw()



# DG = nx.DiGraph(center=center[0][1])