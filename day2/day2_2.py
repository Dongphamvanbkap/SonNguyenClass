import random
import itertools

hoa_thanh = [{'C': ['do', 'mi', 'sol']}, {'D': ['re', 'fa', 'la']}, {'E': ['mi', 'sol', 'si']}, {'F': ['fa', 'la', 'do']}, {'G': ['sol', 'si', 're']}, {'A': ['la', 'do', 'mi']}, {'B': ['si', 're', 'fa']}]
ban_nhac = []

for i in range(15):
    dictz_rand = random.choice(hoa_thanh)
    ban_nhac.append(dictz_rand)


print(ban_nhac)
