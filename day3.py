import re
f = open("data3.lst")
lines =[l.replace("\n",".") for l in f.readlines()]


all_symbols = []
all_numbers = []

for y in range(len(lines)):
    line = lines[y]
    parsing_number = False
    accu_number = ""
    number_start_at = 0
    for x in range(len(line)):
        if re.match(r"\d", line[x]) and parsing_number == False:
            print("found number", line[x])
            parsing_number = True
            number_start_at = x
        if parsing_number == True:
            if re.match(r"\d", line[x]):
                accu_number += line[x]
                print(accu_number)
            else:
                parsing_number = False
                all_numbers.append(
                    (accu_number, (number_start_at, y))
                )
                accu_number = ""
        if not parsing_number and line[x] != ".":
            all_symbols.append(
                (line[x], (x, y))
            )


def are_adjacents(number, symbol):
    (n, (nx, ny)) = number
    (s, (sx, sy)) = symbol
    return ( sy >= ny - 1 and sy <= ny + 1
            and sx >= nx - 1 and sx <= nx + len(n)
    )

def symbol_adjacent(number):
    return any([are_adjacents(number, symbol) for symbol in all_symbols] )

def adjacent_numbers(symbol):
    return [number for number in all_numbers if are_adjacents(number, symbol)]


all_number_with_symbol = [ number for number in all_numbers if  symbol_adjacent(number)]
just_numbers = [int(n) for (n, (nx, ny)) in all_number_with_symbol]

print("Part 1", sum(just_numbers))

all_gears = [
    founds
    for symbol in all_symbols
    if symbol[0] == "*"
    and len(founds:=adjacent_numbers(symbol)) == 2
]

# print(all_gears)
all_ratios = [int(g[0][0])*int(g[1][0]) for g in all_gears]
print(sum(all_ratios))