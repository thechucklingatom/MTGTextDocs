from mtgsdk import Set
from mtgsdk import Card
import DocumentWriter


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

DocumentWriter.createDocumentTest()
