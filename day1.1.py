import pandas as pd
import re

strings = pd.read_csv("data1.lst", header=None, delim_whitespace=True)[0].values.tolist()

# Part 1

onlydigits = [re.sub(r'([a-z\[\]]+)', '', x) for x in strings]

#twodigits = [d[0] if len(d)==1 else d[0]+d[-1] for d in onlydigits]
twodigits = [d[0]+d[-1] for d in onlydigits]

numbers = [int(d) for d in twodigits]

print(numbers)

somme = sum(numbers)

print(somme)
breakpoint()

