f = open("data2.1.lst")
lines =[l.strip() for l in f.readlines()]

def possible(myset):
    print("testing", myset)
    return ( myset.get("red", 0) <= 12
         and myset.get("green", 0) <= 13
         and myset.get("blue", 0) <= 14
    )



games = [
    (int(game[0][5:]), 
     [{o[1]:int(o[0])
       for it in sets
       if (o:=it.split(" "))
     }
         for tirage in game[1].split("; ")
         if (sets := tirage.split(", "))
     ]
     ) for l in lines
     if (game := l.split(": "))
]

possibles = [
    i
    for i,g in games
    if all([possible(t) for t in g])
]

print(possibles)
print(sum(possibles))
