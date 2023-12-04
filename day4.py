f = open("data4.lst")
lines =[l.strip() for l in f.readlines()]


cards = [
    (int(card[0][5:].strip()),
     {int(x) for x in card[1].split(" | ")[0].split(" ") if x != ""},
     {int(x) for x in card[1].split(" | ")[1].split(" ") if x != ""},
    )
    for line in lines
    if (card:= line.split(": "))
]

goods = [
    len(winning.intersection(mine))
    for c, winning, mine in cards
]

wins = [
    2**(good-1)
    for good in goods
    if good >= 1
]

print(wins)
print(sum(wins))


multiplicity = [1] * len(lines)

for i, g in enumerate(goods):
    # print(cards[i], "wins", g)
    for j in range(g):
        # print("\tadding", multiplicity[i], "cards" , i+j+1+1)
        multiplicity[i+j+1] += multiplicity[i]

print(multiplicity)
print(sum(multiplicity))