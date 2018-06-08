def createDocumentTest(cards):
    document = open(cards[0].set + ".txt", "w")
    for card in cards:
        cardText = ""
        if card.name is not None:
            cardText += card.name + "\n"
        if card.mana_cost is not None:
            cardText += card.mana_cost + "\n"
        if card.power is not None:
            cardText += card.power + "\\" + card.toughness + "\n"
        if card.text is not None:
            cardText += card.text + "\n"
        if card.set is not None:
            cardText += card.set + "-" + card.rarity + "\n"
        cardText += "\n"
        document.write(cardText)
    document.close()
