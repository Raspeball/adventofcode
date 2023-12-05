# Import data
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2023\day4\day4_input.txt") as card_data:
    cards = [line.strip("\n") for line in card_data]

# TEST DATA
#with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2023\day4\day4_test-input.txt") as test_card_data:
#    test_cards = [line.strip("\n") for line in test_card_data]


# further massage
def CardMassage(list_of_cards):
    
    massaged_cards = []

    for line_num, card in enumerate(list_of_cards):
        first_split = card.split(":")
        second_split = first_split[1].split("|")
        massaged_cards.append(second_split)
    
    # return a list of 2-element lists
    return massaged_cards


# get the points of each card
def GetCardPoints(single_card):
    #single_card is a list of length two, i.e [winning numbers, card numbers]

    # get integer winning and card numbers
    winners = [int(i) for i in single_card[0].split(" ") if i != ""]
    mynums = [int(j) for j in single_card[1].split(" ") if j != ""]

    hits = 0
    
    for n in mynums:
        if n in winners:
            hits += 1
    
    if hits == 0:
        return hits
    else:
        return 2**(hits-1)


# calculate total points of all cards
def SumOfCardPoints(cardlist):
    
    # call CardMassage
    massaged_cards = CardMassage(cardlist)

    # keep track of points
    tot_points = 0

    for scratchcard in massaged_cards:
        tot_points += GetCardPoints(scratchcard)
    
    return tot_points


# print solution
sol = SumOfCardPoints(cards)
print(sol)