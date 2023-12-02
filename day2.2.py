import math

f = open("data2.lst")
lines =[l.strip() for l in f.readlines()]


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

def minoftirages(tirages):
    mins = {
        "red": 0,
        "green": 0,
        "blue":0
    }
    for t in tirages:
        for col in t.keys():
            mins[col] = max(mins[col], t[col])
    return mins


allmins = [minoftirages(g) for i, g in games]

powers = [math.prod(m.values()) for m in allmins]
print(powers)
print(sum(powers))