fruit = input("Enter fruit name : ").capitalize()


if fruit != 'Banana':
    print('These fruit not in the list only Banana in these list')
    exit()

color = input("Enter fruit color name : ").capitalize()
    
if fruit == 'Banana':
    if color == 'Green':
        print("Unripe")
    elif color == 'Yellow':
        print('Ripe')
    elif color == 'Brown':
        print('Overripe')
    else :
        print('These not the color of Banana')

