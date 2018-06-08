from mtgsdk import Set
from mtgsdk import Card
import DocumentWriter
import tkinter
import ttk

def name_list(setList):
    return_list = []
    for mtgSet in setList:
        return_list.append(mtgSet.name)
    return_list.sort()
    return return_list

class Application(tkinter.Frame):

    def __init__(self, master=tkinter.Tk()):
        master.geometry("500x500")
        tkinter.Frame.__init__(self, master, width=400, height=400)
        self.pack_propagate(0)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.setList = ttk.Combobox(self, textvariable="self", values=name_list(apiAccessor.getAllSets()))
        self.setList.pack()
        self.setList.grid()
        self.quitButton = tkinter.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid()

class ApiAccessor:

    def getAllSets(self):
        return Set.all()

    def getAllCardsForSet(self, name):
        return Card.where(set=name)


def main():
    print("test")


apiAccessor = ApiAccessor()
for mtgSet in apiAccessor.getAllSets():
    print(mtgSet.code)


print(len(apiAccessor.getAllCardsForSet("LEA").all()))

# DocumentWriter.createDocumentTest(apiAccessor.getAllCardsForSet("KTK").all())

app = Application()
app.master.title("Set document creator.")
app.mainloop()
