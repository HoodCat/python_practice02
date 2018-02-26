from functools import reduce

concate = lambda acc, x: acc+x

char = ['T','h','i','s',' ','i','s',' ','a',' ','p','e','n','c','i','l','.']
replace_char = [w.replace(' ', ',') for w in char]

print(reduce(concate, char))
print(reduce(concate, replace_char))