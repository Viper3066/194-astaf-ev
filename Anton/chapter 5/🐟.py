flowers_set = ["rose", "jasmine", "lily"]
flowers_set1 = ["orchid", "tulip", "violet", "daisy"]
flowers_set2 = ["lavender", "sunflower"]
sea_fish        = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

a=[sea_fish+freshwater_fish]
a=(sorted(([i.capitalize() for i in sea_fish ]+[i.capitalize() for i in freshwater_fish])))

for i in a:
    for i1 in sea_fish:
        if i==i1.capitalize():
            a[a.index(i)]=i1
    for i1 in freshwater_fish:
        if i==i1.capitalize():
            a[a.index(i)]=i1
print(a)