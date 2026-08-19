import random

# Fisher-Yates Shuffler for Lists

def list_shuffle(arr: list)-> list:
    last = len(arr)-1
    while last > 0:
        rand = random.choice(range(0 , last+1))
        temp = arr[last]
        arr[last] = arr[rand]
        arr[rand] = temp
        last -= 1
    print (arr)
    return arr


