import random
import itertools

hoa_thanh = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
hop_am_truong = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
ban_nhac = []

for i in range(15):
    key = random.choice(hoa_thanh)
    value = [x for x in random.choice([p for p in itertools.permutations(hop_am_truong, 3) if len(set(p)) == 3])]
    ban_nhac.append({key: value})


print(ban_nhac)
