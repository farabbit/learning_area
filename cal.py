allGuests = {'alice':{"apple":2, "pineable":3}, "bob":{"grape":4, "apple":5}}

key=[]

def totalBought(guests, item):
    numBought=0
    for guest, foodsDict in guests.items():
        numBought+=foodsDict.get(item,0)
    return numBought

for guest, foodsDict in allGuests.items():
    for food in foodsDict:
        if food not in key:
            key.append(food)
            print("---", food,':',totalBought(allGuests, food))
