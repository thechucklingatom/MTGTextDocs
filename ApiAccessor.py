from mtgsdk import Set
from mtgsdk import Card


class ApiAccessor:

    def getAllSets(self):
        return Set.all()

    def getAllCardsForSet(self, name):
        return Card.where(set=name)


def main():
    print("test")


apiAccessor = ApiAccessor()
for mtgSet in apiAccessor.getAllSets():
    print(mtgSet.name)


print(len(apiAccessor.getAllCardsForSet("LEA").all()))
