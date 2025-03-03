items = ['apple','banana','orange','appple','mango']
unique_item = set()

for item in items :
    if item in unique_item:
        print('Duplicate',item)
        break
    new =unique_item.add(item)
print(new)
