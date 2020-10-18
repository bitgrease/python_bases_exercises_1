cats_w_hats = {}
tru_cats = []
for x in range(1,101):
    cats_w_hats[x] = False

for round in range(1,101):
    for cat in cats_w_hats.keys():
        if cat % round == 0:
            cats_w_hats[cat] = not(cats_w_hats[cat])

for cat in range(1,101):
    if cats_w_hats[cat]:
        tru_cats.append(cat)

print(tru_cats)