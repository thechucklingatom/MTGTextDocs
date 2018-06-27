from mtgsdk import Set
from mtgsdk import Card
import DocumentWriter
import tkinter
import ttk


class ApiAccessor:

    @staticmethod
    def get_all_sets():
        return Set.all()

    @staticmethod
    def get_all_cards_for_set(name):
        if name is '':
            return [None]
        return Card.where(set=name)


apiAccessor = ApiAccessor()


def name_list(set_list):
    return_list = []
    for mtgSet in set_list:
        return_list.append(mtgSet.name)
    return_list.sort()
    return return_list


class Application(tkinter.Frame):

    def __init__(self, master=tkinter.Tk()):
        master.geometry("500x500")
        tkinter.Frame.__init__(self, master, width=400, height=400)
        self.pack_propagate(0)
        self.grid()
        self.set_list = ttk.Combobox(self, textvariable="self", values=name_list(apiAccessor.get_all_sets()))
        self.set_list.pack()
        self.set_list.grid()
        self.quit_button = tkinter.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid()
        self.create_button = tkinter.Button(self, text="Create document", command=self.create_document())
        self.create_button.grid()

    def create_document(self):
        api_accessor = ApiAccessor()
        DocumentWriter.create_document_test(api_accessor.get_all_cards_for_set(self.set_list.get()).all())


app = Application()
app.master.title("Set document creator.")
app.mainloop()
