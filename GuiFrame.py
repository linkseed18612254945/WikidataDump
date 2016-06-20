from tkinter import *
from tkinter import ttk
from JsonParsing import JsonParse
# import Network


# 基础界面参数
AUTHOR = 'Kun Li'
VERSION = '1.00'
TITLE = 'WikiDataDump'+'     Ver ' + VERSION
KEYWORD_API = 'https://www.wikidata.org/w/api.php?action=wbsearchentities'
ID_API = 'https://www.wikidata.org/w/api.php?action=wbgetentities'


class WikiDataDump:
    def __init__(self, master):
        self.master = master
        self.mainframe = ttk.Frame(self.master)
        self.search_box = ttk.Notebook(self.mainframe)
        self.search_frame = ttk.Frame(self.search_box, padding=(5, 5))
        self.inquire_frame = ttk.Frame(self.search_box, padding=(5, 5))
        self.search_box.add(self.search_frame, text='KeyWord Search')
        self.search_box.add(self.inquire_frame, text='ID Search')
        self.output_frame = ttk.Frame(self.mainframe)
        self.show_frame = ttk.Frame(self.mainframe)
        self.output_box = ttk.Treeview(self.output_frame, height=12, show='headings',
                                       columns=('ID', 'Label', 'Description'))
        self.show_box = ttk.Treeview(self.show_frame, height=14, show='headings',
                                     columns=('P_ID', 'Predicate', 'O_ID', 'Object'))
        self.grid_frame()
        self.create_inquire()
        self.create_search()
        self.create_output()
        self.create_show()
        self.entity_ids = []
        self.detail_ids = []

    def grid_frame(self):
        self.mainframe.grid()
        self.search_box.grid(column=0, row=0, columnspan=1, sticky=(N, S, E, W))
        self.output_frame.grid(column=1, row=0, sticky=(N, S, E, W))
        self.show_frame.grid(column=0, row=1, columnspan=2, sticky=(N, S, W, E))

    def create_search(self):
        search_label = ttk.Label(self.search_frame, text='Search')
        search_label.grid(column=0, row=0, columnspan=2, pady=30)
        keyword_label = ttk.Label(self.search_frame, text='Keyword')
        keyword_label.grid(column=0, row=1, padx=20)
        keyword = StringVar()
        keyword_input = ttk.Entry(self.search_frame, width=15, textvariable=keyword)
        keyword_input.grid(column=1, row=1)
        format_label = ttk.Label(self.search_frame, text='Format')
        format_label.grid(column=0, row=2, rowspan=2, pady=50)
        source_format = StringVar()
        source_format.set('json')
        json_radio = ttk.Radiobutton(self.search_frame, text='json', variable=source_format, value='json')
        xml_radio = ttk.Radiobutton(self.search_frame, text='xml', variable=source_format, value='xml')
        json_radio.grid(column=1, row=2, sticky=(S, W))
        xml_radio.grid(column=1, row=3, sticky=(N, W))
        search_button = ttk.Button(self.search_frame, text='Search', command=lambda: self.search(keyword, source_format))
        search_button.grid(column=0, row=4, columnspan=2)

    def create_inquire(self):
        inquire_label = ttk.Label(self.inquire_frame, text='Inquire')
        inquire_label.grid(column=0, row=0, columnspan=2, pady=30)
        id_label = ttk.Label(self.inquire_frame, text='ID')
        id_label.grid(column=0, row=1, padx=20)
        id_num = StringVar()
        id_input = ttk.Entry(self.inquire_frame, width=15, textvariable=id_num)
        id_input.grid(column=1, row=1)
        inquire_button = ttk.Button(self.inquire_frame, text='Inquire', command=lambda: self.inquire(id_num))
        inquire_button.grid(column=1, row=3, columnspan=1, sticky=(S, W, N, E), pady=50)

    def create_output(self):
        self.output_box.column('ID', width=80, anchor='center')
        self.output_box.column('Label', width=120, anchor='center')
        self.output_box.column('Description', width=330, anchor='center')
        self.output_box.heading('ID', text='ID')
        self.output_box.heading('Label', text='Label')
        self.output_box.heading('Description', text='Description')
        self.output_box.grid(column=0, row=0, sticky=(N, S, E, W))
        output_box_ybar = ttk.Scrollbar(self.output_frame, orient=VERTICAL, command=self.output_box.yview)
        output_box_xbar = ttk.Scrollbar(self.output_frame, orient=HORIZONTAL, command=self.output_box.xview)
        self.output_box.configure(yscrollcommand=output_box_ybar.set)
        self.output_box.configure(xscrollcommand=output_box_xbar.set)
        output_box_ybar.grid(column=1, row=0, sticky=(N, S))
        output_box_xbar.grid(column=0, row=1, sticky=(E, W))

    def create_show(self):
        self.show_box.column('P_ID', width=100, anchor='center')
        self.show_box.column('Predicate', width=170, anchor='center')
        self.show_box.column('O_ID', width=100, anchor='center')
        self.show_box.column('Object', width=400, anchor='center')
        self.show_box.heading('P_ID', text='P_ID')
        self.show_box.heading('Predicate', text='Predicate')
        self.show_box.heading('O_ID', text='O_ID')
        self.show_box.heading('Object', text='Object')
        self.show_box.grid(column=0, row=0, columnspan=1, sticky=(N, S, E, W))
        show_box_ybar = ttk.Scrollbar(self.show_frame, orient=VERTICAL, command=self.show_box.yview)
        show_box_xbar = ttk.Scrollbar(self.show_frame, orient=HORIZONTAL, command=self.show_box.xview)
        self.show_box.configure(yscrollcommand=show_box_ybar.set)
        self.show_box.configure(xscrollcommand=show_box_xbar.set)
        show_box_ybar.grid(column=1, row=0, sticky=(N, S))
        show_box_xbar.grid(column=0, row=1, sticky=(E, W))

    def search(self, keyword, source_format):
        key = keyword.get()
        if key == '':
            return
        if ' ' in key:
            key = key.replace(' ', '%20')
        source_format = source_format
        url = KEYWORD_API + '&search=' + key + '&format=' + source_format.get() + '&language=en'
        entities_json = JsonParse(url)
        entities = entities_json.get_entities()
        self.insert_output(entities)

    def inquire(self, id_num):
        flag = True
        if isinstance(id_num, str):
            flag = False
            inquire_id = id_num
        else:
            if id_num.get()[0].isdigit():
                inquire_id = 'Q' + id_num.get()
            elif id_num.get()[0].upper() == 'P' or id_num.get()[0].upper() == 'Q':
                inquire_id = id_num.get().upper()
            else:
                return
        url = ID_API + '&ids=' + inquire_id + '&format=json&languages=en'
        entity_json = JsonParse(url)
        details = entity_json.get_detail()
        info = details[0]
        if flag:
            self.insert_output([info])
        self.insert_show(details[1:])

    def insert_output(self, entities_json):
        if self.entity_ids:
            for i in self.entity_ids:
                self.output_box.delete(i)
            self.entity_ids = []
        for entity in entities_json:
            entity_num = self.output_box.insert('', 0, tags=('double_click'), values=(entity[0], entity[1], entity[2]))
            self.entity_ids.append(entity_num)
        self.output_box.bind("<Double-1>", self.double_click)

    def insert_show(self, detail_json):
        if self.detail_ids:
            for i in self.detail_ids:
                self.show_box.delete(i)
            self.detail_ids = []
        for detail in detail_json:
            for i in range(len(detail[2])):
                if i == len(detail[2]) - 1:
                    detail_num = self.show_box.insert('', 0, values=(detail[0], detail[1], detail[2][i], detail[3][i]))
                else:
                    detail_num = self.show_box.insert('', 0, values=(' ', ' ', detail[2][i], detail[3][i]))
                self.detail_ids.append(detail_num)

    def double_click(self, event):
        item = self.output_box.selection()[0]
        entity_id = self.output_box.item(item,'values')[0]
        self.inquire(entity_id)


def main():
    root = Tk()
    root.title(TITLE)
    WikiDataDump(root)
    root.mainloop()

if __name__ == '__main__':
    main()