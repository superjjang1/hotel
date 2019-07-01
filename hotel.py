# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.

hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson'],
        '102': [],
        '103':['Wally World','Jeff Goldstein']
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
        '240': ['Anne Smith', 'Leslie Park'],
        '238': []
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

print("Good morning! Welcome to our small Hotel.")

def checkin():
    checkin = input("Would you like to check in?: ('y'/'n') ")
    if checkin == 'y'  or 'n':
        if checkin.lower() == ('y'):
            print(hotel.keys())
        elif checkin.lower() == ('n'):
            print("Okay, are you checking out ('y'/'n'): ")
        else:
            print("That's not an option.")

checkin()

floorho = hotel.keys()
print("These are the floors that we have available, which room would you like to check in?")
def checkfloor():
    checkfloor = input("Floor 1, floor 2, floor 3? ('1','2', or '3'): ")
    floorho = hotel.get()
    while checkfloor == range(1,3):
        if checkfloor.lower() == ('1'):
            print(floorho('1'))
        elif checkfloor.lower() == ('2'):
            print(floorho('2'))
        elif checkfloor.lower() == ('3'):
            print(floorho('3'))
        else:
            print("We don't have that floor.")
checkfloor()