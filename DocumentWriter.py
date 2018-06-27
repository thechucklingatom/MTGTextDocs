def create_document_test(cards):
    if cards is None:
        return
    document = open(cards[0].set + ".txt", "w")
    for card in cards:
        card_text = ""
        if card.name is not None:
            card_text += card.name + "\n"
        if card.mana_cost is not None:
            card_text += card.mana_cost + "\n"
        if card.power is not None:
            card_text += card.power + "\\" + card.toughness + "\n"
        if card.text is not None:
            card_text += card.text + "\n"
        if card.set is not None:
            card_text += card.set + "-" + card.rarity + "\n"
        card_text += "\n"
        document.write(card_text)
    document.close()
