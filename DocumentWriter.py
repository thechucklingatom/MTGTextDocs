def create_document_test(cards, set_name):
    document = open(set_name + ".txt", "w")
    for card in enumerate(cards):
        card_text = ""
        if card[1].name is not None:
            card_text += card[1].name + "\n"
        if card[1].mana_cost is not None:
            card_text += card[1].mana_cost + "\n"
        if card[1].power is not None:
            card_text += card[1].power + "\\" + card[1].toughness + "\n"
        if card[1].text is not None:
            card_text += card[1].text + "\n"
        if card[1].set is not None:
            card_text += card[1].set + "-" + card[1].rarity + "\n"
        card_text += "\n"
        document.write(card_text)
    document.close()
    print("done")
