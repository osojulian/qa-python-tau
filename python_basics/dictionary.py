stuff = {'food': 25, 'energy': 100, 'enemies':3}

#print(stuff.get('food'))

#print(stuff.items())

#print(stuff.keys())

#print(stuff.popitem())
#print(stuff)

#print(stuff.setdefault('food'))
#print(stuff)
#print(stuff.setdefault('water', 50))
#print(stuff)


new_items = {'rocks': 10, 'arrows': 5}
stuff.update(new_items)
print(stuff)


new_items = {'rocks': 3, 'arrows': 23}
stuff.update(new_items)
print(stuff)